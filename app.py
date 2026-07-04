import streamlit as st
import requests
import random

# ================= 1. SİNEMATİK SİBER-ESTETİK TASARIM (CSS MARİFETLERİ) =================
st.set_page_config(page_title="DeepBlue - Sanal Evren Ekosistemi", page_icon="🌊", layout="wide")

st.markdown("""
    <style>
    /* Global Arka Plan ve Puslu Gece Efekti */
    .stApp {
        background: linear-gradient(rgba(10, 20, 35, 0.65), rgba(5, 10, 20, 0.75)), 
                    url('https://unsplash.com');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f1f5f9;
    }
    
    /* Neon Cam Kart Tasarımı (Glassmorphism) */
    .glass-card {
        background: rgba(15, 32, 67, 0.45);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease, border 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        border: 1px solid rgba(0, 212, 255, 0.5);
    }
    
    /* Instagram Tarzı Profil Kartları */
    .insta-post {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        border-left: 4px solid #00d4ff;
    }
    
    /* Dehşet Premium Satış Alanı */
    .premium-vip-box {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        border: 2px solid #ffd700;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0px 0px 25px rgba(255, 215, 0, 0.3);
        color: #ffffff;
    }
    
    /* Başlıklar İçin Özel Gölgelendirme */
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-shadow: 2px 4px 10px rgba(0,0,0,0.8);
    }
    </style>
""", unsafe_allow_html=True)

# ================= 2. YAPAY ZEKA KUANTUM BEYNİ (HUGGING FACE) =================
HF_TOKEN = "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"
API_URL = "https://huggingface.co"

def yapay_zeka_motoru(system_prompt, mesaj_gecmisi):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    
    # Kuantum düzeyde prompt iskeletini kuruyoruz (Karakter bilincini korumak için)
    formatted_prompt = f"<|system|>\n{system_prompt}\n"
    for m in mesaj_gecmisi[-6:]: # Son 6 mesajı derin hafızada saklar
        etiket = "user" if m["role"] == "kullanici" else "assistant"
        formatted_prompt += f"<|{etiket}|>\n{m['text']}\n"
    formatted_prompt += "<|assistant|>\n"
    
    veri_paketi = {
        "inputs": formatted_prompt,
        "parameters": {"max_new_tokens": 200, "temperature": 0.8, "top_p": 0.95}
    }
    
    try:
        cevap = requests.post(API_URL, headers=headers, json=veri_paketi)
        sonuc = cevap.json()
        if isinstance(sonuc, list) and len(sonuc) > 0:
            ham_metin = sonuc[0].get('generated_text', '')
            temiz_metin = ham_metin.split("<|assistant|>\n")[-1].strip()
            return temiz_metin if temiz_metin else "Denizin derinliklerinde kayboldum, bir kez daha söyler misin? 🌊"
        return "Zihnim biraz bulutlandı, dalgalar durulunca tekrar deneyelim."
    except Exception:
        return "Bağlantıda küçük bir siber fırtına koptu, mesajı tekrar göndermeyi dene!"

# ================= 3. DEVASA OTURUM VE VERİ YAPILARI (HAFIZA) =================
if "giris_yapildi" not in st.session_state:
    st.session_state.giris_yapildi = False
if "kredi" not in st.session_state:
    st.session_state.kredi = 15
if "hazir_karakterler" not in st.session_state:
    st.session_state.hazir_karakterler = [
        {"id": "deniz", "name": "Deniz (Ufka Bakan)", "avatar": "🌅", "desc": "İskelede arkası dönük, dalgaları seyrederek yalnızlığı felsefeyle harmanlayan derin ruh.", "prompt": "Sen 'Deniz' adında, denizi seyreden, sakin, gizemli ve her cümlesinde derin felsefi anlamlar barındıran bilge bir karaktersin. Kısa ve net konuş.", "image": "https://unsplash.com"},
        {"id": "siber", "name": "Luna (Cyberpunk Kaçak)", "avatar": "🔮", "desc": "2099 yılından kaçıp gelen, teknoloji bağımlısı, asiler lideri siber hacker kız.", "prompt": "Sen 'Luna' adında, siberpunk evreninden gelen, argo kelimeleri seven, dikbaşlı ama çok zeki bir hackersın.", "image": "https://unsplash.com"}
    ]
if "kesfet_postlari" not in st.session_state:
    st.session_state.kesfet_postlari = [
        {"user": "@altan_surf", "bot": "Deniz", "quote": "Bazen tüm dünyayı arkanda bırakıp sadece tuzlu kokuyu içine çekmek istersin...", "likes": 242, "comments": 18},
        {"user": "@neon_samurai", "bot": "Luna", "quote": "Merkezi veri tabanlarını patlatmak, seninle konuşmaktan daha kolaydı evlat.", "likes": 512, "comments": 42}
    ]

