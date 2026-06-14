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
html, body, .stApp { background: linear-gradient(135deg, #f4efe6 0%, #e8dcc8 100%) !important; color: #3a3a3a !important; font-family: 'Poppins', sans-serif !important; }
.block-container { padding: 1.2rem 0.9rem 4rem !important; max-width: 780px !important; }
.hud-wrap { background: linear-gradient(135deg, #d4c4b0 0%, #cbb89f 100%); border: 2px solid #a89878; border-radius: 16px; padding: 18px 22px; margin-bottom: 16px; position: relative; overflow: hidden; box-shadow: 0 8px 16px rgba(0,0,0,0.08); }
.hud-wrap::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #8b6f47 0%, #d4a574 50%, #8b6f47 100%); }
.hud-title { font-family: 'Cormorant Garamond', serif; font-size: 28px; font-weight: 700; color: #5a4a3a; letter-spacing: 2px; }
.hud-sub { font-family: 'Poppins', sans-serif; font-size: 10px; color: #7a6a5a; letter-spacing: 1px; margin-top: 2px; }
.prog-wrap { margin-bottom: 14px; }
.prog-meta { display: flex; justify-content: space-between; font-family: 'Poppins', sans-serif; font-size: 10px; color: #6b5a4a; margin-bottom: 6px; font-weight: 600; }
.prog-track { background: #d4c4b0; border-radius: 8px; height: 8px; border: 1px solid #a89878; overflow: hidden; }
.prog-fill { height: 100%; border-radius: 8px; background: linear-gradient(90deg, #8b6f47 0%, #b8956a 100%); transition: width .5s ease; }
.achievement-banner { background: linear-gradient(135deg, #e8d5b7 0%, #d9c9b3 100%); border: 2px solid #8b6f47; border-radius: 12px; padding: 14px 16px; margin: 12px 0; text-align: center; animation: slideIn .5s ease; }
@keyframes slideIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
.achievement-emoji { font-size: 28px; margin-bottom: 6px; }
.achievement-text { font-family: 'Cormorant Garamond', serif; font-size: 16px; font-weight: 700; color: #5a4a3a; letter-spacing: 1px; }
.achievement-desc { font-size: 12px; color: #7a6a5a; margin-top: 4px; }
.hap-card { background: linear-gradient(135deg, #f9f4ed 0%, #f0e8dd 100%); border: 2px solid #a89878; border-radius: 16px; padding: 30px 26px; margin: 14px 0; min-height: 200px; display: flex; align-items: center; justify-content: center; animation: up .4s ease; position: relative; box-shadow: 0 4px 12px rgba(0,0,0,0.06); }
.hap-card::before { content: '🌿'; position: absolute; top: -12px; right: 20px; font-size: 32px; opacity: 0.3; }
@keyframes up { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.hap-text { font-family: 'Cormorant Garamond', serif; font-size: 18px; font-weight: 600; line-height: 1.8; text-align: center; color: #3a3a3a; letter-spacing: .5px; }
.stat-row { display: flex; gap: 8px; margin-bottom: 12px; }
.stat-box { flex: 1; background: linear-gradient(135deg, #e8dcc8 0%, #dfd2bb 100%); border: 1px solid #a89878; border-radius: 12px; padding: 12px; text-align: center; }
.stat-val { font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 700; color: #8b6f47; }
.stat-lbl { font-family: 'Poppins', sans-serif; font-size: 9px; color: #7a6a5a; margin-top: 2px; font-weight: 600; }
.stSelectbox > div > div { background: #f0e8dd !important; border: 1px solid #a89878 !important; color: #3a3a3a !important; border-radius: 10px !important; font-size: 13px !important; }
.stSelectbox label { color: #5a4a3a !important; font-family: 'Cormorant Garamond', serif !important; font-size: 12px !important; font-weight: 600 !important; letter-spacing: 1px !important; }
.stButton > button { font-family: 'Poppins', sans-serif !important; font-weight: 700 !important; font-size: 12px !important; letter-spacing: 1px !important; text-transform: uppercase !important; border-radius: 10px !important; height: 48px !important; width: 100% !important; background: linear-gradient(135deg, #d4c4b0 0%, #cbb89f 100%) !important; border: 1.5px solid #a89878 !important; color: #5a4a3a !important; transition: all .2s !important; }
.stButton > button:hover:not(:disabled) { background: linear-gradient(135deg, #b8956a 0%, #a8854a 100%) !important; border-color: #5a4a3a !important; color: #f9f4ed !important; box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important; }
.stButton > button:disabled { opacity: .3 !important; }
details > summary { background: #e8dcc8 !important; border: 1px solid #a89878 !important; border-radius: 10px !important; color: #5a4a3a !important; font-family: 'Cormorant Garamond', serif !important; font-size: 13px !important; font-weight: 700 !important; padding: 12px 16px !important; }
details[open] > summary { border-radius: 10px 10px 0 0 !important; }
details > div { background: #f0e8dd !important; border: 1px solid #a89878 !important; border-top: none !important; border-radius: 0 0 10px 10px !important; padding: 16px !important; }
#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stDecoration"] { display: none !important; }
hr { border: none; border-top: 1px solid #a89878 !important; margin: 14px 0 !important; }
@media (max-width: 480px) { .hud-title { font-size: 20px; letter-spacing: .5px; } .hap-text { font-size: 15px; } .stat-val { font-size: 18px; } .stButton > button { font-size: 11px !important; height: 44px !important; } }
</style>""", unsafe_allow_html=True)

ACHIEVEMENTS = {
    1: ("🐦", "Anadolu Serçesini buldun", "Başarımına başladın"),
    5: ("🦅", "Anadolu Kartalı seni selamlıyor", "5 hap bilgiye ulaştın"),
    10: ("🏔️", "Iğdır Dağına hoş geldin", "10 hap bilgiye vardın"),
    15: ("🌲", "Sarıçam Ağacına su döktün", "15 hap bilgiyle tanıştın"),
    20: ("⛰️", "Hazar Dağı Eteklerine geldin", "20 hap bilgiyi tamamladın"),
    25: ("🌳", "Meşe Ormanında Dinlendin", "25 hap bilgiye vardın"),
    30: ("🏜️", "Kapadokya Kaya Saraylarında gezdin", "30 hap bilgiye ulaştın"),
    35: ("🌸", "Aksaray Çandırı Çiçeği kokladın", "35 hap bilgiyi gördün"),
    40: ("🪨", "Niğde Dağları Kampına gittin", "40 hap bilgiye vardın"),
    45: ("🦜", "Kayseri Karçıkakısını selamladın", "45 hap bilgiyi gördün"),
    50: ("🌾", "Konya Ovasında yürüdün", "50 hap bilgiye ulaştın"),
    55: ("🏞️", "Sivas Yeşilırmak Kanyonuna geçtin", "55 hap bilgiyi geçtin"),
    60: ("🌿", "Çorum Ballı Bahçelerine gittin", "60 hap bilgiyi kurtardın"),
    65: ("🍃", "Ankara Eğrelti Ormanına daldın", "65 hap bilgiyi gezdin"),
    70: ("🌰", "Kastamonu Kestaneleri yedin", "70 hap bilgiye vardın"),
    75: ("🏔️", "Sinop Kara Düzüye gittin", "75 hap bilgiyi aştın"),
    80: ("🍵", "Rize Çay Bahçelerinde çay topladın", "80 hap bilgiye ulaştın"),
    85: ("🌅", "Ordu Platolarında Gün Batımını izledin", "85 hap bilgiyi seyretti"),
    90: ("🌰", "Giresun Kestane Ormanına gittin", "90 hap bilgide sakinlik buldun"),
    95: ("🦅", "Rize Yüksek Platolarında Kartal izledin", "95 hap bilgiyi gördün"),
    100: ("🏔️", "Erciyes Dağı Zirvesine ulaştın", "YOLCULUK TAMAMLANDI!"),
    110: ("🌲", "Munzur Ormanlarında Yaban Keçisini gördün", "110 hap bilgiye vardın"),
    120: ("🦅", "Peregrin Şahını izledin", "120 hap bilgiye ulaştın"),
    130: ("🏔️", "Aladağ Kütlelerine geçtin", "130 hap bilgiyi gezdin"),
    140: ("🌿", "Toros Sediri yakınına vardin", "140 hap bilgiye vardın"),
    150: ("🌸", "Lilium Anadolu Dağ Zambağını buldum", "150 hap bilgiyi gördün"),
    160: ("🦜", "Sıvri Kuşunu selamladın", "160 hap bilgiye ulaştın"),
    170: ("🏞️", "Pütürge Kanyon yolculuğunun yaptın", "170 hap bilgiyi geçtin"),
    180: ("⛰️", "Gavur Dağlarına yükseldin", "180 hap bilgiye vardın"),
    190: ("🌾", "Kayseri Merkez Ovasından geçtin", "190 hap bilgiyi tamamladın"),
    200: ("🎯", "Anadolu'nın Ortasında 200 Hap!", "200 hap bilgiye ulaştın"),
    220: ("🦅", "Altın Kartal Korunma Alanında geçdin", "220 hap bilgiyi gezdin"),
    240: ("🏔️", "Nesiş Dağlarını tırmandın", "240 hap bilgiye vardın"),
    260: ("🌿", "Sürmene Çamlığında yürüdün", "260 hap bilgiyi gördün"),
    280: ("🌲", "Turhal Ormansında sesini işittim", "280 hap bilgiye ulaştın"),
    300: ("🎯", "Üçüncü Yüzlük Başarım! Tebrikler!", "300 hap bilgiyi tamamladın"),
    320: ("🦜", "Ceylan Dağlarında ceylan gözledin", "320 hap bilgiye vardın"),
    340: ("🌸", "Şarkışla Antik Şehri gezdin", "340 hap bilgiyi gördün"),
    360: ("⛰️", "Venasa Dağlarında çıkış yaptın", "360 hap bilgiye ulaştın"),
    380: ("🏞️", "Pontus Ormanlarının Derinliklerine indim", "380 hap bilgiyi geçtin"),
    400: ("🎯", "Dördüncü Yüzlük Başarım Sağlıdır!", "400 hap bilgiyi tamamladın"),
    420: ("🦅", "Doğmuş Şahini izledin", "420 hap bilgiye vardın"),
    440: ("🌿", "Yaban Mersini topladın", "440 hap bilgiyi gördün"),
    460: ("🏔️", "Artanış Dağlarında kamp yaptın", "460 hap bilgiye ulaştın"),
    480: ("🌲", "Göknar Korunma Alanında yürüdün", "480 hap bilgiyi geçtin"),
    500: ("👑", "ANADOLU ZIRVESI! 500 HAP BİLGİYE ULAŞTINIZ!", "GÜNLÜK YOLCULUK BAŞARISI TESCİL EDİLDİ!"),
}

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

@st.dialog("TYT Çalışma Sistemi")
def show_onboarding():
    st.markdown("""
    <div style="text-align: center;">
        <div style="font-size: 48px; margin-bottom: 16px;">🏔️</div>
        <div style="font-family: 'Poppins', sans-serif; font-size: 13px; color: #5a4a3a; line-height: 1.6;">
            <strong>Mutedra Co.</strong> tarafından<br>
            <strong>Nuriye Hanımın</strong> şahsı için<br>
            özel kodlanmıştır.
            <br><br>
            Anadolu'da bir yolculuğa başla,<br>
            dağları, ormanları ve kuşları keşfet.
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 Yolculuğa Başla", use_container_width=True):
        st.session_state.onboarding_seen = True
        st.rerun()

if not st.session_state.onboarding_seen:
    show_onboarding()

st.markdown('<div class="hud-wrap"><div class="hud-title">🏔️ Nuriye Hanım Şahsına TYT Çalışma Yolculuğu</div><div class="hud-sub">Anadolu\'da Bir Öğrenme Serüveni</div></div>', unsafe_allow_html=True)

d1, d2, d3 = st.columns([1.5, 1.8, 1.4])
with d1:
    secilen_ders = st.selectbox("DERS", tum_dersler, index=tum_dersler.index(st.session_state.current_ders), key="ders_sel")

with d2:
    if secilen_ders in mevcut_dersler:
        konular = list(mevcut_dersler[secilen_ders].keys())
        default_idx = 0
        if st.session_state.current_konu and st.session_state.current_konu in konular:
            default_idx = konular.index(st.session_state.current_konu)
        secilen_konu = st.selectbox("KONU", konular, index=default_idx, key="konu_sel")
        
        # ÖNEMLI: Konu değişince hap_idx sıfırla
        if secilen_konu != st.session_state.current_konu:
            st.session_state.hap_idx = 0
            st.session_state.current_konu = secilen_konu
        
        st.session_state.current_ders = secilen_ders
    else:
        secilen_konu = st.selectbox("KONU", ["⏳ Yakında Eklenecek"], key="konu_wait", disabled=True)

with d3:
    st.markdown(f"<div style='padding-top: 10px; font-family:Poppins,sans-serif; font-size:11px; color:#7a6a5a; letter-spacing:1px; text-align:right; font-weight:600;'>{secilen_ders}</div>", unsafe_allow_html=True)

if secilen_ders in mevcut_dersler and secilen_konu != "⏳ Yakında Eklenecek":
    hap_bilgileri = mevcut_dersler[secilen_ders].get(secilen_konu, [])
    
    if not hap_bilgileri:
        st.markdown('<div class="hap-card"><div class="hap-text" style="color:#8b6f47;">⏳ Bu konunun hap bilgileri yükleniyor...</div></div>', unsafe_allow_html=True)
    else:
        if st.session_state.hap_idx >= len(hap_bilgileri):
            st.session_state.hap_idx = 0
        
        idx = st.session_state.hap_idx
        toplam = len(hap_bilgileri)
        
        pct = round((idx + 1) / toplam * 100, 1)
        st.markdown(f"""
<div class="prog-wrap">
    <div class="prog-meta"><span>HAP BİLGİ İLERLEMESİ</span><span>{idx+1} / {toplam} · %{pct}</span></div>
    <div class="prog-track"><div class="prog-fill" style="width:{pct}%"></div></div>
</div>""", unsafe_allow_html=True)
        
        st.markdown(f"""
<div class="stat-row">
    <div class="stat-box"><div class="stat-val">{idx+1}</div><div class="stat-lbl">Şu an</div></div>
    <div class="stat-box"><div class="stat-val">{toplam}</div><div class="stat-lbl">Toplam</div></div>
    <div class="stat-box"><div class="stat-val">{st.session_state.toplam_hap_goruldu}</div><div class="stat-lbl">Toplam Görülen</div></div>
</div>""", unsafe_allow_html=True)
        
        hap_text = str(hap_bilgileri[idx]).replace("<", "&lt;").replace(">", "&gt;")
        st.markdown(f'<div class="hap-card"><div class="hap-text">{hap_text}</div></div>', unsafe_allow_html=True)
        
        if st.session_state.toplam_hap_goruldu in ACHIEVEMENTS:
            emoji, basarim, aciklama = ACHIEVEMENTS[st.session_state.toplam_hap_goruldu]
            st.markdown(f"""
<div class="achievement-banner">
    <div class="achievement-emoji">{emoji}</div>
    <div class="achievement-text">{basarim}</div>
    <div class="achievement-desc">{aciklama}</div>
</div>""", unsafe_allow_html=True)
        
        b1, b2, b3, b4 = st.columns([1, 1.2, 1, 1])
        
        with b1:
            if st.button("◀ ÖNCEKİ KART", disabled=(idx == 0), key="onceki"):
                st.session_state.hap_idx = max(0, idx - 1)
                st.rerun()
        
        with b2:
            if st.button("🔀 RASTGELE", key="rastgele"):
                st.session_state.hap_idx = random.randint(0, toplam - 1)
                st.session_state.toplam_hap_goruldu += 1
                st.rerun()
        
        with b3:
            if st.button("SONRAKİ KART ▶", disabled=(idx == toplam - 1), key="sonraki"):
                st.session_state.hap_idx = min(toplam - 1, idx + 1)
                st.session_state.toplam_hap_goruldu += 1
                st.rerun()
        
        with b4:
            if st.button("↺ SIFIRLA", key="sifirla"):
                st.session_state.hap_idx = 0
                st.rerun()

else:
    if secilen_ders not in mevcut_dersler:
        st.markdown(f'<div class="hap-card"><div class="hap-text" style="color:#8b6f47;">⏳ <b>{secilen_ders}</b> dersi henüz hazırlanmadı.</div></div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

with st.expander("🏔️  ANADOLU'DA YOLCULUGUN HARİTASI"):
    st.markdown("""
**Hoşgeldin Gizemli Yolcu Nuriye. Yolculuğun Haritasını veriyorum:**

Anadolu'da bir öğrenme serüvenine başladın. Her hap bilgiyi okudukça, dağları tırmanıyor, ormanları geçiyor ve kuşları görüyorsun. Bol şans!

🎯 **Başarımlarını Takip Et (1-500):**
""")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
🐦 1-50: Kuş Dönemeci
🌲 51-100: Orman Gezinti
🏔️ 101-150: Dağ Tırmanışı
⛰️ 151-200: Tepe Yolculuğu
        """)
    with col2:
        st.markdown("""
🌿 201-250: Bitki Tanımı
🏞️ 251-300: Manzara Seyri
🦅 301-350: Yüksek Kuşlar
🌸 351-400: Çiçek Bahçeleri
        """)
    with col3:
        st.markdown("""
🌾 401-450: Tarla Yolculuğu
🏔️ 451-500: Zirveye Yükseliş
👑 500+: ANADOLU USTASI!
        """)

c1, c2 = st.columns([2, 1])
with c1:
    if st.button("🔄 YENILE", key="yenile"):
        st.cache_data.clear()
        st.rerun()
with c2:
    st.markdown(f"<div style='font-family:Poppins,sans-serif;font-size:9px;color:#7a6a5a;letter-spacing:1px;padding:10px 0;'>TYT ÇALIŞMA SİSTEMİ · AŞK İLE YAPILDI ❤️ · MUTEDRA CO.</div>", unsafe_allow_html=True)
