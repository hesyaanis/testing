/**
 * SAHABAT TECH - DUAL AI TECH CONSULTANT JAVASCRIPT APP
 * State management, chat rendering, modal catalogs, and live rig building
 */

// Application State
let chatHistory = [];
let currentSpecialistMode = 'auto'; // 'auto' | 'laptop' | 'pc'
let isWaitingResponse = false;
let specialistsMeta = {
  laptop: {
    name: 'Aris',
    title: 'Senior Laptop Consultant',
    color: 'cyan',
    badge: 'Spesialis Laptop',
    icon: 'fa-laptop'
  },
  pc: {
    name: 'Dimas',
    title: 'Senior PC Master Builder',
    color: 'green',
    badge: 'Master Builder PC',
    icon: 'fa-screwdriver-wrench'
  }
};

// DOM Elements
const messagesContainer = document.getElementById('messagesContainer');
const chatForm = document.getElementById('chatForm');
const messageInput = document.getElementById('messageInput');
const btnSend = document.getElementById('btnSend');
const headerAvatar = document.getElementById('headerAvatar');
const headerSpecialistName = document.getElementById('headerSpecialistName');
const headerSpecialistRole = document.getElementById('headerSpecialistRole');
const activeModeLabel = document.getElementById('activeModeLabel');
const welcomeCard = document.getElementById('welcomeCard');

// Mode Switcher Buttons
const modeBtnAuto = document.getElementById('modeBtnAuto');
const modeBtnLaptop = document.getElementById('modeBtnLaptop');
const modeBtnPC = document.getElementById('modeBtnPC');

// Modals
const modalLaptop = document.getElementById('modalLaptop');
const modalPC = document.getElementById('modalPC');
const modalRigBuilder = document.getElementById('modalRigBuilder');

// Initialization
document.addEventListener('DOMContentLoaded', () => {
  setupEventListeners();
  setupTextareaAutoResize();
  loadInitialMeta();
  setSpecialistMode('auto', false);
});

async function loadInitialMeta() {
  try {
    const res = await fetch('/api/specialists');
    const data = await res.json();
    if (data.status === 'success' && data.specialists) {
      specialistsMeta = data.specialists;
    }
  } catch (err) {
    console.warn('Gagal memuat metadata spesialis:', err);
  }
}

// Event Listeners
function setupEventListeners() {
  // Chat submit
  chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    handleUserSubmit();
  });

  // Enter to send (Shift+Enter for newline)
  messageInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleUserSubmit();
    }
  });

  // Mode Buttons
  modeBtnAuto.addEventListener('click', () => setSpecialistMode('auto'));
  modeBtnLaptop.addEventListener('click', () => setSpecialistMode('laptop'));
  modeBtnPC.addEventListener('click', () => setSpecialistMode('pc'));

  // Sidebar Mobile Toggle
  const btnOpenSidebar = document.getElementById('btnOpenSidebar');
  const btnCloseSidebar = document.getElementById('btnCloseSidebar');
  const sidebar = document.getElementById('sidebar');

  if (btnOpenSidebar && sidebar) {
    btnOpenSidebar.addEventListener('click', () => sidebar.classList.add('open'));
  }
  if (btnCloseSidebar && sidebar) {
    btnCloseSidebar.addEventListener('click', () => sidebar.classList.remove('open'));
  }

  // Reset Chat
  document.getElementById('btnResetChat').addEventListener('click', resetChatSession);

  // Quick prompt chips in sidebar
  document.querySelectorAll('.prompt-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const text = chip.getAttribute('data-prompt');
      if (text) {
        sendQuickMessage(text);
        if (sidebar) sidebar.classList.remove('open');
      }
    });
  });

  // Modal Openers
  document.getElementById('btnOpenLaptopModal').addEventListener('click', () => openLaptopCatalogModal());
  document.getElementById('btnOpenPCModal').addEventListener('click', () => openPCCatalogModal());
  document.getElementById('btnOpenRigBuilder').addEventListener('click', () => openRigBuilderModal());

  // Search input listeners in modals
  setupModalSearchListeners();
}