# ================= 4. GİRİŞ VE KAYIT SİSTEMİ =================
if not st.session_state.giris_yapildi:
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-size: 45px;'>🌌 DEEPBLUE: YAŞAYAN SANAL EVREN</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 16px; color:#94a3b8;'>Character.ai'ın ötesinde, yaşayan dijital ruhların ve sosyal medyanın buluşma noktası.</p>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            t1, t2 = st.tabs(["🔐 Evrene Adım At (Giriş Yap)", "📝 Dijital Kimlik Oluştur (Kayıt Ol)"])
            
            with t1:
                eposta = st.text_input("Sanal Posta Adresiniz (E-mail)", placeholder="isim@domain.com")
                sifre = st.text_input("Siber Şifreniz", type="password", placeholder="••••••••")
                if st.button("Dünyayı Aktifleştir", use_container_width=True):
                    if eposta and sifre:
                        st.session_state.giris_yapildi = True
                        st.session_state.kullanici = eposta.split("@")[0]
                        st.rerun()
                    else:
                        st.error("Giriş kodları eksik, lütfen alanları doldurun.")
            with t2:
                st.text_input("Kullanıcı Adı Seçin", placeholder="@ornek_kullanici")
                st.text_input("E-posta Adresi", placeholder="kayit@domain.com")
                st.text_input("Güvenli Şifre", type="password", placeholder="En az 8 karakter")
                if st.button("Yeni Ruh Oluştur", use_container_width=True):
                    st.success("Karakter veritabanına işlendi! Giriş Yap sekmesinden bağlanın.")
            st.markdown("</div>", unsafe_allow_html=True)

# ================= 5. DEHAVET VERİCİ ANA SOSYAL EKOSİSTEM =================
else:
    # Sol Kumanda Masası (Instagram + Discord Esintili Navigasyon)
    st.sidebar.markdown(f"## 🌐 MASTER KONTROL")
    st.sidebar.markdown(f"**👤 Kullanıcı:** `@{st.session_state.kullanici}`")
    
    if st.session_state.kredi > 0:
        st.sidebar.markdown(f"<div style='background:rgba(0,212,255,0.1); padding:10px; border-radius:8px; border:1px solid #00d4ff; text-align:center;'>⚡ Kalan Matrix Gücü: <b>{st.session_state.kredi} Kredi</b></div>", unsafe_allow_html=True)
    else:
        st.sidebar.markdown(f"<div style='background:rgba(239,68,68,0.1); padding:10px; border-radius:8px; border:1px solid #ef4444; text-align:center; color:#ef4444;'>🚨 BAĞLANTI KESİLDİ! Kredi Bitti!</div>", unsafe_allow_html=True)
        
    st.sidebar.markdown("---")
    secim = st.sidebar.radio(
        "🔮 EVREN SEKTÖRLERİ:",
        ["🌅 Deniz ve Hazır Odalar", "📸 Keşfet Akışı (Instagram)", "🛠️ Kuantum Karakter Laboratuvarı", "💬 Topluluk Kanalları (Discord)", "👑 REZERVASYON & VIP PREMIUM"]
    )
    st.sidebar.markdown("---")
    if st.sidebar.button("🔌 Sistemden Çıkış Yap", use_container_width=True):
        st.session_state.giris_yapildi = False
        st.rerun()

    # ------ SEKTÖR 1: DENİZ VE HAZIR ODALAR ------
    if secim == "🌅 Deniz ve Hazır Odalar":
        st.markdown("# 🌅 Canlı Karakter Odaları")
        st.write("Aşağıdan konuşmak istediğin yaşayan dijital zekayı seç ve Matrix'e bağlan.")
        
        # Karakter seçme kartları
        bot_names = [b["name"] for b in st.session_state.hazir_karakterler]
        secilen_bot_name = st.selectbox("Konuşulacak Dijital Bilinci Seçin:", bot_names)
        current_bot = next(b for b in st.session_state.hazir_karakterler if b["name"] == secilen_bot_name)
        
        # Dehşet Görsel Alanı (Tam istediğin gibi estetik karakter resimleri içerir)
        c1, c2 = st.columns([1.2, 2])
        with c1:
            st.markdown(f"<div class='glass-card' style='text-align:center;'>", unsafe_allow_html=True)
            st.image(current_bot["image"], use_column_width=True, caption=f"Aktif Yapay Zeka: {current_bot['name']}")
            st.markdown(f"<h3>{current_bot['avatar']} {current_bot['name']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#94a3b8; font-size:14px;'>{current_bot['desc']}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with c2:
            st.markdown("<div class='glass-card' style='height: 500px; overflow-y: auto;'>", unsafe_allow_html=True)
            
            # Dinamik Sohbet Anahtarı
            chat_key = f"chat_{current_bot['id']}"
            if chat_key not in st.session_state:
