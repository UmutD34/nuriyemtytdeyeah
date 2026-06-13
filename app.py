import streamlit as st
import json
import random

# Sayfa Yapılandırması
st.set_page_config(
    page_title="TYT Çalışma Sistemi",
    page_icon="🏔️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS Tanımlamaları
st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">""", unsafe_allow_html=True)
st.markdown("""<style>
/* CSS içerikleri değişmedi, sadece modal ile ilgili kısımlar st.dialog'a uyarlandı */
html, body, .stApp { background: linear-gradient(135deg, #f4efe6 0%, #e8dcc8 100%) !important; color: #3a3a3a !important; font-family: 'Poppins', sans-serif !important; }
.block-container { padding: 1.2rem 0.9rem 4rem !important; max-width: 780px !important; }
.hud-wrap { background: linear-gradient(135deg, #d4c4b0 0%, #cbb89f 100%); border: 2px solid #a89878; border-radius: 16px; padding: 18px 22px; margin-bottom: 16px; box-shadow: 0 8px 16px rgba(0,0,0,0.08); }
.hud-title { font-family: 'Cormorant Garamond', serif; font-size: 28px; font-weight: 700; color: #5a4a3a; letter-spacing: 2px; }
.prog-fill { background: linear-gradient(90deg, #8b6f47 0%, #b8956a 100%); transition: width .5s ease; }
.hap-card { background: linear-gradient(135deg, #f9f4ed 0%, #f0e8dd 100%); border: 2px solid #a89878; border-radius: 16px; padding: 30px 26px; margin: 14px 0; min-height: 200px; display: flex; align-items: center; justify-content: center; }
.stButton > button { background: linear-gradient(135deg, #d4c4b0 0%, #cbb89f 100%) !important; color: #5a4a3a !important; border-radius: 10px !important; font-weight: 700 !important; }
</style>""", unsafe_allow_html=True)

# ── Başarım Sistemi ──────────────────────────────────────────────────────────
ACHIEVEMENTS = {
    1: ("🐦", "Anadolu Serçesi", "Başarımına başladın"),
    5: ("🦅", "Kartal Yolcu", "5 hap bilgiye ulaştın"),
    # ... (Diğer başarımlar aynı şekilde kalabilir)
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

# ── Session State Başlatma ──────────────────────────────────────────────────
if "hap_idx" not in st.session_state: st.session_state.hap_idx = 0
if "current_ders" not in st.session_state: st.session_state.current_ders = "Türkçe"
if "toplam_hap_goruldu" not in st.session_state: st.session_state.toplam_hap_goruldu = 0
if "onboarding_seen" not in st.session_state: st.session_state.onboarding_seen = False

# ── Modal (Dialog) Yapısı ───────────────────────────────────────────────────
@st.dialog("TYT Çalışma Sistemi")
def show_onboarding():
    st.markdown("""
    <div style='text-align: center;'>
        <div style='font-size: 48px; margin-bottom: 16px;'>🏔️</div>
        <p><strong>Mutedra Co.</strong> tarafından<br>
        <strong>Nuriye Hanımın</strong> şahsı için özel kodlanmıştır.<br><br>
        Anadolu'da bir yolculuğa başla.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 Yolculuğa Başla", use_container_width=True):
        st.session_state.onboarding_seen = True
        st.rerun()

if not st.session_state.onboarding_seen:
    show_onboarding()

# ── Ana UI ──────────────────────────────────────────────────────────────────
st.markdown('<div class="hud-wrap"><div class="hud-title">🏔️ TYT Çalışma Yolculuğu</div></div>', unsafe_allow_html=True)

# ... (Kalan UI kodların: Seçim kutuları, Progress Bar, Kartlar vs. aynen korunmalı)
# [Buraya mevcut UI kodlarını ekleyebilirsin]
