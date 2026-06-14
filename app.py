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
.hud-title { font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 700; color: #5a4a3a; letter-spacing: 1px; }
.hud-sub { font-family: 'Poppins', sans-serif; font-size: 10px; color: #7a6a5a; letter-spacing: 1px; margin-top: 2px; }
.prog-wrap { margin-bottom: 14px; }
.prog-meta { display: flex; justify-content: space-between; font-family: 'Poppins', sans-serif; font-size: 10px; color: #6b5a4a; margin-bottom: 6px; font-weight: 600; text-transform: uppercase; }
.prog-track { background: #d4c4b0; border-radius: 8px; height: 8px; border: 1px solid #a89878; overflow: hidden; }
.prog-fill { height: 100%; border-radius: 8px; background: linear-gradient(90deg, #8b6f47 0%, #b8956a 100%); transition: width .5s ease; }
.achievement-banner { background: linear-gradient(135deg, #e8d5b7 0%, #d9c9b3 100%); border: 2px solid #8b6f47; border-radius: 12px; padding: 14px 16px; margin: 12px 0; text-align: center; animation: slideIn .5s ease; }
@keyframes slideIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
.achievement-emoji { font-size: 28px; margin-bottom: 6px; }
.achievement-text { font-family: 'Cormorant Garamond', serif; font-size: 16px; font-weight: 700; color: #5a4a3a; letter-spacing: 1px; }
.achievement-desc { font-size: 12px; color: #7a6a5a; margin-top: 4px; }
.hap-card { background: linear-gradient(135deg, #f9f4ed 0%, #f0e8dd 100%); border: 2px solid #a89878; border-radius: 16px; padding: 30px 26px; margin: 14px 0; min-height: 200px; display: flex; align-items: center; justify-content: center; animation: up .4s ease; position: relative; box-shadow: 0 4px 12px rgba(0,0,0,0.06); }
.hap-card::before { content: '🌿'; position: absolute; top: 12px; right: 20px; font-size: 24px; opacity: 0.3; }
@keyframes up { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.hap-text { font-family: 'Cormorant Garamond', serif; font-size: 18px; font-weight: 600; line-height: 1.8; text-align: center; color: #3a3a3a; letter-spacing: .5px; }
.stat-row { display: flex; gap: 8px; margin-bottom: 12px; }
.stat-box { flex: 1; background: linear-gradient(135deg, #e8dcc8 0%, #dfd2bb 100%); border: 1px solid #a89878; border-radius: 12px; padding: 12px; text-align: center; }
.stat-val { font-family: 'Cormorant Garamond', serif; font-size: 18px; font-weight: 700; color: #8b6f47; }
.stat-lbl { font-family: 'Poppins', sans-serif; font-size: 9px; color: #7a6a5a; margin-top: 4px; font-weight: 600; }
.stSelectbox > div > div { background: #f0e8dd !important; border: 1px solid #a89878 !important; color: #3a3a3a !important; border-radius: 10px !important; font-size: 13px !important; }
.stSelectbox label { color: #5a4a3a !important; font-family: 'Cormorant Garamond', serif !important; font-size: 13px !important; font-weight: 600 !important; letter-spacing: 1px !important; }
.stButton > button { font-family: 'Poppins', sans-serif !important; font-weight: 600 !important; font-size: 11px !important; letter-spacing: 1px !important; text-transform: uppercase !important; border-radius: 10px !important; height: 44px !important; width: 100% !important; background: linear-gradient(135deg, #d4c4b0 0%, #cbb89f 100%) !important; border: 1px solid #a89878 !important; color: #5a4a3a !important; transition: all .2s !important; }
.stButton > button:hover:not(:disabled) { background: linear-gradient(135deg, #b8956a 0%, #a8854a 100%) !important; border-color: #5a4a3a !important; color: #f9f4ed !important; box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important; }
.stButton > button:disabled { opacity: .4 !important; }
details > summary { background: #e8dcc8 !important; border: 1px solid #a89878 !important; border-radius: 10px !important; color: #5a4a3a !important; font-family: 'Cormorant Garamond', serif !important; font-size: 13px !important; font-weight: 700 !important; padding: 12px 16px !important; }
details[open] > summary { border-radius: 10px 10px 0 0 !important; }
details > div { background: #f0e8dd !important; border: 1px solid #a89878 !important; border-top: none !important; border-radius: 0 0 10px 10px !important; padding: 16px !important; }
#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stDecoration"] { display: none !important; }
hr { border: none; border-top: 1px solid #a89878 !important; margin: 14px 0 !important; }
</style>""", unsafe_allow_html=True)

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
    ("🍯", "Anzer Arısının Kararlılığı", "Kaçkarlar'daki Anzer arısı en şifalı çiçeği ararken Nuriye Hanım'ın masasına konmuş: 'Ben bin çiçekten bal topluyorum ama Nuriye Hanım bin hap bilgiden gelecek inşa ediyor, asıl şifa onda!'"),
    ("🦉", "Efes'in Bilge Baykuşu", "Antik Celsus Kütüphanesi'nin sütunlarında tüneyen 2000 yıllık baykuş, Nuriye Hanım'ın hızını görünce gözlüğünü düzeltti: 'Biz Romalılar Stoacı felsefeyi severdik ama bu hanımın odaklanma kapasitesi Marcus Aurelius'u bile çırağa çıkarır! Hu hu! Hadi teste devam!'"),
    ("🫒", "Ege'nin Asırlık Zeytin Ağacı", "Kaz Dağları'ndaki 800 yıllık zeytin ağacı dallarını eğip mırıldandı: 'Köklerim asırlardır bu mitolojik topraklara tutunuyor ama Nuriye Hanım'ın şu masaya ve hedeflerine tutunuşu benden bile sağlam. Yağım ve bilgeliğim sana feda olsun!'"),
    ("🐢", "İztuzu'nun Filozof Caretta'sı", "Dalyan sahilindeki filozof Caretta Caretta, Nuriye Hanım'ın paragraf çözümünü izlerken utandı: 'Ben denize ulaşana kadar aylar geçiyor, Nuriye Hanım bir nefeste üç medeniyet tarihi deviriyor. Görelilik kuramı tam olarak buymuş!'"),
    ("🌬️", "Çanakkale Boğazı'nın Lodosu", "Çanakkale'de esen hırçın lodos, pencereden sızdı ve yelkenleri suya indirdi: 'Ben İlyada destanındaki dev gemileri yoldan çıkardım ama bu kadının çalışma ritmini milim sarsamadım. Truva surlarından bile sağlam bir iradesi var!'"),
    ("🏛️", "Sümela'nın Sarp Kayalıkları", "Trabzon'da uçuruma tutunan Sümela Manastırı dile geldi: 'Yüzyıllardır şu yerçekimine inat dengede dururum, ama Nuriye Hanım'ın onca ders ve hap bilgi arasında kurduğu o kusursuz zihinsel denge beni bile kıskandırdı!'"),
    ("🦩", "Tuz Gölü'nün Entelektüel Flamingosu", "Tuz Gölü'nde tek ayak üstünde duran flamingo mırıldandı: 'Suyun tuzluluk oranı ile bu hanımın net artış grafiği arasında felsefi bir doğru orantı var. Nuriye Hanım öyle bir odaklandı ki, şaşkınlıktan iki ayağımın üzerine bastım!'"),
    ("🐕", "Sivas'ın Sadık Kangalı", "Sivas yaylalarındaki dev Kangal köpeği masanın önüne yattı ve uludu: 'Bu saatten sonra bu masaya ne anksiyete yaklaşabilir ne de erteleme hastalığı. Alan koruması bende Nuriye Hanım, sen o soruları paramparça et!'"),
    ("⛰️", "Ağrı Dağı'nın İhtişamlı Zirvesi", "Türkiye'nin çatısı Ağrı Dağı, bulutlardan sıyrılıp gülümsedi: 'Benim zirvem soğuk, karlı ve ıssızdır. Ama senin ulaşacağın o zirve bilgiyle, aydınlıkla ve zaferin o sıcacık ateşiyle dolu olacak Nuriye Hanım! Adım adım geliyorsun!'"),
    ("🌳", "Antep Fıstığı Ağacının Sabrı", "Kavurucu sıcağın altındaki fıstık ağacı fısıldadı: 'Çöl sıcağında sert kabuğumu çatlatıp meyve vermek kolay değil sanırdım... Ta ki Nuriye Hanım'ın o en zor felsefe sorularının kabuğunu tık tık kırmasını görene dek!'"),
    ("🌊", "Munzur Suyu'nun Berraklığı", "Tunceli dağlarından kopup gelen Munzur Suyu coşkuyla çağladı: 'Ben bin yıllık kayaları dele dele gelirim ama Nuriye Hanım'ın zihni benden bile berrak! Hangi TYT sorusu bu akıntının önünde durabilir ki?'"),
    ("🐎", "Erciyes'in Asi Yılkı Atları", "Kayseri eteklerinde özgürce koşan yılkı atları aniden durup kulak kabarttı. En asisi kişnedi: 'Biz bozkırın deli rüzgarıyla yarışırız sanırdık, Nuriye Hanım'ın sayfa çevirme hızıyla karşılaşana kadar. Teslim oluyoruz!'"),
    ("🌲", "Torosların Ulu Sedir Ağacı", "Torosların zirvesindeki yalnız sedir yapraklarını hışırdatarak konuştu: 'Benim kozalaklarım yıllarca olgunlaşmayı bekler. Nuriye Hanım ise her hap bilgide yepyeni bir evrensel kozalak patlatıyor zihninde!'"),
    ("🐝", "Marmaris'in Çam Arısı", "Muğla ormanlarında çam balı yapan arı notlara kondu: 'Ben bir kilo bal için 40 bin uçuş yapıyorum, Nuriye Hanım oturduğu yerden bilimi süzüp en saf entelektüel balı üretiyor. Kraliçe arı tacını acilen devretmem gerek!'"),
    ("🪨", "Pamukkale'nin Beyaz Travertenleri", "Şifalı sular usulca fısıldadı: 'Bana termodinamik yasalarıyla kalsiyum çökeltmek zor gelirdi, Nuriye Hanım'ın sinapslarında kurduğu o devasa kimyasal bağları görene kadar! İhtişamdan rengim daha da ağardı!'"),
    ("🔥", "Çıralı'nın Sönmeyen Ateşi", "Olympos eteklerindeki bin yıllık Yanartaş dile geldi: 'Yunan mitolojisindeki Kimera bile binlerce yıldır böyle harlı yanmadı! Nuriye Hanım'ın içindeki o öğrenme ve başarma ateşi, efsaneleri gölgede bıraktı. Yansın o testler!'"),
    ("🦅", "Palandöken'in Kar Kartalı", "Erzurum'un dondurucu ayazında uçan kar kartalı kanat çırptı: 'Hava eksi 30 derece, tüm dereler dondu ama Nuriye Hanım'ın içindeki başarma ateşi öyle bir yanıyor ki, Palandöken'in karları eriyecek!'"),
    ("🌰", "Ordu'nun Yüklü Fındık Dalı", "Karadeniz'in yamaçlarındaki ağır bir fındık dalı rüzgarda sallanıp dedi ki: 'İçim dolu dolu mahsulle taşıyor ama Nuriye Hanım'ın zihni öyle bir bilgiyle doldu ki, benim dallarım onun ağır entelektüel yükü yanında hafif kalır!'"),
    ("🕊️", "Göbeklitepe'nin Tarihi Güvercini", "Tarihin sıfır noktasında uçan bilge güvercin: 'T-şekilli dev dikilitaşları dikenler büyük mühendismiş ama Nuriye Hanım'ın şu an kurduğu o analitik altyapı, insanlık tarihine yeni bir çağ atlatacak kalitede!'"),
    ("🐟", "Van Gölü'nün İnci Kefali", "Akıntıya karşı uçarak yüzen İnci Kefali sudan sıçrayıp bağırdı: 'Zorluklara karşı tersine yüzmek bizim işimiz sanırdık, Nuriye Hanım'ın o karmaşık problemlerle mücadelesini görene kadar! Ne eşsiz bir inat maşallah!'"),
    ("💦", "Kaz Dağları'nın Coşkun Şelalesi", "İda Dağı'nın eteklerindeki şelale gürledi: 'Mitolojik çağlardan beri böyle coşkun akmadım. Nuriye Hanım'ın o berrak zihniyle konuları bir çırpıda yutması benim asırlık akıntımı bile kıskandırdı!'"),
    ("✨", "Nemrut Dağı'nın Gece Yıldızları", "Antiochus'un dev heykelleri üzerinde parlayan Sirius yıldızı göz kırptı: 'İki bin yıldır burada yalnız bizim ışığımız yanar sanırdık. Nuriye Hanım'ın masa lambası ve parlak zihni galaksiyle yarışıyor!'"),
    ("🍎", "Amasya'nın Misket Elması", "Dalında kızaran Amasya elması utançla yaprakların arkasına saklandı: 'Benim yarım kırmızı yarım sarı, ama Nuriye Hanım'ın TYT hazırlığı eksiksiz, tas tamam! Benim tadım bile onun zaferi yanında ekşi kalır.'"),
    ("🐐", "Ankara'nın İnatçı Tiftik Keçisi", "Bozkırın dik yamaçlarında gezen keçi meledi: 'Benim inadım Anadolu'da meşhurdur sanırdım, ta ki Nuriye Hanım'ın anlamadığı konunun üstüne gidişini görene kadar. Ablamdaki bu entelektüel inat, taşı bile deler!'"),
    ("🌊", "Boğazın Asi Lüferi", "İstanbul Boğazı'nın hırçın lüferi akıntıya kafa tutarken mırıldandı: 'Sert akıntıya karşı durmak yürek ister! Nuriye Hanım o sınav stresinin akıntısını zekasıyla öyle bir yardı ki, bana bile dalga dalga ders verdi!'"),
    ("🌿", "Karadeniz'in İnatçı Çay Filizi", "Dik yamaçlarda yağmur çamur dinlemeden açan filiz gülümsedi: 'Siste ve fırtınada yeşermek maharet ister. Ama Nuriye Hanım'ın şu masa başında dirsek çürüterek yeşerttiği umutlar, benim en taze yaprağımdan daha destansı!'" )
]

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
    <div style="text-align: center; padding-bottom: 10px;">
        <div style="font-size: 50px; margin-bottom: 12px;">{emoji}</div>
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 700; color: #5a4a3a; margin-bottom: 12px;">{baslik}</div>
        <div style="font-family: 'Poppins', sans-serif; font-size: 13px; color: #5a4a3a; line-height: 1.6;">
            {mesaj}
            <br><br>
            <strong>Mutedra Co.</strong> tarafından<br>
            <strong>Nuriye Hanımın</strong> şahsı için özel kodlanmıştır.
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 YOLCULUĞA BAŞLA", use_container_width=True):
        st.session_state.onboarding_seen = True
        st.rerun()

if not st.session_state.onboarding_seen:
    show_onboarding()

st.markdown('<div class="hud-wrap"><div class="hud-title">🏔️ Nuriye Hanım Şahsına TYT Çalışma Yolculuğu</div><div class="hud-sub">Anadolu\'da Bir Öğrenme Serüveni</div></div>', unsafe_allow_html=True)

secilen_ders = st.selectbox("DERS", tum_dersler, index=tum_dersler.index(st.session_state.current_ders), key="ders_sel")

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
            <div class="prog-meta"><span>HAP BİLGİ İLERLEMESİ</span><span>{secilen_ders} {idx+1} / {toplam} · %{pct}</span></div>
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
        
        b1, b2, b3 = st.columns(3)
        
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

else:
    if secilen_ders not in mevcut_dersler:
        st.markdown(f'<div class="hap-card"><div class="hap-text" style="color:#8b6f47;">⏳ <b>{secilen_ders}</b> dersi henüz hazırlanmadı.</div></div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

with st.expander("🏔️  ANADOLU'DA YOLCULUGUN HARİTASI"):
    st.markdown("""
**Hoşgeldin Gizemli Yolcu Nuriye. Yolculuğun Haritasını veriyorum:**

Anadolu'da bir öğrenme serüvenine başladın. Her hap bilgiyi okudukça, dağları tırmanıyor, ormanları geçiyor ve kuşları görüyorsun. Bol şans!

🎯 **Başarımlarını Takip Et (1-1000):**
Her 25 hap bilgide bir yeni başarım açılır. Toplam 42 Eşsiz Başarım mevcuttur.
""")

c1, c2 = st.columns([2, 1])
with c1:
    if st.button("🔄 YENİLE & YENİ HİKAYE", key="yenile"):
        st.session_state.daily_story = random.choice(KOMIK_HIKAYELER)
        st.session_state.onboarding_seen = False
        st.cache_data.clear()
        st.rerun()
with c2:
    st.markdown(f"<div style='font-family:Poppins,sans-serif;font-size:9px;color:#7a6a5a;letter-spacing:1px;padding:10px 0;text-align:right;'>MUTEDRA CO.</div>", unsafe_allow_html=True)