function setupTextareaAutoResize() {
  messageInput.addEventListener('input', () => {
    messageInput.style.height = 'auto';
    messageInput.style.height = Math.min(messageInput.scrollHeight, 140) + 'px';
  });
}

// Mode Switcher Handler
function setSpecialistMode(mode, notify = true) {
  currentSpecialistMode = mode;

  // Toggle button active states
  [modeBtnAuto, modeBtnLaptop, modeBtnPC].forEach(btn => btn.classList.remove('active'));
  headerAvatar.className = 'consultant-avatar-box';

  if (mode === 'laptop') {
    modeBtnLaptop.classList.add('active');
    headerAvatar.classList.add('laptop');
    headerAvatar.innerHTML = '<i class="fa-solid fa-laptop"></i>';
    headerSpecialistName.innerText = 'Mas Aris';
    headerSpecialistRole.innerText = 'Senior Laptop Consultant';
    activeModeLabel.innerHTML = '<i class="fa-solid fa-circle-dot text-cyan"></i> Mode: Aris (Spesialis Laptop Aktif)';
    messageInput.placeholder = 'Tanyakan laptop impian Anda ke Mas Aris...';
    if (notify) showSystemNotice('Mode beralih ke 💻 Mas Aris (Spesialis Laptop). Silakan tanyakan seputar unit laptop resmi!');
  } else if (mode === 'pc') {
    modeBtnPC.classList.add('active');
    headerAvatar.classList.add('pc');
    headerAvatar.innerHTML = '<i class="fa-solid fa-screwdriver-wrench"></i>';
    headerSpecialistName.innerText = 'Mas Dimas';
    headerSpecialistRole.innerText = 'Senior PC Master Builder';
    activeModeLabel.innerHTML = '<i class="fa-solid fa-circle-dot text-green"></i> Mode: Dimas (Master Builder PC Aktif)';
    messageInput.placeholder = 'Konsultasikan rakitan PC atau komponen desktop ke Mas Dimas...';
    if (notify) showSystemNotice('Mode beralih ke 🛠️ Mas Dimas (Master Builder PC). Tanyakan racikan PC, part, atau komponen yang sudah Anda miliki!');
  } else {
    modeBtnAuto.classList.add('active');
    headerAvatar.classList.add('auto');
    headerAvatar.innerHTML = '<i class="fa-solid fa-wand-magic-sparkles"></i>';
    headerSpecialistName.innerText = 'Aris & Dimas';
    headerSpecialistRole.innerText = 'Dual AI Tech Consultant (Auto-Detect)';
    activeModeLabel.innerHTML = '<i class="fa-solid fa-circle-dot text-purple"></i> Mode: Auto-Detect (Aris & Dimas Siaga)';
    messageInput.placeholder = 'Tanyakan rekomendasi laptop atau konsultasi rakit PC impian Anda...';
  }
}

// Chat Sending Pipeline
async function handleUserSubmit() {
  const text = messageInput.value.trim();
  if (!text || isWaitingResponse) return;

  // Hide welcome hero on first conversation
  if (welcomeCard) {
    welcomeCard.style.display = 'none';
  }

  // Clear input
  messageInput.value = '';
  messageInput.style.height = 'auto';

  // 1. Render User Bubble
  appendMessageBubble('user', text);

  // 2. Render Typing Indicator
  isWaitingResponse = true;
  btnSend.disabled = true;
  const typingRow = showTypingIndicator();

  try {
    const payload = {
      message: text,
      history: chatHistory,
      specialist: currentSpecialistMode
    };

    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    typingRow.remove();

    if (data.status === 'success') {
      const activeSpec = data.specialist || 'laptop';
      appendMessageBubble('bot', data.reply, activeSpec, data.engine_used);
      
      // Update memory
      chatHistory.push({ role: 'user', content: text });
      chatHistory.push({ role: 'model', content: data.reply });
      if (chatHistory.length > 12) chatHistory = chatHistory.slice(-12);

      // If auto mode, update header to reflect who replied
      if (currentSpecialistMode === 'auto') {
        updateHeaderSpecialistBadge(activeSpec);
      }
    } else {
      appendMessageBubble('bot', 'Mohon maaf Kak, terjadi kendala saat memproses jawaban. Silakan coba kembali sesaat lagi.', 'laptop');
    }
  } catch (error) {
    console.error('Chat error:', error);
    typingRow.remove();
    appendMessageBubble('bot', '⚠️ **Koneksi Terputus**: Tidak dapat terhubung ke server backend (`http://localhost:5000`). Mohon pastikan perintah `python server.py` sedang berjalan di terminal Anda, lalu coba kirim pesan kembali.', 'laptop');
  } finally {
    isWaitingResponse = false;
    btnSend.disabled = false;
    messageInput.focus();
  }
}

