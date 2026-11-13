import os
import sys
import json
from flask import Flask, request, jsonify, render_template, send_from_directory
from dotenv import load_dotenv

# Muat environment
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path=env_path, override=True)

from recommender import (
    load_catalog, load_pc_catalog, find_recommendations,
    search_pc_components, build_pc_rig_from_catalog, format_rupiah
)
from bot_persona import (
    ask_gemini_api, generate_local_response, predict_intent_ml,
    SPECIALISTS, detect_specialist_domain, append_pc_safety_disclaimer_if_needed
)

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

app = Flask(__name__, static_folder="static", template_folder="templates")

# Muat database katalog
LAPTOP_CATALOG = load_catalog()
PC_CATALOG = load_pc_catalog()

@app.route("/")
def index():
    """Halaman utama portal konsultasi web."""
    return render_template("index.html")

@app.route("/api/specialists", methods=["GET"])
def get_specialists():
    """Mengembalikan metadata spesialis AI toko."""
    return jsonify({
        "status": "success",
        "specialists": SPECIALISTS,
        "stats": {
            "total_laptops": len(LAPTOP_CATALOG),
            "total_pc_components": len(PC_CATALOG)
        }
    })

@app.route("/api/chat", methods=["POST"])
def chat():
    """Endpoint pemrosesan chat konsultasi dengan memori percakapan."""
    data = request.get_json() or {}
    user_message = data.get("message", "").strip()
    chat_history = data.get("history", [])
    specialist_mode = data.get("specialist", "auto")

    if not user_message:
        return jsonify({"status": "error", "message": "Pesan tidak boleh kosong"}), 400

    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    
    # 1. Tambahkan pesan user ke histori
    full_history = list(chat_history)
    full_history.append({"role": "user", "content": user_message})
    
    # Batasi histori percakapan maksimal 12 turn agar efisien
    if len(full_history) > 12:
        full_history = full_history[-12:]

    # 2. Proses jawaban melalui Cloud LLM (Gemini) atau Local Smart Engine
    response_text = None
    engine_used = "Smart Local Engine"
    active_spec = detect_specialist_domain(user_message, current_mode=specialist_mode, chat_history=full_history)

    if api_key:
        res, spec_used = ask_gemini_api(full_history, LAPTOP_CATALOG, api_key, specialist=specialist_mode)
        if res:
            response_text = res
            active_spec = spec_used
            engine_used = "Cloud LLM (Gemini)"

    if not response_text:
        recommendations = find_recommendations(user_message, LAPTOP_CATALOG, limit=3)
        res, spec_used = generate_local_response(
            user_message, recommendations, LAPTOP_CATALOG,
            pc_catalog=PC_CATALOG, chat_history=full_history,
            specialist=specialist_mode
        )
        response_text = res
        active_spec = spec_used
        engine_used = "Smart Local Engine"

    # Pastikan disclaimer keamanan perakitan terpasang jika spesialis PC (Dimas)
    if active_spec == "pc" and response_text:
        response_text = append_pc_safety_disclaimer_if_needed(response_text, user_message)

    # Prediksi intent ML untuk telemetry
    ml_intent, ml_conf = predict_intent_ml(user_message)
    spec_info = SPECIALISTS.get(active_spec, SPECIALISTS["laptop"])

    return jsonify({
        "status": "success",
        "reply": response_text,
        "specialist": active_spec,
        "specialist_info": spec_info,
        "engine_used": engine_used,
        "ml_intent": ml_intent,
        "ml_confidence": round(ml_conf, 1)
    })

@app.route("/api/catalog/laptops", methods=["GET"])
def get_laptops():
    """Endpoint pencarian & filter 500 unit laptop."""
    query = request.args.get("query", "").lower().strip()
    brand = request.args.get("brand", "").lower().strip()
    limit = int(request.args.get("limit", 20))
    offset = int(request.args.get("offset", 0))

    filtered = LAPTOP_CATALOG
    if brand:
        filtered = [x for x in filtered if x["brand"].lower() == brand]
    if query:
        filtered = [
            x for x in filtered
            if query in x["nama"].lower()
            or query in x["kategori"].lower()
            or query in x["spesifikasi"]["gpu"].lower()
            or query in x["spesifikasi"]["prosesor"].lower()
        ]

    total = len(filtered)
    results = filtered[offset:offset + limit]

    return jsonify({
        "status": "success",
        "total": total,
        "offset": offset,
        "limit": limit,
        "items": results
    })

@app.route("/api/catalog/pc", methods=["GET"])
def get_pc_components():
    """Endpoint pencarian & filter 542 komponen PC."""
    query = request.args.get("query", "").strip()
    category = request.args.get("category", "").strip()
    limit = int(request.args.get("limit", 20))

    filtered = PC_CATALOG
    if category:
        filtered = [x for x in filtered if x["kategori"].lower() == category.lower()]
    
    if query:
        filtered = search_pc_components(query, filtered, limit=limit)
    else:
        filtered = filtered[:limit]

    return jsonify({
        "status": "success",
        "total_catalog": len(PC_CATALOG),
        "count": len(filtered),
        "items": filtered
    })

@app.route("/api/pc/build-rig", methods=["POST"])
def build_rig():
    """Endpoint simulasi rakit 8 komponen PC sesuai budget."""
    data = request.get_json() or {}
    budget = int(data.get("budget", 10000000))
    
    rig = build_pc_rig_from_catalog(budget, PC_CATALOG)
    return jsonify({
        "status": "success",
        "rig": rig
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Server Konsultan Web Sahabat Laptop & PC Solution aktif di http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
