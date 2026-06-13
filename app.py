import streamlit as st
import json

st.set_page_config(
    page_title="NURİYEM TYT Yİ EZİP GEÇİYOR - SİSTEM AKTİVE OLUYOR...",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, .stApp {
    background-color: #0b0d11 !important;
    color: #e8edf2 !important;
    font-family: sans-serif !important;
}
.block-container { padding: 1.5rem 1rem 4rem !important; max-width: 720px !important; }

/* Üst Başlık (HUD) */
.hud-wrap {
    background:#13171f; border:1px solid #252b36; border-radius:14px;
    padding:16px 20px; margin-bottom:18px; text-align: center;
}
.hud-title { font-size:22px; font-weight:700; color:#4da3ff; letter-spacing:2px; }

/* Bilgi Kartı */
.card {
    background:#13171f; border:1px solid #252b36; border-left:4px solid #4da3ff;
    border-radius:14px; padding:30px 25px; margin-top:15px; margin-bottom:20px;
    min-height: 220px; display:flex; align-items:center; justify-content:center;
    animation: up 0.3s ease;
}
@keyframes up { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
.card-text { font-size:18px; font-weight:600; line-height:1.6; text-align:center; color:#f0f4f8; }

/* Arayüz Elemanları */
.stSelectbox > div > div { background:#13171f !important; border-color:#252b36 !important; color:#e8edf2 !important; border-radius:8px !important; }
.stSelectbox label { color:#6b7280 !important; font-size:12px !important; letter-spacing:1px !important; }

.stButton > button {
    font-weight:700 !important; font-size:14px !important; letter-spacing:1px !important;
    border-radius:8px !important; height:46px !important; width:100% !important;
    background:#13171f !important; border:1px solid #252b36 !important; color:#adb5bd !important;
    transition: all 0.2s !important;
}
.stButton > button:hover:not(:disabled) { border-color:#4da3ff !important; color:#4da3ff !important; }
.stButton > button:disabled { opacity: 0.4 !important; border-color: #252b36 !important; }

#MainMenu, footer, header { visibility:hidden !important; }
</style>""", unsafe_allow_html=True)

# ── Veri ─────────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    try:
        with open("dersler.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"dersler": {"Hata": {"Dosya": ["dersler.json dosyası bulunamadı."]}}}

data = load_data()
mevcut_dersler_dict = data.get("dersler", {})
mevcut_dersler_listesi = list(mevcut_dersler_dict.keys())
tum_dersler = ["Türkçe", "Matematik", "Fen", "Sosyal"]

# ── Arayüz ───────────────────────────────────────────────────────────────────
st.markdown('<div class="hud-wrap"><div class="hud-title">📚 NURİYEM TYT Yİ EZİP GEÇİYOR - SİSTEM AKTİVE OLUYOR</div></div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    secilen_ders = st.selectbox("DERS SEÇİMİ", tum_dersler)
with c2:
    if secilen_ders in mevcut_dersler_listesi:
        konular = list(mevcut_dersler_dict[secilen_ders].keys())
        secilen_konu = st.selectbox("KONU SEÇİMİ", konular)
    else:
        secilen_konu = st.selectbox("KONU SEÇİMİ", ["Yakında Eklenecek"])

# ── Session State Kontrolü ───────────────────────────────────────────────────
if "idx" not in st.session_state:
    st.session_state.idx = 0
if "current_konu" not in st.session_state or st.session_state.current_konu != secilen_konu:
    st.session_state.idx = 0
    st.session_state.current_konu = secilen_konu

# ── Kart ve Navigasyon ───────────────────────────────────────────────────────
if secilen_ders in mevcut_dersler_listesi and secilen_konu != "Yakında Eklenecek":
    hap_bilgiler = mevcut_dersler_dict[secilen_ders][secilen_konu]
    toplam = len(hap_bilgiler)
    idx = st.session_state.idx

    st.markdown(f"<div style='text-align:right; font-size:12px; color:#6b7280; font-weight:bold;'>İLERLEME: {idx+1} / {toplam}</div>", unsafe_allow_html=True)
    
    bilgi_metni = hap_bilgiler[idx].replace("<", "&lt;").replace(">", "&gt;")
    st.markdown(f'<div class="card"><div class="card-text">{bilgi_metni}</div></div>', unsafe_allow_html=True)

    b1, b2, b3 = st.columns([1, 1, 1])
    with b1:
        if st.button("◀ ÖNCEKİ", disabled=(idx == 0)):
            st.session_state.idx -= 1
            st.rerun()
    with b2:
        if st.button("🔀 RASTGELE"):
            import random
            st.session_state.idx = random.randint(0, toplam - 1)
            st.rerun()
    with b3:
        if st.button("SONRAKİ ▶", disabled=(idx == toplam - 1)):
            st.session_state.idx += 1
            st.rerun()
else:
    st.markdown('<div class="card"><div class="card-text" style="color:#f0883e;">Bu derse ait modül henüz sisteme yüklenmedi veya geliştirme aşamasında.</div></div>', unsafe_allow_html=True)
