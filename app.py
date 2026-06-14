code_content = """import streamlit as st
import json
import random

st.set_page_config(
    page_title="TYT Çalışma Sistemi",
    page_icon="🏔️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS tamamen basitleştirildi. Mobil Safari'de beyaz ekrana neden olan agresif root (!important html/body) müdahaleleri, ağır animasyonlar ve st.App ezmeleri kaldırıldı.
st.markdown(\"\"\"<style>
.block-container { padding: 1.5rem 1rem 4rem !important; max-width: 780px !important; }
.hud-wrap { background: #d4c4b0; border: 2px solid #a89878; border-radius: 16px; padding: 18px 22px; margin-bottom: 16px; text-align: center; }
.hud-title { font-size: 24px; font-weight: bold; color: #5a4a3a; margin-bottom: 4px; }
.hud-sub { font-size: 12px; color: #7a6a5a; }
.prog-wrap { margin-bottom: 14px; }
.prog-meta { display: flex; justify-content: space-between; font-size: 12px; color: #6b5a4a; font-weight: bold; margin-bottom: 6px; }
.prog-track { background: #e8dcc8; border-radius: 8px; height: 12px; border: 1px solid #a89878; overflow: hidden; }
.prog-fill { height: 100%; border-radius: 8px; background: #8b6f47; transition: width 0.3s; }
.achievement-banner { background: #e8d5b7; border: 2px solid #8b6f47; border-radius: 12px; padding: 16px; margin: 16px 0; text-align: center; }
.hap-card { background: #f9f4ed; border: 2px solid #a89878; border-radius: 16px; padding: 30px 20px; margin: 16px 0; min-height: 180px; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
.hap-text { font-size: 18px; font-weight: bold; text-align: center; color: #3a3a3a; line-height: 1.6; }
.stat-row { display: flex; gap: 8px; margin-bottom: 16px; }
.stat-box { flex: 1; background: #dfd2bb; border: 1px solid #a89878; border-radius: 12px; padding: 12px; text-align: center; }
.stat-val { font-size: 22px; font-weight: bold; color: #8b6f47; }
.stat-lbl { font-size: 11px; color: #7a6a5a; font-weight: bold; }
.splash-card { text-align: center; padding: 40px 20px; background: #f9f4ed; border-radius: 20px; border: 2px solid #a89878; margin: 20px auto; max-width: 500px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
hr { border: none; border-top: 1px solid #a89878 !important; margin: 20px 0 !important; }
</style>\"\"\", unsafe_allow_html=True)

KOMIK_HIKAYELER = [
    ("🐦", "Anadolu Serçesinin Akıl Defteri", "Nuriye Hanım! Köy meydanındaki bilge serçe telli duvaklı defterine bakıp dedi ki: 'Formüller kısa, çaylar taze olmalı!' Haklı mı? Sonuna kadar haklı! Hadi başla!"),
    ("🦅", "Yörük Ali'nin Kartalı", "Toroslar'da bir Yörük Ali varmış, kartalına sormuş: 'Bu sınavı kim geçer?' Kartal da göklerden süzülüp pençesiyle Nuriye Hanım'ın masasını işaret etmiş! Rüzgarın bol olsun!"),
    ("🏔️", "Erciyes Dağı'nın İnadı", "Erciyes Dağı dile gelmiş: 'Beni aşmak zordur ama Nuriye Hanım'ın azmini görünce tepemdeki karlar eridi, utancımdan dumanımı sakladım' demiş. Dağlar önünde eğiliyor!"),
    ("🌲", "Asırlık Meşe Ağacının Fısıltısı", "Köyün girişindeki 500 yıllık meşe ağacı köklerini oynatıp fısıldamış: 'Ben bu yaşımda böyle kararlı ders çalışan görmedim. Nuriye Hanım bu hızla giderse yakında beni de geçer!'"),
    ("🌾", "Konya Ovası'ndaki Gizemli Traktör", "Konyalı bir dayı traktörle tarlayı sürerken Nuriye Hanım'ın hap bilgi okuma hızını görmüş. Traktörü stop ettirip 'Yahu biz dönüm başı bu kadar hızlı gidemedik, maşallah!' diyerek şapka çıkarmış!"),
    ("🦜", "Çaycı Hüseyin Efendi'nin Papağanı", "Sivaslı Çaycı Hüseyin'in papağanı normalde sadece 'Çay ver' dermiş. Ama Nuriye Hanım'ı görünce 'Nuriye Hanım yine başladı, paragraf soruları kaçacak delik arasın!' diye bağırmış!"),
    ("⛰️", "Horozlu Dede'nin Kehaneti", "Denizli'nin meşhur horozu bu sabah Nuriye Hanım için erken ötmüş: 'Üüü-ürü-üüü! Nuriye Hanım bugün TYT'yi dize getirecek!' Duymayan kalmasın!"),
    ("🌸", "Isparta Gülü'nün Kıskançlığı", "Isparta'nın en güzel gülü Nuriye Hanım'ın ders masasına bakıp boynunu bükmüş: 'Onun zihnindeki bilgi çiçekleri benden daha güzel kokuyor, pes ediyorum' demiş. Çiçekler açsın zihninde!"),
    ("🍵", "Kıraathanedeki Büyük Hakemlik", "Erzurumlu amcalar kahvehanede okeyi bırakmış senin başarımları tartışıyor: 'Hele bakın, Nuriye Hanım 1000 hap bilgiye doğru koşir, dadaşlık budur işte!' Çaylar şirketten!"),
    ("🌅", "Karadeniz Takası ve Fırtına", "Sürmeneli Temel Reis fırtınada dalgalarla boğuşurken Nuriye Hanım'ın ders çalışma azmini duymuş: 'Ula ben bu dalgalarla baş ederim de Nuriye Hanım'ın bilgi fırtınasının önünde duramam!' demiş."),
    ("🎯", "Kayserili Esnafın Ticari Dehası", "Kayserili sarraf Nuriye Hanım'ı ders çalışırken izlemiş ve yanındakine fısıldamış: 'Bu hanımdaki azim ve bilgi altından daha değerli, buraları satın alır valla!' Yatırım tavsiyesidir, devam!"),
    ("🏞️", "Yeşilırmak'ın Ters Akma İhtimali", "Amasya'daki Yeşilırmak Nuriye Hanım'ın kararlılığını görünce şaşkınlıktan ters akmaya karar vermiş: 'Nuriye Hanım sınavı altüst ederken ben düz mü akacağım?' demiş!"),
    ("🍉", "Diyarbakır Karpuzunun İtirafı", "150 kiloluk dev Diyarbakır karpuzu dile gelmiş: 'Ben Anadolu'nun en ağırıyım sanıyordum, meğer Nuriye Hanım'ın zihnindeki hap bilgilerin ağırlığı benimkinden fazlaymış' demiş!"),
    ("🏺", "Hattuşaş Güneşi Kursu", "Hitit kralı rüyasında Nuriye Hanım'ı görmüş ve vezirine emretmiş: 'Hemen bir tablet kazıyın, gelecekte Nuriye Hanım adında bir bilge tüm TYT konularını tek nefeste fethedecek!' Tarih seni yazıyor!"),
    ("🐈", "Van Kedisinin Renkli Gözleri", "Van kedisi Nuriye Hanım'ın ders notlarına bakarken heyecandan gözlerinin rengini şaşırmış! 'Ablam öyle bir konsantre olmuş ki, bende ne mavi kaldı ne yeşil!' diyerek mırıldanmış."),
    ("🫓", "Varto Tandır Ekmeğinin Sıcaklığı", "Muşlu teyze tandırdan sıcak ekmeği çıkarırken demiş ki: 'Bu ekmek sıcak ama Nuriye Hanım'ın ders çalışma aşkı ve motivasyonu bu tandır ateşinden de sıcak!' Afiyet olsun, zihnin açık olsun!"),
    ("🧀", "Kars Kaşarının Olgunlaşma Sırrı", "Kars'taki peynir ustası sırrını açıklamış: 'Biz peyniri mahzende bekletiriz ama asıl olgunlaşma Nuriye Hanım'ın zihnindeki hap bilgilerin demlenmesi gibidir, sabırla ve emekle olur!'"),
    ("🏺", "Çömlekçi Ustanın Çırağı", "Avanoslu çömlek ustası çamura şekil verirken çırağına bağırmış: 'Oğlum elini gevşek tutma! Bak Nuriye Hanım derslerine nasıl sıkı sarılıyor, örnek al ablanı!'"),
    ("🎠", "Nasreddin Hoca'nın Yeni Müjdesi", "Nasreddin Hoca göle maya çalmaktan vazgeçmiş, gelmiş Nuriye Hanım'ın masasına bakmış: 'Yahu Hoca, bu göl maya tutar mı?' diyenlere, 'Gölü bırakın, Nuriye Hanım bu azimle TYT'yi kesin tutturur!' demiş."),
    ("🌶️", "Maraş Biberinin Acı İtirafı", "Kahramanmaraş'ın en acı biberi Nuriye Hanım'ın deneme çözme hızını görünce terlemiş: 'Ben insanları yakardım ama Nuriye Hanım'ın hırsı beni bile kavurdu!' demiş. Yolun açık olsun!"),
    ("🎻", "Aşık Veysel'in Sazının Teli", "Sazın teli kendi kendine titremeye başlamış. Demişler ne oluyor? Saz dile gelmiş: 'Nuriye Hanım 1000 başarıma doğru emin adımlarla yürüyor, ona güzel bir fon müziği yapıyorum!'"),
    ("🏰", "Ankara Kalesi'nin Güvencesi", "Ankara Kalesi'nin burçlarındaki askerler nöbette konuşuyormuş: 'Kaleden daha sağlam ne var bu memlekette?' Biri cevap vermiş: 'Nuriye Hanım'ın TYT çalışma disiplini var, kale gibi sarsılmaz!'"),
    ("🍇", "Erzincan Tulumu ve Üzümü", "Cimin üzümü bağından seslenmiş: 'Nuriye Hanım hap bilgileri birer birer yerken, biz burada hayranlıkla onu izliyoruz. Bu tatlı yolculuğun sonu şampiyonluk!'"),
    ("🧵", "Bursa İpeğinin Zarafeti", "Bursa'daki ipek böceği kozasını örerken durup düşünmüş: 'Ben ilmek ilmek örüyorum ama Nuriye Hanım bilgileri zihnine daha zarif ve sağlam işliyor.' Helal olsun abla!"),
    ("🍯", "Anzer Arısının Kararlılığı", "Kaçkarlar'daki Anzer arısı en şifalı çiçeği ararken Nuriye Hanım'ın masasına konmuş: 'Ben bin çiçekten bal topluyorum ama Nuriye Hanım bin hap bilgiden gelecek inşa ediyor, asıl şifa onda!'")
]

# 1'den 1000'e kadar tam 42 adet eşsiz başarım (Her 25 hap bilgide bir)
ACHIEVEMENTS = {
    1: ("🐦", "Anadolu Serçesini Buldun", "Yolculuk bin adımlık bir yürüyüşle başlar, ilk hap bilgi cebinizde Nuriye Hanım!"),
    10: ("🏔️", "Iğdır Dağı Etekleri", "10 hap bilgi tamamlandı! Zirve uzakta görünebilir ama ilk tırmanış başarıyla başladı."),
    25: ("🌳", "Meşe Ormanında Dinlenme", "25 hap bilgiye ulaştın. Anadolu'nun asırlık çınarları azmine şahit oluyor."),
    50: ("🌾", "Konya Ovası Bereketleri", "50 hap bilgi! Bilgi tarlanı sabırla ektin, bereketli başaklar yeşermeye başladı."),
    75: ("🐎", "Kapadokya Yılkı Atları", "75 hap bilgi! Zihnin uçsuz bucaksız bozkırda özgürce koşan atlar gibi hızlandı."),
    100: ("🎯", "Yüzüncü Yıl Kahramanı", "100 hap bilgiyi tamamladın! Bu sarsılmaz azim tüm Anadolu'ya örnek olur."),
    125: ("🍯", "Kars Karakovan Balı", "125 hap bilgi! Emeklerin petek petek doluyor, zihnin şifa buluyor."),
    150: ("🦅", "Toros Kartalı Kanat Çırpışı", "150 hap bilgi! Artık TYT konularına çok daha yükseklerden ve net bakıyorsun."),
    175: ("🏺", "Avanos Çömlek Ustası", "175 hap bilgi! Bilgiyi elinde bir kil gibi yoğuruyor, ona şekil veriyorsun."),
    200: ("🧿", "Nazar Boncuğu Koruması", "200 hap bilgi! Kem gözlere şiş, bu motivasyon ve odaklanma hiç bozulmasın!"),
    225: ("🍉", "Diyarbakır Karpuzu Bereketi", "225 hap bilgi! Hafızan o kadar genişledi ki, içine koca bir medeniyet sığar."),
    250: ("🏞️", "Yeşilırmak Kanyonu Yankısı", "250 hap bilgi! Çalışmalarının yankısı derin vadilerden tüm şehirlere duyuluyor."),
    275: ("🕌", "Selimiye Kubbesi İhtişamı", "275 hap bilgi! Zihninin mimarisi tıpkı Sinan'ın eserleri gibi kusursuz yükseliyor."),
    300: ("🍵", "Kıraathane Bilgesi", "300 hap bilgi tamamlandı! Muhtar ve tüm ahali senin bu muazzam hızını konuşuyor."),
    325: ("🧶", "Hereke Halısı Dokuyucusu", "325 hap bilgi! Her bir formülü ve kuralı zihnine ilmek ilmek, altın sırmalarla işledin."),
    350: ("🌸", "Isparta Gül Bahçeleri Kokusu", "350 hap bilgi! Zihninde açan taze bilgi güllerinin kokusu tüm engelleri unutturdu."),
    375: ("🏔️", "Ağrı Dağı Zirvesi", "375 hap bilgi! Anadolu'nun en yüksek tepesine adım adım, nefes nefese tırmanıyorsun."),
    400: ("🏰", "Ankara Kalesi Zirve Burçları", "400 hap bilgi geride kaldı. Kaleyi kalbinden ve zihninden fethettin Nuriye Hanım!"),
    425: ("🫓", "Varto Tandır Ekmeği Sıcaklığı", "425 hap bilgi! Başarı sıcak sıcak tütüyor, emeklerinin kokusu her yeri sardı."),
    450: ("⛰️", "Erciyes'in Dumanlı Zirvesi", "450 hap bilgiye ulaştın. Bulutların üzerindesin, zafere adımlar kaldı."),
    475: ("🧀", "Ezine Peyniri Ustası", "475 hap bilgi! Bilgilerin zamanla demlendi, keskinleşti ve en lezzetli halini aldı."),
    500: ("👑", "Anadolu Zirvesi Yarıyıl", "500 hap bilgi! Yolun tam yarısı bitti, altın harflerle adın zirveye kazındı!"),
    525: ("🎻", "Aşık Veysel'in Sazı", "525 hap bilgi! Uzun ince bu yolda artık ustalıkla ve türküler eşliğinde yürüyorsun."),
    550: ("🎠", "Eskişehir Lületaşı Zarafeti", "550 hap bilgi! Zihnini bir sanat eseri gibi ilmek ilmek ve ince ince işliyorsun."),
    575: ("🌊", "Fırtına Deresi Coşkusu", "575 hap bilgi! Hiçbir engel tanımadan, Karadeniz dereleri gibi coşkun akıyorsun."),
    600: ("🌌", "Kapadokya Peri Bacaları Masalı", "600 hap bilgi! Başarın Anadolu masalları gibi büyüleyici ve benzersiz bir hal aldı."),
    625: ("🌰", "Giresun Fındık Bahçesi", "625 hap bilgi! Çotanaklar gibi bereketli, her bilgi tanesi zihninde sağlamca kök saldı."),
    650: ("🌿", "Toros Geyikbayırı Derinlikleri", "650 hap bilgiye ulaştın. En dik patikalar bile senin iraden karşısında düzleşti."),
    675: ("🦁", "Aslanlı Yol Yürüyüşü", "675 hap bilgi! Hedefe doğru atılan her adım, tarihe geçen sağlam bir yürüyüş oldu."),
    700: ("🌊", "Çoruh Nehri Akıntısı", "700 hap bilgi! Bilgi selin önüne çıkan tüm setleri, barajları yıkıp geçiyor."),
    725: ("🧵", "Bursa İpeği Zarafeti", "725 hap bilgi! Sınav stresini ipek gibi pürüzsüz ve yumuşak bir zihinle aşıyorsun."),
    750: ("🪕", "Gönül Dağı Yolcusu", "750 hap bilgi! Gönül dağında karlar eridi, başarı çiçekleri rengarenk açmaya başladı."),
    775: ("🍇", "Erzincan Cimin Üzümü", "775 hap bilgi! Bu zorlu çalışma günleri, sonunda tadına doyulmaz salkımlara dönüştü."),
    800: ("🦅", "Göbeklitepe Gözcüsü", "800 hap bilgi tamamlandı! Tarihin sıfır noktasından bugüne gelen en sarsılmaz irade."),
    825: ("☀️", "Nemrut Dağı Gündoğumu", "825 hap bilgi! Heykellerin arasından doğan güneş gibi, zihnini aydınlattın."),
    850: ("🌲", "Yenice Ormanları Saymanlığı", "850 hap bilgi! Sayısız bilgi fidanını hafıza ormanının en verimli toprağına diktin."),
    875: ("⚔️", "Erzurum Dadaş İradesi", "875 hap bilgi! Palandöken'in ayazında bile üşümeyen bir dadaş gibi dimdik ayaktasın."),
    900: ("🍯", "Kaçkar Anzer Balı Şifası", "900 hap bilgi! Bu dökülen alın terinin sonundaki ödül, en şifalı bal gibi tatlı olacak."),
    925: ("🏹", "Malazgirt Ovası Fatihi", "925 hap bilgi! Anadolu'nun kapılarını ardına kadar bilgiyle ve azimle açıyorsun."),
    950: ("⚡", "Dumlupınar Taarruzu", "950 hap bilgi! Son kulvar, son adımlar... Cephede mutlak zafer artık an meselesidir!"),
    975: ("🇹🇷", "Cumhuriyet Fidanı", "975 hap bilgi! Fikri hür, irfanı hür bir zihinle zirveye sadece ramak kaldı."),
    1000: ("👑", "ANADOLU USTASI EFSANESİ", "1000 HAP BİLGİ BİTTİ! Destan yazıldı, Nuriye Hanım TYT'nin mutlak efsanesi oldunuz!")
}

@st.cache_data(show_spinner=False)
def load_data():
    try:
        with open("dersler.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"dersler": {"Türkçe": {"Örnek Konu": ["Ders verileri yüklenemedi. Lütfen dersler.json dosyasını yükleyin."]}}}

data = load_data()
mevcut_dersler = data.get("dersler", {})
tum_dersler = ["Türkçe", "Matematik", "Fen", "Sosyal"]

# Session State Başlatma
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

# --- SPLASH EKRANI (Açılış Hikayesi) ---
if not st.session_state.onboarding_seen:
    st.markdown("<br>", unsafe_allow_html=True)
    emoji, baslik, mesaj = st.session_state.daily_story
    
    st.markdown(f\"\"\"
    <div class="splash-card">
        <div style="font-size: 60px; margin-bottom: 10px;">{emoji}</div>
        <h2 style="color: #5a4a3a; margin-bottom: 10px;">{baslik}</h2>
        <p style="color: #5a4a3a; font-size: 16px; line-height: 1.5;">{mesaj}</p>
        <hr style="border-top: 1px solid #a89878; margin: 20px 0;">
        <p style="font-size: 12px; color: #8b6f47; font-weight: bold;">Mutedra Co. / Nuriye Hanım Şahsına Özel</p>
    </div>
    \"\"\", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 YOLCULUĞA BAŞLA", use_container_width=True):
            st.session_state.onboarding_seen = True
            st.rerun()

# --- ANA UYGULAMA (Sadece Onboarding Görüldüyse Çalışır) ---
else:
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
        st.markdown(f"<div style='padding-top: 30px; font-size:12px; color:#7a6a5a; text-align:right; font-weight:bold;'>{secilen_ders}</div>", unsafe_allow_html=True)

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
            st.markdown(f\"\"\"
            <div class="prog-wrap">
                <div class="prog-meta"><span>HAP BİLGİ İLERLEMESİ</span><span>{idx+1} / {toplam} · %{pct}</span></div>
                <div class="prog-track"><div class="prog-fill" style="width:{pct}%"></div></div>
            </div>\"\"\", unsafe_allow_html=True)
            
            st.markdown(f\"\"\"
            <div class="stat-row">
                <div class="stat-box"><div class="stat-val">{idx+1}</div><div class="stat-lbl">Şu an</div></div>
                <div class="stat-box"><div class="stat-val">{toplam}</div><div class="stat-lbl">Toplam</div></div>
                <div class="stat-box"><div class="stat-val">{st.session_state.toplam_hap_goruldu}</div><div class="stat-lbl">Toplam Görülen</div></div>
            </div>\"\"\", unsafe_allow_html=True)
            
            hap_text = str(hap_bilgileri[idx]).replace("<", "&lt;").replace(">", "&gt;")
            st.markdown(f'<div class="hap-card"><div class="hap-text">{hap_text}</div></div>', unsafe_allow_html=True)
            
            if st.session_state.toplam_hap_goruldu in ACHIEVEMENTS:
                emoji, basarim, aciklama = ACHIEVEMENTS[st.session_state.toplam_hap_goruldu]
                st.markdown(f\"\"\"
                <div class="achievement-banner">
                    <div style="font-size: 30px; margin-bottom: 6px;">{emoji}</div>
                    <div style="font-size: 18px; font-weight: bold; color: #5a4a3a;">{basarim}</div>
                    <div style="font-size: 13px; color: #7a6a5a; margin-top: 4px;">{aciklama}</div>
                </div>\"\"\", unsafe_allow_html=True)
            
            b1, b2, b3, b4 = st.columns([1, 1.2, 1, 1])
            
            with b1:
                if st.button("◀ ÖNCEKİ", disabled=(idx == 0), key="onceki"):
                    st.session_state.hap_idx = max(0, idx - 1)
                    st.rerun()
            
            with b2:
                if st.button("🔀 RASTGELE", key="rastgele"):
                    st.session_state.hap_idx = random.randint(0, toplam - 1)
                    st.session_state.toplam_hap_goruldu += 1
                    st.rerun()
            
            with b3:
                if st.button("SONRAKİ ▶", disabled=(idx == toplam - 1), key="sonraki"):
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

    c1, c2 = st.columns([2, 1])
    with c1:
        if st.button("🔄 YENİLE & YENİ HİKAYE GÖSTER", key="yenile"):
            st.session_state.daily_story = random.choice(KOMIK_HIKAYELER)
            st.session_state.onboarding_seen = False
            st.cache_data.clear()
            st.rerun()
    with c2:
        st.markdown(f"<div style='font-size:10px;color:#7a6a5a;text-align:right;padding-top:15px;font-weight:bold;'>MUTEDRA CO.</div>", unsafe_allow_html=True)
"""

with open("tyt_calisma_sistemi_v3.py", "w", encoding="utf-8") as f:
    f.write(code_content)
print("File regenerated successfully.")
