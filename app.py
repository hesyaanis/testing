import os
import sys
import time
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt

from recommender import load_catalog, load_pc_catalog, find_recommendations, format_rupiah, search_pc_components
from bot_persona import (
    generate_local_response, ask_gemini_api, predict_intent_ml,
    SPECIALISTS, detect_specialist_domain
)

env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path=env_path, override=True)

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

console = Console()

def display_banner(api_mode: str, current_mode: str = "auto"):
    """Menampilkan header aplikasi dengan 2 spesialis AI terpisah."""
    console.clear()
    mode_desc = {
        "auto": "🔄 Auto-Detect Cerdas (Sistem otomatis memilihkan ahli yang tepat)",
        "laptop": "💻 Fokus Konsultan Laptop (Bersama Mas Aris)",
        "pc": "🛠️ Fokus Master Builder PC (Bersama Mas Dimas)"
    }.get(current_mode, "🔄 Auto-Detect")

    banner_text = (
        "[bold cyan]🏪 DUAL AI KONSULTAN TEKNOLOGI (LAPTOP & CUSTOM PC SOLUTION)[/bold cyan]\n"
        "[dim]Toko Resmi Bergaransi Distributor • 500 Unit Laptop & 542 Komponen PC Siap Rakit[/dim]\n\n"
        "👥 [bold white]Spesialis Toko yang Siaga Melayani Anda:[/bold white]\n"
        "   1. [bold cyan]💻 Aris[/bold cyan]  : [cyan]Senior Laptop Consultant[/cyan] (Mobilitas, Baterai, Layar OLED/IPS, Laptop Mahasiswa/Kantor/Gaming)\n"
        "   2. [bold green]🛠️ Dimas[/bold green] : [green]Senior PC Master Builder[/green] (Rakit PC Custom, Kompatibilitas 8 Part, PSU 80+, Bottleneck, Part Parsial)\n\n"
        f"Mode Konsultasi : [bold magenta]{mode_desc}[/bold magenta]\n"
        f"Mesin Pemroses  : [bold {'green' if 'Gemini' in api_mode else 'yellow'}]{api_mode}[/bold {'green' if 'Gemini' in api_mode else 'yellow'}]"
    )
    console.print(Panel(banner_text, border_style="cyan", padding=(1, 2)))

def display_pc_catalog(pc_catalog, filter_query=""):
    """Menampilkan tabel katalog komponen PC dengan ringkasan & filter."""
    filtered = search_pc_components(filter_query, pc_catalog, limit=50) if filter_query else pc_catalog
    
    filter_info = f"Filter: '{filter_query}' - " if filter_query else ""
    title = f"🛠️ GUDANG KOMPONEN PC TOKO ({filter_info}{len(filtered)} Part dari Total {len(pc_catalog)} Komponen)"
    table = Table(title=title, border_style="green", show_lines=True)
    table.add_column("No", justify="center", style="dim", width=4)
    table.add_column("ID", justify="center", style="cyan", width=9)
    table.add_column("Nama Komponen PC", style="bold white", width=36)
    table.add_column("Kategori", style="magenta", width=22)
    table.add_column("Harga", justify="right", style="green", width=14)
    table.add_column("Spesifikasi Kunci", style="yellow")
    table.add_column("Stok", justify="center", style="white", width=6)

    display_items = filtered[:15]
    for idx, item in enumerate(display_items, 1):
        spec = item.get("spesifikasi_ringkas", "-")
        table.add_row(
            str(idx),
            item["id"],
            item["nama"],
            item["kategori"],
            format_rupiah(item["harga"]),
            spec[:45] + ("..." if len(spec) > 45 else ""),
            str(item["stok"])
        )

    console.print(table)
    if len(filtered) > 15:
        console.print(f"[dim]ℹ️ Menampilkan 15 teratas dari {len(filtered)} part. Ketik '[bold yellow]katalog pc [part/brand][/bold yellow]' (contoh: 'katalog pc vga', 'katalog pc ryzen', 'katalog pc rtx', 'katalog pc ram')[/dim]\n")
    else:
        console.print()