function sendQuickMessage(text) {
  messageInput.value = text;
  handleUserSubmit();
}

function updateHeaderSpecialistBadge(activeSpec) {
  if (activeSpec === 'pc') {
    headerAvatar.className = 'consultant-avatar-box pc';
    headerAvatar.innerHTML = '<i class="fa-solid fa-screwdriver-wrench"></i>';
    headerSpecialistName.innerText = 'Mas Dimas';
    headerSpecialistRole.innerText = 'Senior PC Master Builder';
  } else {
    headerAvatar.className = 'consultant-avatar-box laptop';
    headerAvatar.innerHTML = '<i class="fa-solid fa-laptop"></i>';
    headerSpecialistName.innerText = 'Mas Aris';
    headerSpecialistRole.innerText = 'Senior Laptop Consultant';
  }
}

// Render Message Bubbles
function appendMessageBubble(sender, text, specialist = 'laptop', engine = 'Smart Local Engine') {
  const row = document.createElement('div');
  row.className = `message-row ${sender}`;

  const timeStr = new Date().toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' });

  if (sender === 'user') {
    row.innerHTML = `
      <div class="msg-avatar user-avatar"><i class="fa-regular fa-user"></i></div>
      <div class="msg-body-wrapper">
        <div class="msg-header-meta">
          <span class="msg-sender-name">Anda</span>
          <span class="msg-time">${timeStr}</span>
        </div>
        <div class="msg-bubble">${escapeHtml(text)}</div>
      </div>
    `;
  } else {
    row.classList.add(specialist);
    const specInfo = specialistsMeta[specialist] || specialistsMeta.laptop;
    const badgeClass = specialist === 'pc' ? 'green' : 'cyan';
    const parsedMarkdown = typeof marked !== 'undefined' ? marked.parse(text) : escapeHtml(text);

    row.innerHTML = `
      <div class="msg-avatar ${specialist}">
        <i class="fa-solid ${specInfo.icon || (specialist === 'pc' ? 'fa-screwdriver-wrench' : 'fa-laptop')}"></i>
      </div>
      <div class="msg-body-wrapper">
        <div class="msg-header-meta">
          <span class="msg-sender-name">${specInfo.name || 'Konsultan'}</span>
          <span class="msg-badge ${badgeClass}">${specInfo.badge || 'Konsultan'}</span>
          <span class="msg-time">${timeStr}</span>
        </div>
        <div class="msg-bubble">${parsedMarkdown}</div>
      </div>
    `;
  }

  messagesContainer.appendChild(row);
  scrollToBottom();
}

function showTypingIndicator() {
  const typingRow = document.createElement('div');
  typingRow.className = 'typing-indicator-row';
  typingRow.id = 'typingIndicator';
  
  const targetName = currentSpecialistMode === 'pc' ? 'Mas Dimas' : (currentSpecialistMode === 'laptop' ? 'Mas Aris' : 'Konsultan');
  typingRow.innerHTML = `
    <div class="typing-bubble">
      <div class="typing-dot"></div>
      <div class="typing-dot"></div>
      <div class="typing-dot"></div>
    </div>
    <span class="typing-text">${targetName} sedang menganalisis & menyiapkan rekomendasi...</span>
  `;
  messagesContainer.appendChild(typingRow);
  scrollToBottom();
  return typingRow;
}

