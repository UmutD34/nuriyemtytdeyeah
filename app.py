import streamlit as st
import json
import random

st.set_page_config(
    page_title="TYT HAP BİLGİ",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&family=Share+Tech+Mono&family=Noto+Sans:wght@400;600;700&display=swap" rel="stylesheet">""", unsafe_allow_html=True)

st.markdown("""<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, .stApp {
    background-color: #0b0d11 !important;
    color: #e8edf2 !important;
    font-family: 'Noto Sans', sans-serif !important;
}
.block-container { padding: 1.2rem 0.9rem 4rem !important; max-width: 780px !important; }

/* HUD */
.hud-wrap {
    background: linear-gradient(135deg, #13171f 0%, #0f1318 100%);
    border: 1px solid #252b36; border-radius: 14px;
    padding: 16px 20px; margin-bottom: 16px; position: relative; overflow: hidden;
}
.hud-wrap::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
    animation: siren .7s steps(1) infinite;
}
@keyframes siren {
    0%  { background: linear-gradient(90deg, #ff2020 0%, #ff2020 49%, #333 50%, #1a6fff 51%, #1a6fff 100%); }
    50% { background: linear-gradient(90deg, #1a6fff 0%, #1a6fff 49%, #333 50%, #ff2020 51%, #ff2020 100%); }
}
.hud-title { font-family: 'Rajdhani', sans-serif; font-size: 24px; font-weight: 700; color: #4da3ff; letter-spacing: 3px; text-transform: uppercase; }
.hud-sub { font-family: 'Share Tech Mono', monospace; font-size: 10px; color: #4a5568; letter-spacing: 2px; margin-top: 3px; }

/* Progress */
.prog-wrap { margin-bottom: 14px; }
.prog-meta { display: flex; justify-content: space-between; font-family: 'Share Tech Mono', monospace; font-size: 10px; color: #6b7280; margin-bottom: 5px; }
.prog-track { background: #0f1318; border-radius: 4px; height: 6px; border: 1px solid #252b36; overflow: hidden; }
.prog-fill { height: 100%; border-radius: 4px; background: linear-gradient(90deg, #1d5db5, #4da3ff); transition: width .5s ease; }

/* Kart */
.hap-card {
    background: linear-gradient(135deg, #13171f 0%, #0f1318 100%);
    border: 1px solid #252b36; border-left: 4px solid #4da3ff;
    border-radius: 14px; padding: 28px 24px; margin: 14px 0;
    min-height: 180px; display: flex; align-items: center; justify-content: center;
    animation: up .3s ease; position: relative;
}
@keyframes up { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.hap-text { font-size: 17px; font-weight: 600; line-height: 1.7; text-align: center; color: #f0f4f8; }

/* Dropdown */
.stSelectbox > div > div { background: #13171f !important; border-color: #252b36 !important; color: #e8edf2 !important; border-radius: 8px !important; font-size: 13px !important; }
.stSelectbox label, .stNumberInput label { color: #6b7280 !important; font-family: 'Share Tech Mono', monospace !important; font-size: 10px !important; letter-spacing: 2px !important; }

/* Butonlar */
.stButton > button {
    font-family: 'Rajdhani', sans-serif !important; font-weight: 700 !important;
    font-size: 13px !important; letter-spacing: 2px !important; text-transform: uppercase !important;
    border-radius: 8px !important; height: 48px !important; width: 100% !important;
    background: #13171f !important; border: 1px solid #252b36 !important; color: #c9d1d9 !important;
    transition: all .2s !important;
}
.stButton > button:hover:not(:disabled) {
    background: #1a1f2b !important; border-color: #4da3ff !important; color: #4da3ff !important;
    box-shadow: 0 0 12px rgba(77,163,255,.15) !important;
}
.stButton > button:disabled { opacity: .25 !important; }

/* Stat */
.stat-row { display: flex; gap: 8px; margin-bottom: 12px; }
.stat-box { flex: 1; background: #0f1318; border: 1px solid #252b36; border-radius: 10px; padding: 10px; text-align: center; }
.stat-val { font-family: 'Rajdhani', sans-serif; font-size: 22px; font-weight: 700; color: #4da3ff; }
.stat-lbl { font-family: 'Share Tech Mono', monospace; font-size: 9px; color: #6b7280; margin-top: 2px; }

details > summary { background: #13171f !important; border: 1px solid #252b36 !important; border-radius: 8px !important; color: #6b7280 !important; font-family: 'Share Tech Mono', monospace !important; font-size: 10px !important; letter-spacing: 2px !important; padding: 12px 16px !important; }
details[open] > summary { border-radius: 8px 8px 0 0 !important; }
details > div { background: #0f1318 !important; border: 1px solid #252b36 !important; border-top: none !important; border-radius: 0 0 8px 8px !important; padding: 16px !important; }

#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stDecoration"] { display: none !important; }
hr { border: none; border-top: 1px solid #1e2530 !important; margin: 14px 0 !important; }

@media (max-width: 480px) {
    .hud-title { font-size: 18px; letter-spacing: 1px; }
    .hap-text { font-size: 15px; }
    .stat-val { font-size: 18px; }
    .stButton > button { font-size: 11px !important; height: 44px !important; }
}
</style>""", unsafe_allow_html=True)


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
    st.session_state.current_ders = None

