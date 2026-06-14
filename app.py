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
.story-box { background: linear-gradient(135deg, #e8d5b7 0%, #d9c9b3 100%); border: 2px solid #8b6f47; border-radius: 14px; padding: 20px; margin: 16px 0; text-align: center; }
.story-emoji { font-size: 32px; margin-bottom: 8px; }
.story-text { font-family: 'Cormorant Garamond', serif; font-size: 15px; color: #5a4a3a; line-height: 1.7; }
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

# Rastgele Komik Hikayeler
KOMIK_HIKAYELER = [
    ("🐦", "Serçenin Ders Notu", "Anadolu Serçesi sana 'Hap bilgiler kısa ve etkili olmalı' dedi. Haklı mı? Tabii ki haklı!"),
    ("🦅", "Kartalın Tavsiyesi", "Yüksek uçmak için iyiyotlara ihtiyaç var. Sen de böyle yapıyorsun!"),
    ("🏔️", "Dağın İntikamı", "Dağ: 'Beni tırmanmak zor, ama zirveye ulaşan hiç pişman olmaz.' Hazır mısın?"),
    ("🌲", "Ağacın Hikayesi", "Orman Şefi Meşe Ağacı: 'Kütleşme yavaş ama güçlü olur. Sen de öyle çalış!'"),
    ("🌾", "Çiftçinin Sırrı", "Çiftçi: 'Topu kuru, suyu bol, ve sabırla bekle. Sonra hasat zamanı gelir.'"),
    ("🦜", "Papağanın Tekrarı", "Karçıkakı: 'Bildiklerini tekrar söylenince, unutulan kapı açılır.'"),
    ("⛰️", "Dağ Tırmanışı", "Rehber: 'Her adım önemli, aceleci olma. Zirve seni bekliyor.'"),
    ("🌸", "Çiçeğin Dersi", "Çandırı Çiçeği: 'Ben bahar bekledi. Sen ne bekliyor?'"),
    ("🍵", "Çay Bahçesinde Hikaye", "Torna: 'Sıcak suyla ıslatılınca lezzetliyim. Sen de zorluktan güç alıyor musun?'"),
    ("🌅", "Gün Batımında Dönem", "Ordu Platosu: 'Her gün biter, ama yeni bir gün doğar. Devam et!'"),
    ("🎯", "Av Kuşunun Dikkati", "Şahin: 'Hedefi belirle, çabukça har ve ıskalamaz. Hap bilgiyi öyle oku.'"),
    ("🏞️", "Kanyonun Yankısı", "Yeşilırmak: 'Bağırsan sesi geri dönüyor. Çalışsan da sonucu dönüyor.'"),
    ("🌿", "Ormanın Derinliği", "Toros Ormanı: 'Içimde kaybolabilirsin, ama çıkışa varırsan çok güzel olur.'"),
    ("🦌", "Ceylanın Hızı", "Ceylan: 'Hızlı ama tekinlemli. Ders geçmek için her türü deneme!'"),
    ("🪨", "Kaya Sarayları", "Kapadokya: 'Zamanın üzerine yazılmış hikayelerim var. Senin hap bilgiler de sana yazılmış.'"),
]

ACHIEVEMENTS = {
    1: ("🐦", "Anadolu Serçesini buldun", "Başarımına başladın"),
    10: ("🏔️", "Iğdır Dağına hoş geldin", "10 hap bilgiye vardın"),
    25: ("🌳", "Meşe Ormanında Dinlendin", "25 hap bilgiye vardın"),
    50: ("🌾", "Konya Ovasında yürüdün", "50 hap bilgiye ulaştın"),
    100: ("🎯", "Yüzüncü Başarım Kutlandı!", "100 hap bilgiyi tamamladın"),
    150: ("🦅", "Kartal Gökyüzünde", "150 hap bilgiye vardın"),
    200: ("🎯", "İkiyüzüncü Başarım!", "200 hap bilgiyi tamamladın"),
    250: ("🏞️", "Kanyonun Yankısında", "250 hap bilgiye ulaştın"),
    300: ("🎯", "Üçyüzüncü Başarım Kriteri!", "300 hap bilgiyi tamamladın"),
    350: ("🌸", "Çiçek Bahçelerinde Ruh Dinlemesi", "350 hap bilgiye vardın"),
    400: ("🎯", "Dörtyüzüncü Başarım!", "400 hap bilgiyi tamamladın"),
    450: ("🏔️", "Zirveye Yakındır", "450 hap bilgiye ulaştın"),
    500: ("👑", "ANADOLU ZIRVESI 500!", "GÜNLÜK YOLCULUK BAŞARISI TESCİL EDİLDİ!"),
    550: ("🦅", "Yüksekten Bakanlar Kulübü", "550 hap bilgiye vardın"),
    600: ("🎯", "Altıyüzüncü Başarım!", "600 hap bilgiyi tamamladın"),
    650: ("🌿", "Ormanın Derinliklerinde", "650 hap bilgiye ulaştın"),
    700: ("🎯", "Yediyüzüncü Başarım!", "700 hap bilgiyi tamamladın"),
    750: ("⛰️", "Dağların İnsan Dostu", "750 hap bilgiye vardın"),
    800: ("🎯", "Sekizyüzüncü Başarım Kutlama!", "800 hap bilgiyi tamamladın"),
    850: ("🌲", "Orman Saymanı", "850 hap bilgiye ulaştın"),
    900: ("🎯", "Dokuzyüzüncü Başarım!", "900 hap bilgiyi tamamladın"),
    950: ("🦅", "Binden Bir Adım Uzak", "950 hap bilgiye vardın"),
    1000: ("👑", "ANADOLU USTASI 1000 HAP!", "EPIK YOLCULUK TAMAMLANDI - SEN BİR EFSANESİN!"),
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
if "daily_story" not in st.session_state:
    st.session_state.daily_story = random.choice(KOMIK_HIKAYELER)

@st.dialog("TYT Çalışma Sistemi")
def show_onboarding():
    emoji, baslik, mesaj = st.session_state.daily_story
    st.markdown(f"""
    <div style="text-align: center;">
        <div style="font-size: 48px; margin-bottom: 16px;">{emoji}</div>
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 700; color: #5a4a3a; margin-bottom: 12px;">{baslik}</div>
        <div style="font-family: 'Poppins', sans-serif; font-size: 13px; color: #5a4a3a; line-height: 1.6;">
            {mesaj}
            <br><br>
            <strong>Mutedra Co.</strong> tarafından<br>
            <strong>Nuriye Hanımın</strong> şahsı için özel kodlanmıştır.
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

🎯 **Başarımlarını Takip Et (1-1000):**
""")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
🐦 1-100: Kuş Dönemeci
🌲 101-200: Orman Gezinti
🏔️ 201-300: Dağ Tırmanışı
⛰️ 301-400: Tepe Yolculuğu
        """)
    with col2:
        st.markdown("""
🌿 401-500: Bitki Tanımı
🏞️ 501-600: Manzara Seyri
🦅 601-700: Yüksek Kuşlar
🌸 701-800: Çiçek Bahçeleri
        """)
    with col3:
        st.markdown("""
🌾 801-900: Tarla Yolculuğu
🏔️ 901-950: Zirveye Yükseliş
👑 950-1000: ANADOLU USTASI!
        """)
    with col4:
        st.markdown(f"""
💪 Toplam Bölüm: 40
📊 Her 25 hap: Yeni başarım
🎯 Hedefin: 1000 HAP
""")

c1, c2 = st.columns([2, 1])
with c1:
    if st.button("🔄 YENILE & YENİ HİKAYE", key="yenile"):
        st.session_state.daily_story = random.choice(KOMIK_HIKAYELER)
        st.cache_data.clear()
        st.rerun()
with c2:
    st.markdown(f"<div style='font-family:Poppins,sans-serif;font-size:9px;color:#7a6a5a;letter-spacing:1px;padding:10px 0;'>TYT ÇALIŞMA SİSTEMİ · AŞK İLE YAPILDI ❤️ · MUTEDRA CO.</div>", unsafe_allow_html=True)