function showSystemNotice(msg) {
  const noticeRow = document.createElement('div');
  noticeRow.style.cssText = 'text-align: center; margin: 8px 0;';
  noticeRow.innerHTML = `
    <span style="display: inline-block; padding: 4px 14px; border-radius: 9999px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); font-size: 11.5px; color: #94a3b8;">
      ${msg}
    </span>
  `;
  messagesContainer.appendChild(noticeRow);
  scrollToBottom();
}

function scrollToBottom() {
  setTimeout(() => {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }, 50);
}

function resetChatSession() {
  chatHistory = [];
  messagesContainer.innerHTML = '';
  if (welcomeCard) {
    welcomeCard.style.display = 'block';
    messagesContainer.appendChild(welcomeCard);
  }
  showSystemNotice('Sesi percakapan telah diatur ulang. Silakan sampaikan kebutuhan teknologi Anda.');
}

function escapeHtml(text) {
  const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
  return text.replace(/[&<>"']/g, (m) => map[m]);
}

// =============================================================================
// MODAL LOGIC: LAPTOP CATALOG (500 UNIT)
// =============================================================================
let currentLaptopBrand = '';

function openLaptopCatalogModal() {
  modalLaptop.classList.add('open');
  loadLaptopsData();
}

async function loadLaptopsData() {
  const query = document.getElementById('laptopSearchInput').value.trim();
  const countDisplay = document.getElementById('laptopResultCount');
  const cardsContainer = document.getElementById('laptopCardsContainer');

  countDisplay.innerText = 'Mengambil data dari 500 unit stok laptop...';
  cardsContainer.innerHTML = '<p style="color:#64748b; padding:20px;">Memuat produk...</p>';

  try {
    const url = `/api/catalog/laptops?query=${encodeURIComponent(query)}&brand=${encodeURIComponent(currentLaptopBrand)}&limit=30`;
    const res = await fetch(url);
    const data = await res.json();

    if (data.status === 'success') {
      countDisplay.innerText = `Menampilkan ${data.items.length} dari total ${data.total} unit laptop yang sesuai.`;
      renderLaptopCards(data.items, cardsContainer);
    }
  } catch (err) {
    countDisplay.innerText = 'Gagal memuat katalog laptop.';
    console.error(err);
  }
}

function renderLaptopCards(items, container) {
  if (!items || items.length === 0) {
    container.innerHTML = '<p style="color:#94a3b8; grid-column: 1/-1; text-align:center; padding: 40px;">Unit tidak ditemukan untuk filter ini.</p>';
    return;
  }

  container.innerHTML = items.map(lap => {
    const specs = lap.spesifikasi;
    return `
      <div class="catalog-card">
        <div class="card-header-top">
          <span class="card-tag">${lap.kategori}</span>
          <span class="card-stock"><i class="fa-solid fa-check"></i> Stok: ${lap.stok}</span>
        </div>
        <h4>${lap.nama}</h4>
        <div class="card-price">${formatRupiahJS(lap.harga)}</div>
        <div class="card-specs-list">
          <div><i class="fa-solid fa-microchip"></i> ${specs.prosesor}</div>
          <div><i class="fa-solid fa-memory"></i> ${specs.ram} | ${specs.storage}</div>
          <div><i class="fa-solid fa-tv"></i> ${specs.layar} (${specs.berat})</div>
        </div>
        <button class="card-action-btn" onclick="consultProduct('laptop', '${lap.nama}', ${lap.harga})">
          <i class="fa-regular fa-comment-dots"></i> Tanyakan ke Mas Aris
        </button>
      </div>
    `;
  }).join('');
}

// =============================================================================
// MODAL LOGIC: PC COMPONENTS (542 PART)
// =============================================================================
let currentPCCategory = '';

function openPCCatalogModal() {
  modalPC.classList.add('open');
  loadPCData();
}

async function loadPCData() {
  const query = document.getElementById('pcSearchInput').value.trim();
  const countDisplay = document.getElementById('pcResultCount');
  const cardsContainer = document.getElementById('pcCardsContainer');

  countDisplay.innerText = 'Mengambil data dari 542 komponen PC gudang...';
  cardsContainer.innerHTML = '<p style="color:#64748b; padding:20px;">Memuat komponen...</p>';

  try {
    const url = `/api/catalog/pc?query=${encodeURIComponent(query)}&category=${encodeURIComponent(currentPCCategory)}&limit=30`;
    const res = await fetch(url);
    const data = await res.json();

    if (data.status === 'success') {
      countDisplay.innerText = `Menampilkan ${data.count} part dari total 542 komponen di gudang toko.`;
      renderPCCards(data.items, cardsContainer);
    }
  } catch (err) {
    countDisplay.innerText = 'Gagal memuat komponen PC.';
    console.error(err);
  }
}

function renderPCCards(items, container) {
  if (!items || items.length === 0) {
    container.innerHTML = '<p style="color:#94a3b8; grid-column: 1/-1; text-align:center; padding: 40px;">Komponen tidak ditemukan untuk kata kunci ini.</p>';
    return;
  }

  container.innerHTML = items.map(p => {
    const spec = p.spesifikasi_ringkas || '-';
    return `
      <div class="catalog-card">
        <div class="card-header-top">
          <span class="card-tag">${p.kategori}</span>
          <span class="card-stock"><i class="fa-solid fa-check"></i> Stok: ${p.stok}</span>
        </div>
        <h4>${p.nama}</h4>
        <div class="card-price">${formatRupiahJS(p.harga)}</div>
        <div class="card-specs-list">
          <div><strong>ID:</strong> ${p.id}</div>
          <div><strong>Spesifikasi:</strong> ${spec}</div>
          <div><strong>Garansi:</strong> ${p.garansi || 'Resmi'}</div>
        </div>
        <button class="card-action-btn pc-btn" onclick="consultProduct('pc', '${p.nama}', ${p.harga})">
          <i class="fa-solid fa-screwdriver-wrench"></i> Tanyakan ke Mas Dimas
        </button>
      </div>
    `;
  }).join('');
}

// =============================================================================
// MODAL LOGIC: RIG BUILDER SIMULATION
// =============================================================================
let currentRigData = null;

function openRigBuilderModal() {
  modalRigBuilder.classList.add('open');
  loadRigCalculation(10000000);
}

function setSliderBudget(val) {
  document.getElementById('rigBudgetSlider').value = val;
  document.querySelectorAll('.preset-btn').forEach(btn => {
    btn.classList.toggle('active', btn.innerText.includes(formatPresetMatch(val)));
  });
  loadRigCalculation(val);
}

function formatPresetMatch(val) {
  return (val / 1000000).toFixed(0) + ' Jt';
}

async function loadRigCalculation(budget) {
  const display = document.getElementById('sliderBudgetDisplay');
  const container = document.getElementById('rigResultContainer');
  display.innerText = formatRupiahJS(budget);
  container.innerHTML = '<p style="color:#64748b; padding:20px;">Meracik 8 komponen kompatibel...</p>';

  try {
    const res = await fetch('/api/pc/build-rig', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ budget })
    });
    const data = await res.json();
    if (data.status === 'success' && data.rig) {
      currentRigData = data.rig;
      renderRigResult(data.rig, container);
    }
  } catch (err) {
    container.innerHTML = '<p style="color:#ef4444;">Gagal menghitung racikan rig.</p>';
  }
}