# ── UI ───────────────────────────────────────────────────────────────────────
st.markdown('<div class="hud-wrap"><div class="hud-title">📚 NURİYEM TYT Yİ EZİP GEÇİYOR SAKIZ DİYE CİGNİYOR. SİSTEM YÜKLENİYOR...</div><div class="hud-sub">SINAV HAZIRLIK SİSTEMİ</div></div>', unsafe_allow_html=True)

# Ders ve Konu Seçimi
d1, d2, d3 = st.columns([1.5, 1.8, 1.4])
with d1:
    secilen_ders = st.selectbox("DERS", tum_dersler)

with d2:
    if secilen_ders in mevcut_dersler:
        konular = list(mevcut_dersler[secilen_ders].keys())
        default_idx = 0
        if st.session_state.current_konu in konular:
            default_idx = konular.index(st.session_state.current_konu)
        secilen_konu = st.selectbox("KONU", konular, index=default_idx)
    else:
        secilen_konu = st.selectbox("KONU", ["⏳ Yakında Eklenecek"])
        secilen_ders_var = False
    
    if secilen_ders in mevcut_dersler:
        st.session_state.current_ders = secilen_ders
        st.session_state.current_konu = secilen_konu

with d3:
    st.markdown("<div style='padding-top: 8px; font-family:Share Tech Mono,monospace; font-size:11px; color:#4a5568; letter-spacing:2px; text-align:right;'>KONU SEÇ</div>", unsafe_allow_html=True)

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
    <div class="stat-box"><div class="stat-val">{secilen_ders[0]}</div><div class="stat-lbl">Ders</div></div>
</div>""", unsafe_allow_html=True)
    
    # Hap Kartı
    hap_text = hap_bilgileri[idx].replace("<", "&lt;").replace(">", "&gt;")
    st.markdown(f'<div class="hap-card"><div class="hap-text">{hap_text}</div></div>', unsafe_allow_html=True)
    
    # Butonlar
    b1, b2, b3, b4 = st.columns([1, 1.2, 1, 1])
    
    with b1:
        if st.button("◀ ÖNC.", disabled=(idx == 0), key="onceki"):
            st.session_state.hap_idx -= 1
            st.rerun()
    
    with b2:
        if st.button("🔀 RASTGELE", key="rastgele"):
            st.session_state.hap_idx = random.randint(0, toplam - 1)
            st.rerun()
    
    with b3:
        if st.button("SON. ▶", disabled=(idx == toplam - 1), key="sonraki"):
            st.session_state.hap_idx += 1
            st.rerun()
    
    with b4:
        if st.button("↺ SIFIRLA", key="sifirla"):
            st.session_state.hap_idx = 0
            st.rerun()

else:
    if secilen_ders not in mevcut_dersler:
        st.markdown(f'<div class="hap-card"><div class="hap-text" style="color:#f0883e;">⏳ <b>{secilen_ders}</b> dersi için dersler henüz hazırlanmadı.</div></div>', unsafe_allow_html=True)

# ── Bilgiler ─────────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)

with st.expander("ℹ️  KULLANICIA KILAVUZU"):
    st.markdown("""
**TYT HAP BİLGİ** sistemi başarıyla kullanmak için:

1️⃣ **Ders Seçin:** Türkçe, Matematik, Fen veya Sosyal
2️⃣ **Konu Seçin:** Seçtiğiniz dersle ilgili konuları listeden seçin
3️⃣ **Hap Bilgileri:** Kartlarda yer alan özetlenmiş bilgileri okuyun
4️⃣ **Navigasyon:** ◀️ Önceki / 🔀 Rastgele / ➡️ Sonraki butonlarıyla geçiş yapın
5️⃣ **Tekrar:** Aynı konuyu birden çok kez görmek için ↺ Sıfırla kullanın

📊 **Şu An Yüklü Dersler:**
""")
    
    for ders, konular in mevcut_dersler.items():
        topak_hap = sum(len(v) for v in konular.values())
        st.markdown(f"- **{ders}**: {len(konular)} konu, {topak_hap} hap bilgi")

c1, c2 = st.columns([2, 1])
with c1:
    st.markdown(f"<div style='font-family:Share Tech Mono,monospace;font-size:9px;color:#2a3040;letter-spacing:1px;padding:10px 0;'>TYT HAP BİLGİ v1.0 · SINAV HAZIRLIK ARACĞI</div>", unsafe_allow_html=True)
with c2:
    if st.button("🔄 HEPSINI YENILE", key="yenile"):
        st.cache_data.clear()
        st.rerun()
