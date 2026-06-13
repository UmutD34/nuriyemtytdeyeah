import streamlit as st
import json
import random

st.set_page_config(
    page_title="TYT Çalışma Sistemi",
    page_icon="🏔️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">""", unsafe_allow_html=True)

st.markdown("""<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, .stApp {
    background: linear-gradient(135deg, #f4efe6 0%, #e8dcc8 100%) !important;
    color: #3a3a3a !important;
    font-family: 'Poppins', sans-serif !important;
}
.block-container { padding: 1.2rem 0.9rem 4rem !important; max-width: 780px !important; }

/* HUD - Otantik Doğa Teması */
.hud-wrap {
    background: linear-gradient(135deg, #d4c4b0 0%, #cbb89f 100%);
    border: 2px solid #a89878; border-radius: 16px;
    padding: 18px 22px; margin-bottom: 16px; position: relative; overflow: hidden;
    box-shadow: 0 8px 16px rgba(0,0,0,0.08);
}
.hud-wrap::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, #8b6f47 0%, #d4a574 50%, #8b6f47 100%);
}
.hud-title { font-family: 'Cormorant Garamond', serif; font-size: 28px; font-weight: 700; color: #5a4a3a; letter-spacing: 2px; }
.hud-sub { font-family: 'Poppins', sans-serif; font-size: 10px; color: #7a6a5a; letter-spacing: 1px; margin-top: 2px; }

/* Progress */
.prog-wrap { margin-bottom: 14px; }
.prog-meta { display: flex; justify-content: space-between; font-family: 'Poppins', sans-serif; font-size: 10px; color: #6b5a4a; margin-bottom: 6px; font-weight: 600; }
.prog-track { background: #d4c4b0; border-radius: 8px; height: 8px; border: 1px solid #a89878; overflow: hidden; }
.prog-fill { height: 100%; border-radius: 8px; background: linear-gradient(90deg, #8b6f47 0%, #b8956a 100%); transition: width .5s ease; }

/* Başarım Banner */
.achievement-banner {
    background: linear-gradient(135deg, #e8d5b7 0%, #d9c9b3 100%);
    border: 2px solid #8b6f47; border-radius: 12px; padding: 14px 16px;
    margin: 12px 0; text-align: center; animation: slideIn .5s ease;
}
@keyframes slideIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
.achievement-emoji { font-size: 28px; margin-bottom: 6px; }
.achievement-text { font-family: 'Cormorant Garamond', serif; font-size: 16px; font-weight: 700; color: #5a4a3a; letter-spacing: 1px; }
.achievement-desc { font-size: 12px; color: #7a6a5a; margin-top: 4px; }

/* Kart */
.hap-card {
    background: linear-gradient(135deg, #f9f4ed 0%, #f0e8dd 100%);
    border: 2px solid #a89878; border-radius: 16px; padding: 30px 26px;
    margin: 14px 0; min-height: 200px; display: flex; align-items: center; justify-content: center;
    animation: up .4s ease; position: relative; box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}
.hap-card::before {
    content: '🌿'; position: absolute; top: -12px; right: 20px; font-size: 32px; opacity: 0.3;
}
@keyframes up { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.hap-text { font-family: 'Cormorant Garamond', serif; font-size: 18px; font-weight: 600; line-height: 1.8; text-align: center; color: #3a3a3a; letter-spacing: .5px; }

/* Stat */
.stat-row { display: flex; gap: 8px; margin-bottom: 12px; }
.stat-box { flex: 1; background: linear-gradient(135deg, #e8dcc8 0%, #dfd2bb 100%); border: 1px solid #a89878; border-radius: 12px; padding: 12px; text-align: center; }
.stat-val { font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 700; color: #8b6f47; }
.stat-lbl { font-family: 'Poppins', sans-serif; font-size: 9px; color: #7a6a5a; margin-top: 2px; font-weight: 600; }

/* Dropdown */
.stSelectbox > div > div { background: #f0e8dd !important; border: 1px solid #a89878 !important; color: #3a3a3a !important; border-radius: 10px !important; font-size: 13px !important; }
.stSelectbox label { color: #5a4a3a !important; font-family: 'Cormorant Garamond', serif !important; font-size: 12px !important; font-weight: 600 !important; letter-spacing: 1px !important; }

/* Butonlar */
.stButton > button {
    font-family: 'Poppins', sans-serif !important; font-weight: 700 !important;
    font-size: 12px !important; letter-spacing: 1px !important; text-transform: uppercase !important;
    border-radius: 10px !important; height: 48px !important; width: 100% !important;
    background: linear-gradient(135deg, #d4c4b0 0%, #cbb89f 100%) !important;
    border: 1.5px solid #a89878 !important; color: #5a4a3a !important;
    transition: all .2s !important; font-weight: 700 !important;
}
.stButton > button:hover:not(:disabled) {
    background: linear-gradient(135deg, #b8956a 0%, #a8854a 100%) !important;
    border-color: #5a4a3a !important; color: #f9f4ed !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
}
.stButton > button:disabled { opacity: .3 !important; }

/* Expander */
details > summary { background: #e8dcc8 !important; border: 1px solid #a89878 !important; border-radius: 10px !important; color: #5a4a3a !important; font-family: 'Cormorant Garamond', serif !important; font-size: 13px !important; font-weight: 700 !important; padding: 12px 16px !important; }
details[open] > summary { border-radius: 10px 10px 0 0 !important; }
details > div { background: #f0e8dd !important; border: 1px solid #a89878 !important; border-top: none !important; border-radius: 0 0 10px 10px !important; padding: 16px !important; }

/* Modal/Popup */
.modal-overlay {
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center;
    z-index: 9999;
}
.modal-box {
    background: linear-gradient(135deg, #d4c4b0 0%, #cbb89f 100%);
    border: 3px solid #8b6f47; border-radius: 18px; padding: 40px;
    max-width: 500px; width: 90%; text-align: center;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
}
.modal-title { font-family: 'Cormorant Garamond', serif; font-size: 26px; font-weight: 700; color: #5a4a3a; margin-bottom: 12px; letter-spacing: 1px; }
.modal-text { font-family: 'Poppins', sans-serif; font-size: 13px; color: #5a4a3a; line-height: 1.6; margin-bottom: 24px; }
.modal-emoji { font-size: 48px; margin-bottom: 16px; }
.modal-btn {
    background: linear-gradient(135deg, #8b6f47 0%, #6a5a3a 100%);
    color: #f9f4ed; border: none; border-radius: 10px; padding: 12px 32px;
    font-family: 'Poppins', sans-serif; font-weight: 700; cursor: pointer;
    transition: all .2s; font-size: 13px; letter-spacing: 1px;
}
.modal-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.2); }

#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stDecoration"] { display: none !important; }
hr { border: none; border-top: 1px solid #a89878 !important; margin: 14px 0 !important; }

@media (max-width: 480px) {
    .hud-title { font-size: 20px; letter-spacing: .5px; }
    .hap-text { font-size: 15px; }
    .stat-val { font-size: 18px; }
    .stButton > button { font-size: 11px !important; height: 44px !important; }
}
</style>""", unsafe_allow_html=True)

# Başarım Sistemi Tanımlaması
ACHIEVEMENTS = {
    1:   ("🐦", "Anadolu Serçesi", "Başarımına başladın"),
    5:   ("🦅", "Kartal Yolcu", "5 hap bilgiye ulaştın"),
    10:  ("🏔️", "Iğdır Dağı", "10 hap bilgiye vardın"),
    15:  ("🌲", "Sarıçam Ağacı", "15 hap bilgiyle tanıştın"),
    20:  ("⛰️", "Hazar Dağı Etekleri", "20 hap bilgiyi tamamladın"),
    25:  ("🌳", "Meşe Ormanında Dinlendin", "25 hap bilgiye vardin"),
    30:  ("🏜️", "Kapadokya Kaya Sarayları", "30 hap bilgiye ulaştın"),
    35:  ("🌸", "Aksaray Çandırı Çiçeği", "35 hap bilgiyi gördün"),
    40:  ("🪨", "Niğde Dağları Kampı", "40 hap bilgiye vardın"),
    45:  ("🦜", "Kayseri Karçıkakı", "45 hap bilgiyi selamladın"),
    50:  ("🌾", "Konya Ovası", "50 hap bilgiye ulaştın"),
    55:  ("🏞️", "Sivas Yeşilırmak Kanyonu", "55 hap bilgiyi geçtin"),
    60:  ("🌿", "Çorum Ballı Bahçeleri", "60 hap bilgiyi kurtardın"),
    65:  ("🍃", "Ankara Eğrelti Ormanı", "65 hap bilgiyi gezdin"),
    70:  ("🌰", "Kastamonu Kestaneleri", "70 hap bilgiye vardın"),
    75:  ("🏔️", "Sinop Kara Düzü", "75 hap bilgiyi aştın"),
    80:  ("🍵", "Rize Çay Bahçeleri", "80 hap bilgiye ulaştın"),
    85:  ("🌅", "Ordu Platolarında Gün Batımı", "85 hap bilgiyi seyretti"),
    90:  ("🌰", "Giresun Kestane Ormanı", "90 hap bilgide sakinlik buldun"),
    95:  ("🦅", "Rize Yüksek Platolarında Kartal", "95 hap bilgiyi gördün"),
    100: ("🏔️", "Anadolu Zirvesine Ulaştın", "YOLCULUK TAMAMLANDI!"),
}

# ── Veri Yükleme ────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    try:
        with open("dersler.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"dersler": {"Türkçe": {"Örnek Konu": ["Henüz veri yüklenmedi."]}}}

data = load_data()
mevcut_dersler = data.get("dersler", {})
tum_dersler = ["Türkçe", "Matematik", "Fen", "Sosyal"]

# ── Session State ────────────────────────────────────────────────────────────
if "hap_idx" not in st.session_state:
    st.session_state.hap_idx = 0
if "current_konu" not in st.session_state:
    st.session_state.current_konu = None
if "current_ders" not in st.session_state:
    st.session_state.current_ders = "Türkçe"
if "toplam_hap_goruldu" not in st.session_state:
    st.session_state.toplam_hap_goruldu = 0
if "onboarding_seen" not in st.session_state:
    st.session_state.onboarding_seen = False

# ── Pop-up (Onboarding) ──────────────────────────────────────────────────────
if not st.session_state.onboarding_seen:
    st.markdown("""
    <div class="modal-overlay">
        <div class="modal-box">
            <div class="modal-emoji">🏔️</div>
            <div class="modal-title">TYT Çalışma Sistemi</div>
            <div class="modal-text">
                <strong>Mutedra Co.</strong> tarafından<br>
                <strong>Nuriye Hanımın</strong> şahsı için<br>
                özel kodlanmıştır.
                <br><br>
                Anadolu\'da bir yolculuğa başla,<br>
                dağları, ormanları ve kuşları keşfet.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Yolculuğa Başla", key="start_journey", use_container_width=True):
        st.session_state.onboarding_seen = True
        st.rerun()
    
    st.stop()

# ── UI ───────────────────────────────────────────────────────────────────────
st.markdown('<div class="hud-wrap"><div class="hud-title">🏔️ TYT Çalışma Yolculuğu</div><div class="hud-sub">Anadolu\'da Bir Öğrenme Serüveni</div></div>', unsafe_allow_html=True)

# Ders ve Konu Seçimi
d1, d2, d3 = st.columns([1.5, 1.8, 1.4])
with d1:
    secilen_ders = st.selectbox("DERS", tum_dersler, index=tum_dersler.index(st.session_state.current_ders))

with d2:
    if secilen_ders in mevcut_dersler:
        konular = list(mevcut_dersler[secilen_ders].keys())
        default_idx = 0
        if st.session_state.current_konu in konular:
            default_idx = konular.index(st.session_state.current_konu)
        secilen_konu = st.selectbox("KONU", konular, index=default_idx, key="konu_select")
    else:
        secilen_konu = st.selectbox("KONU", ["⏳ Yakında Eklenecek"], key="konu_select_waiting")
    
    if secilen_ders in mevcut_dersler:
        st.session_state.current_ders = secilen_ders
        st.session_state.current_konu = secilen_konu

with d3:
    st.markdown(f"<div style='padding-top: 10px; font-family:Poppins,sans-serif; font-size:11px; color:#7a6a5a; letter-spacing:1px; text-align:right; font-weight:600;'>{secilen_ders}</div>", unsafe_allow_html=True)

# Hap Bilgiler Ekranı
if secilen_ders in mevcut_dersler and secilen_konu != "⏳ Yakında Eklenecek":
    hap_bilgileri = mevcut_dersler[secilen_ders][secilen_konu]
    
    if st.session_state.hap_idx >= len(hap_bilgileri):
        st.session_state.hap_idx = 0
    
    idx = st.session_state.hap_idx
    toplam = len(hap_bilgileri)
    
    # İlerleme Çubuğu
    pct = round((idx + 1) / toplam * 100, 1)
    st.markdown(f"""
<div class="prog-wrap">
    <div class="prog-meta"><span>HAP BİLGİ İLERLEMESİ</span><span>{idx+1} / {toplam} · %{pct}</span></div>
    <div class="prog-track"><div class="prog-fill" style="width:{pct}%"></div></div>
</div>""", unsafe_allow_html=True)
    
    # Stat Satırı
    st.markdown(f"""
<div class="stat-row">
    <div class="stat-box"><div class="stat-val">{idx+1}</div><div class="stat-lbl">Şu an</div></div>
    <div class="stat-box"><div class="stat-val">{toplam}</div><div class="stat-lbl">Toplam</div></div>
    <div class="stat-box"><div class="stat-val">{st.session_state.toplam_hap_goruldu}</div><div class="stat-lbl">Toplam Görülen</div></div>
</div>""", unsafe_allow_html=True)
    
    # Hap Kartı
    hap_text = hap_bilgileri[idx].replace("<", "&lt;").replace(">", "&gt;")
    st.markdown(f'<div class="hap-card"><div class="hap-text">{hap_text}</div></div>', unsafe_allow_html=True)
    
    # Başarım Kontrol
    if st.session_state.toplam_hap_goruldu in ACHIEVEMENTS:
        emoji, başarım, açıklama = ACHIEVEMENTS[st.session_state.toplam_hap_goruldu]
        st.markdown(f"""
<div class="achievement-banner">
    <div class="achievement-emoji">{emoji}</div>
    <div class="achievement-text">{başarım}</div>
    <div class="achievement-desc">{açıklama}</div>
</div>""", unsafe_allow_html=True)
    
    # Butonlar
    b1, b2, b3, b4 = st.columns([1, 1.2, 1, 1])
    
    with b1:
        if st.button("◀ ÖNC.", disabled=(idx == 0), key="onceki"):
            st.session_state.hap_idx -= 1
            st.rerun()
    
    with b2:
        if st.button("🔀 RASTGELE", key="rastgele"):
            st.session_state.hap_idx = random.randint(0, toplam - 1)
            st.session_state.toplam_hap_goruldu += 1
            st.rerun()
    
    with b3:
        if st.button("SON. ▶", disabled=(idx == toplam - 1), key="sonraki"):
            st.session_state.hap_idx += 1
            st.session_state.toplam_hap_goruldu += 1
            st.rerun()
    
    with b4:
        if st.button("↺ SIFIRLA", key="sifirla"):
            st.session_state.hap_idx = 0
            st.rerun()

else:
    if secilen_ders not in mevcut_dersler:
        st.markdown(f'<div class="hap-card"><div class="hap-text" style="color:#8b6f47;">⏳ <b>{secilen_ders}</b> dersi için dersler henüz hazırlanmadı.</div></div>', unsafe_allow_html=True)

# ── Bilgiler ─────────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)

with st.expander("🏔️  ANADOLU'DA YOLCULUĞU ANLA"):
    st.markdown("""
**Yolculuğun Haritası:**

Anadolu\'da bir öğrenme serüvenine başladın. Her hap bilgiyi okudukça, dağları tırmanıyor, ormanları geçiyor ve kuşları görüyorsun.

🎯 **Başarımlarını Takip Et:**
""")
    
    # Başarımları göster
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - 🐦 1 hap: Anadolu Serçesi
        - 🦅 5 hap: Kartal Yolcu
        - 🏔️ 10 hap: Iğdır Dağı
        - 🌲 15 hap: Sarıçam Ağacı
        - ⛰️ 20 hap: Hazar Dağı
        - 🌳 25 hap: Meşe Ormanı
        """)
    with col2:
        st.markdown("""
        - 🏜️ 30 hap: Kapadokya
        - 🌸 35 hap: Çandırı Çiçeği
        - 🏔️ 40 hap: Niğde Dağları
        - 🦜 45 hap: Karçıkakı
        - 🌾 50 hap: Konya Ovası
        - ⋯ 100 hap: Anadolu Zirvesi
        """)
    
    st.markdown(f"""
📊 **Şu An Yüklü Dersler:**
""")
    
    for ders, konular in mevcut_dersler.items():
        topak_hap = sum(len(v) for v in konular.values())
        st.markdown(f"🎓 **{ders}**: {len(konular)} konu, {topak_hap} hap bilgi")

c1, c2 = st.columns([2, 1])
with c1:
    st.markdown(f"<div style='font-family:Poppins,sans-serif;font-size:9px;color:#7a6a5a;letter-spacing:1px;padding:10px 0;'>TYT ÇALIŞMA SİSTEMİ · ANADOLU YOLCULUĞU · MUTEDRA CO.</div>", unsafe_allow_html=True)
with c2:
    if st.button("🔄 YENILE", key="yenile"):
        st.cache_data.clear()
        st.rerun()