function renderRigResult(rig, container) {
  const partsHtml = rig.parts.map(p => `
    <tr>
      <td class="cat-label">${p.kategori.replace('Processor (CPU)', 'CPU').replace('Penyimpanan (SSD / HDD)', 'SSD').replace('VGA / Kartu Grafis', 'VGA')}</td>
      <td class="part-name"><strong>${p.nama}</strong></td>
      <td class="part-price">${formatRupiahJS(p.harga)}</td>
    </tr>
  `).join('');

  container.innerHTML = `
    <div class="rig-tier-header">
      <div>
        <h4 style="font-size:16px; font-weight:700; color:#fff;">Simulasi 8 Komponen Siap Nyala</h4>
        <small style="color:#94a3b8;">100% Bebas Bottleneck & Bergaransi Resmi Distributor</small>
      </div>
      <span class="rig-tier-badge">${rig.tier || 'Custom Build'}</span>
    </div>

    <table class="rig-parts-table">
      ${partsHtml}
    </table>

    <div class="rig-summary-bar">
      <div>
        <span>Total Komponen:</span>
        <strong style="color:#10b981; margin-left:6px;">${formatRupiahJS(rig.total_harga)}</strong>
      </div>
      <div>
        <span>Sisa Budget:</span>
        <strong style="color:#a855f7; margin-left:6px;">${formatRupiahJS(rig.sisa_budget)}</strong>
      </div>
    </div>

    <div class="rig-safety-notice" style="margin-top:14px; padding:12px 14px; background:rgba(234,179,8,0.08); border:1px solid rgba(234,179,8,0.25); border-left:4px solid #eab308; border-radius:8px; font-size:12.5px; color:#cbd5e1; line-height:1.5;">
      <strong style="color:#fde047; display:flex; align-items:center; gap:6px; margin-bottom:4px;">
        <i class="fa-solid fa-triangle-exclamation"></i> Catatan Penting Keamanan Perakitan:
      </strong>
      Untuk keamanan perakitan yang optimal, mohon konfirmasikan terlebih dahulu rekomendasi ini kepada teknisi atau staf toko kami sebelum proses perakitan dimulai agar saat dirakit tidak mengalami kendala fisik, karena rekomendasi sistem diberikan berdasarkan kecocokan data spesifikasi teknis, bukan berdasarkan pengalaman praktik langsung di lapangan.
    </div>
  `;
}