def display_catalog(catalog, filter_query=""):
    """Menampilkan tabel katalog laptop dengan ringkasan & filter untuk 500 produk."""
    filtered = catalog
    if filter_query:
        fq = filter_query.lower().strip()
        filtered = [
            item for item in catalog
            if fq in item["nama"].lower()
            or fq in item["brand"].lower()
            or fq in item["kategori"].lower()
            or fq in item["spesifikasi"]["gpu"].lower()
            or fq in item["spesifikasi"]["prosesor"].lower()
        ]

    filter_info = f"Filter: '{filter_query}' - " if filter_query else ""
    title = f"📦 DAFTAR STOK LAPTOP TOKO ({filter_info}{len(filtered)} Laptop dari Total {len(catalog)} Unit)"
    table = Table(title=title, border_style="cyan", show_lines=True)
    table.add_column("No", justify="center", style="dim", width=4)
    table.add_column("Nama Laptop", style="bold white", width=30)
    table.add_column("Harga", justify="right", style="green", width=14)
    table.add_column("Kategori", style="cyan", width=24)
    table.add_column("Dapur Pacu (CPU | GPU | RAM)", style="yellow")
    table.add_column("Stok", justify="center", style="magenta", width=6)

    display_items = filtered[:15]
    for idx, item in enumerate(display_items, 1):
        specs = item["spesifikasi"]
        cpu_short = specs['prosesor'].split('(')[0].strip()
        gpu_short = specs['gpu'].split('(')[0].strip()
        ram_short = specs['ram'].split('(')[0].strip()
        ringkasan_spek = f"{cpu_short} | {gpu_short} | {ram_short}"
        table.add_row(
            str(idx),
            item["nama"],
            format_rupiah(item["harga"]),
            item["kategori"],
            ringkasan_spek,
            str(item["stok"])
        )

    console.print(table)
    if len(filtered) > 15:
        console.print(f"[dim]ℹ️ Menampilkan 15 teratas dari {len(filtered)} unit. Ketik '[bold yellow]katalog [brand/spek][/bold yellow]' (contoh: 'katalog asus', 'katalog rtx', 'katalog lenovo')[/dim]\n")
    else:
        console.print()

def display_help():
    """Menampilkan panduan interaktif konsultasi."""
    tips = (
        "[bold green]Panduan Percakapan & Kontrol AI Spesialis:[/bold green]\n"
        "1. [bold cyan]Konsultasi Laptop:[/bold cyan] [italic]'Saya cari laptop enteng baterai awet buat kuliah budget 7jt.'[/italic] (Dijawab oleh [bold cyan]Aris[/bold cyan])\n"
        "2. [bold green]Konsultasi Rakit PC:[/bold green] [italic]'Saya punya budget 10 juta racikkan sampai nyala'[/italic] atau [italic]'Saya sudah beli VGA, bagusnya part sisanya apa?'[/italic] (Dijawab oleh [bold green]Dimas[/bold green])\n"
        "3. [bold yellow]Ganti Spesialis Manual:[/bold yellow]\n"
        "   • Ketik [bold cyan]'mode laptop'[/bold cyan] atau [bold cyan]'tanya aris'[/bold cyan] -> Khusus konsultasi laptop\n"
        "   • Ketik [bold green]'mode pc'[/bold green] atau [bold green]'tanya dimas'[/bold green] -> Khusus konsultasi rakit PC & hardware\n"
        "   • Ketik [bold magenta]'mode auto'[/bold magenta] -> Otomatis berganti sesuai topik Anda\n"
        "4. [bold yellow]Cek Stok Barang:[/bold yellow] Ketik [bold yellow]'katalog'[/bold yellow] (laptop) atau [bold yellow]'katalog pc'[/bold yellow] (komponen PC / vga / cpu / ram / psu).\n"
        "5. [bold red]Reset & Keluar:[/bold red] Ketik [bold magenta]'reset'[/bold magenta] untuk mengulang, atau [bold red]'keluar'[/bold red] untuk selesai."
    )
    console.print(Panel(tips, title="💡 Panduan Konsultasi Pelanggan", border_style="dim", padding=(1, 2)))
    console.print()