document.getElementById('rigBudgetSlider').addEventListener('input', (e) => {
  const val = parseInt(e.target.value);
  document.getElementById('sliderBudgetDisplay').innerText = formatRupiahJS(val);
});

document.getElementById('rigBudgetSlider').addEventListener('change', (e) => {
  loadRigCalculation(parseInt(e.target.value));
});

document.getElementById('btnConsultThisRig').addEventListener('click', () => {
  if (!currentRigData) return;
  closeModal('modalRigBuilder');
  setSpecialistMode('pc');
  const prompt = `Halo Mas Dimas, saya tertarik dengan simulasi racikan PC tier '${currentRigData.tier}' dengan total biaya ${formatRupiahJS(currentRigData.total_harga)}. Apakah racikan ini bisa langsung dirakitkan di toko dan siap pakai?`;
  sendQuickMessage(prompt);
});

// Setup Modal Search Listeners
function setupModalSearchListeners() {
  // Laptop Search
  document.getElementById('laptopSearchInput').addEventListener('input', debounce(() => loadLaptopsData(), 300));
  document.querySelectorAll('#laptopBrandPills .pill').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#laptopBrandPills .pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentLaptopBrand = btn.getAttribute('data-brand') || '';
      loadLaptopsData();
    });
  });

  // PC Search
  document.getElementById('pcSearchInput').addEventListener('input', debounce(() => loadPCData(), 300));
  document.querySelectorAll('#pcCategoryPills .pill').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#pcCategoryPills .pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentPCCategory = btn.getAttribute('data-cat') || '';
      loadPCData();
    });
  });
}

function consultProduct(type, name, price) {
  closeModal(type === 'laptop' ? 'modalLaptop' : 'modalPC');
  if (type === 'laptop') {
    setSpecialistMode('laptop');
    sendQuickMessage(`Halo Mas Aris, saya ingin menanyakan lebih detail mengenai laptop ${name} seharga ${formatRupiahJS(price)}. Apakah unit ini cocok untuk kebutuhan saya?`);
  } else {
    setSpecialistMode('pc');
    sendQuickMessage(`Halo Mas Dimas, apakah komponen ${name} seharga ${formatRupiahJS(price)} ini ready stok di gudang dan cocok untuk kebutuhan saya?`);
  }
}

function closeModal(modalId) {
  const m = document.getElementById(modalId);
  if (m) m.classList.remove('open');
}

function formatRupiahJS(angka) {
  return 'Rp ' + Number(angka).toLocaleString('id-ID');
}

function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}