def main():
    catalog = load_catalog()
    pc_catalog = load_pc_catalog()
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    
    current_specialist_mode = "auto"
    api_mode = "🌐 Cloud LLM (Google Gemini)" if api_key else "⚡ Smart Local Engine (Offline / Cepat)"
    
    display_banner(api_mode, current_specialist_mode)
    display_help()

    console.print("[bold cyan]Konsultan Toko:[/bold cyan] Selamat datang di Sahabat Laptop & PC Solution! Kami memiliki Mas [bold cyan]Aris[/bold cyan] (Spesialis Laptop) dan Mas [bold green]Dimas[/bold green] (Master Builder PC). Ada yang ingin Anda diskusikan hari ini?\n")

    chat_history = []

    while True:
        try:
            mode_tag = f"[{current_specialist_mode.upper()}] " if current_specialist_mode != "auto" else ""
            user_input = Prompt.ask(f"[bold white]Pelanggan {mode_tag}[/bold white]").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n[bold yellow]Terima kasih telah berkunjung. Semoga hari Anda menyenangkan![/bold yellow]")
            break

        if not user_input:
            continue

        u_low = user_input.lower().strip()

        if u_low in ["keluar", "exit", "quit", "q"]:
            console.print("\n[bold cyan]Konsultan Toko:[/bold cyan] Terima kasih telah berkonsultasi di Sahabat Laptop & PC Solution. Kami siap membantu kembali kapan pun Anda membutuhkan rekomendasi teknologi. Selamat beraktivitas! 👋\n")
            break

        if u_low in ["reset", "clear", "ulang"]:
            chat_history = []
            console.print("\n[bold cyan]Konsultan Toko:[/bold cyan] Sesi percakapan telah kami atur ulang. Silakan sampaikan kebutuhan teknologi yang ingin Anda diskusikan.\n")
            continue

        # Perintah ganti spesialis manual
        if u_low in ["mode pc", "tanya dimas", "ke dimas", "pilih pc", "spesialis pc"]:
            current_specialist_mode = "pc"
            spec = SPECIALISTS["pc"]
            console.print(f"\n[bold green]{spec['icon']} Mode Terkunci ke {spec['name']} ({spec['title']})[/bold green]")
            console.print(f"[dim green]{spec['greeting']}[/dim green]\n")
            continue

        if u_low in ["mode laptop", "tanya aris", "ke aris", "pilih laptop", "spesialis laptop"]:
            current_specialist_mode = "laptop"
            spec = SPECIALISTS["laptop"]
            console.print(f"\n[bold cyan]{spec['icon']} Mode Terkunci ke {spec['name']} ({spec['title']})[/bold cyan]")
            console.print(f"[dim cyan]{spec['greeting']}[/dim cyan]\n")
            continue

        if u_low in ["mode auto", "auto", "mode otomatis", "pilih auto"]:
            current_specialist_mode = "auto"
            console.print("\n[bold magenta]🔄 Mode Otomatis Aktif:[/bold magenta] [dim]Sistem akan secara cerdas memanggil Mas Aris (Laptop) atau Mas Dimas (PC) sesuai kebutuhan topik Anda.[/dim]\n")
            continue

        # Perintah cek stok / katalog
        if u_low.startswith("katalog") or u_low.startswith("stok") or u_low in ["list", "daftar"]:
            parts = user_input.split(maxsplit=1)
            filter_arg = parts[1].strip() if len(parts) > 1 else ""
            
            is_pc_catalog_req = "pc" in filter_arg.lower() or any(w in filter_arg.lower() for w in [
                "vga", "gpu", "cpu", "prosesor", "mobo", "motherboard", "ram", "psu", "casing", "cooler", "monitor", "ssd", "nvme", "storage", "hdd"
            ])
            
            if is_pc_catalog_req or current_specialist_mode == "pc":
                clean_filter = filter_arg.lower().replace("pc", "").strip()
                display_pc_catalog(pc_catalog, clean_filter)
            else:
                display_catalog(catalog, filter_arg)
            continue

        # Simpan pesan pembeli ke riwayat ingatan
        chat_history.append({"role": "user", "content": user_input})
        if len(chat_history) > 12:
            chat_history = chat_history[-12:]

        # Deteksi awal siapa yang akan merespon untuk spinner
        expected_spec = detect_specialist_domain(user_input, current_mode=current_specialist_mode, chat_history=chat_history)
        spec_info = SPECIALISTS.get(expected_spec, SPECIALISTS["laptop"])
        spinner_msg = f"[bold {spec_info['color']}]{spec_info['name']} sedang menganalisis & menyiapkan respon...[/bold {spec_info['color']}]"

        # Proses Respon
        with console.status(spinner_msg, spinner="dots"):
            response_text = None
            active_spec = expected_spec
            engine_used = "Smart Local Engine"
            
            # 1. Coba Gemini API
            if api_key:
                res, spec_used = ask_gemini_api(chat_history, catalog, api_key, specialist=current_specialist_mode)
                if res:
                    response_text = res
                    active_spec = spec_used
                    engine_used = "Cloud LLM (Gemini)"

            # 2. Local Fallback jika offline / API limit
            if not response_text:
                recommendations = find_recommendations(user_input, catalog, limit=2)
                res, spec_used = generate_local_response(
                    user_input, recommendations, catalog,
                    pc_catalog=pc_catalog, chat_history=chat_history,
                    specialist=current_specialist_mode
                )
                response_text = res
                active_spec = spec_used
                engine_used = "Smart Local Engine"

        # Simpan balasan konsultan ke riwayat ingatan
        chat_history.append({"role": "model", "content": response_text})

        # Ambil metadata spesialis yang menjawab
        responding_spec = SPECIALISTS.get(active_spec, SPECIALISTS["laptop"])
        color = responding_spec["color"]

        ml_intent, ml_conf = predict_intent_ml(user_input)
        memory_indicator = f"💾 Memori: {len(chat_history)} pesan"
        engine_badge = f"🌐 {engine_used}" if "Gemini" in engine_used else f"⚡ {engine_used}"
        intent_info = f"🧠 ML: {ml_intent} ({ml_conf:.0f}%)" if ml_intent else ""
        subtitle_text = f"[{color}]{responding_spec['badge']} • {responding_spec['catalog_desc']} • {memory_indicator} • {engine_badge}[/{color}]"

        # Cetak Balasan dengan efek panel spesialis yang sesuai
        console.print()
        console.print(Panel(
            Markdown(response_text),
            title=f"[bold {color}]{responding_spec['icon']} {responding_spec['name']} ({responding_spec['title']})[/bold {color}]",
            subtitle=subtitle_text,
            border_style=color,
            padding=(1, 2)
        ))
        console.print()

if __name__ == "__main__":
    main()
