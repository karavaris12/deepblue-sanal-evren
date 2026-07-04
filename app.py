import streamlit as st

# 1. Gelişmiş Sayfa Tasarımı ve Genişliği
st.set_page_config(page_title="DeepBlue - Sanal Evren", page_icon="🌊", layout="wide")

# CSS ile Arka Plana Deniz Manzarası ve Sosyal Medya Kart Tasarımı
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(10, 25, 47, 0.5), rgba(10, 25, 47, 0.4)), 
                    url('https://unsplash.com');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .premium-box {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        padding: 20px;
        border-radius: 12px;
        color: #1e293b;
        font-weight: bold;
        text-align: center;
        margin-bottom: 15px;
    }
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
    }
    </style>
""", unsafe_allow_html=True)

# 2. Oturum ve Kredi Durumu Yönetimi
if "giris_yapildi" not in st.session_state:
    st.session_state.giris_yapildi = False
if "kredi" not in st.session_state:
    st.session_state.kredi = 15 # Millet ilk girdiğinde 15 kredi ile başlar
if "ozel_karakterler" not in st.session_state:
    st.session_state.ozel_karakterler = []

# ================= GİRİŞ VE KAYIT EKRANI =================
if not st.session_state.giris_yapildi:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align: center;'>🌊 DeepBlue Sosyal Ağı</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-size:16px;'>Kendi karakterini yarat, gruplara katıl, denize karşı sosyalleş.</h3>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🔐 Giriş Yap", "📝 Hızlı Kayıt Ol"])
        with tab1:
            giris_eposta = st.text_input("E-posta Adresi", key="g_email")
            giris_sifre = st.text_input("Şifre", type="password", key="g_pass")
            if st.button("Sanal Dünyaya Giriş Yap", use_container_width=True):
                if giris_eposta and giris_sifre:
                    st.session_state.giris_yapildi = True
                    st.session_state.kullanici = giris_eposta.split("@")[0]
                    st.rerun()
                else:
                    st.error("Lütfen tüm alanları doldurun.")
        with tab2:
            st.text_input("Kullanıcı Adı", key="k_ad")
            st.text_input("E-posta Adresi", key="k_email")
            st.text_input("Şifre (En az 6 karakter)", type="password", key="k_pass")
            if st.button("Hesabımı Oluştur ve Başla", use_container_width=True):
                st.success("Kayıt başarılı! Giriş Yap sekmesinden hesabına bağlanabilirsin.")

# ================= ANA PANEL (GİRİŞTEN SONRA) =================
else:
    # Sol Menü (Instagram & Discord Esintili Gelişmiş Navigasyon)
    st.sidebar.markdown(f"### 👋 Hoş Geldin, @{st.session_state.kullanici}")
    
    # Canlı Kredi Göstergesi
    if st.session_state.kredi > 0:
        st.sidebar.info(f"⚡ Kalan Ücretsiz Mesaj: {st.session_state.kredi} Kredi")
    else:
        st.sidebar.error("🚨 Krediniz Bitti! Konuşmaya devam etmek için Premium alın.")
        
    menu = st.sidebar.radio(
        "📍 Platform Menüsü:",
        ["🌅 Deniz Manzaralı Oda", "🛠️ Kendi Karakterini Yarat", "💬 Sohbet Grupları", "🎮 Oyun Alanı", "💳 Ödeme & Premium VIP"]
    )
    
    if st.sidebar.button("Güvenli Çıkış"):
        st.session_state.giris_yapildi = False
        st.rerun()

    # --- 1. ODANIN İÇERİĞİ ---
    if menu == "🌅 Deniz Manzaralı Oda":
        st.markdown("## 🌅 İskelede Ufka Bakan Karakter: 'Deniz'")
        
        # Hayal ettiğin denize bakan karakter tasarımı için Unsplash'ten fütüristik/estetik görsel
        st.image("https://unsplash.com", 
                 caption="Deniz, iskelede arkası dönük şekilde dalgaları seyrediyor...", width=500)
        
        # Sohbet Geçmişi
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [{"role": "Deniz", "text": "Selam... Dalgaların sesini duyuyor musun? İnsanlar buraya hep bir şeylerden kaçmak için gelir. Senin hikayen ne?"}]
            
        for msg in st.session_state.chat_history:
            st.chat_message("assistant" if msg["role"] == "Deniz" else "user").write(f"**{msg['role']}:** {msg['text']}")
            
        # Mesaj Giriş Kontrolü (15 Kredi Sınırı Mekanizması)
        if st.session_state.kredi > 0:
            if user_msg := st.chat_input("Deniz ile dertleş..."):
                st.session_state.chat_history.append({"role": st.session_state.kullanici, "text": user_msg})
                # Krediyi bir düşür
                st.session_state.kredi -= 1
                # Simüle cevap
                st.session_state.chat_history.append({"role": "Deniz", "text": "Bunu duyduğuma sevindim. Bazen sadece durup denize bakmak tüm sorunları çözer."})
                st.rerun()
        else:
            st.markdown("<div class='premium-box'>⚠️ Ücretsiz Sohbet Sınırına Ulaştınız! Sohbeti kilitlemek zorunda kaldık. Devam etmek için lütfen yan menüden Premium VIP paketine geçin.</div>", unsafe_allow_html=True)

    # --- 2. KENDİ KARAKTERİNİ YARAT PANELİ ---
    elif menu == "🛠️ Kendi Karakterini Yarat":
        st.markdown("## 🛠️ Yapay Zeka Karakter Fabrikası")
        st.write("Kendi benzersiz yapay zeka karakterini tasarla, profilini oluştur ve ekosisteme sal!")
        
        c_name = st.text_input("Karakterin İsmi", placeholder="Örn: Siyah Gözlüklü Yazılımcı")
        c_greeting = st.text_area("İlk Selamlama Cümlesi", placeholder="Örn: Merhaba dostum, bugün hangi kodu patlatıyoruz?")
        c_prompt = st.text_area("Karakterin Kişiliği ve Gizli Talimatları (Prompt)", placeholder="Sen çok havalı, sürekli kahve içen bir yazılımcısın...")
        c_bg = st.selectbox("Arka Plan Manzarası", ["Deniz Sahili", "Siberpunk Şehir", "Dağ Evi", "Gizemli Kütüphane"])
        
        if st.button("🚀 Karakteri Dünyaya Fırlat"):
            if c_name and c_prompt:
                st.session_state.ozel_karakterler.append({"name": c_name, "greet": c_greeting, "bg": c_bg})
                st.success(f"🎉 '{c_name}' başarıyla yaratıldı! Diğer insanlar artık bu karakterle sohbet edebilir.")
            else:
                st.error("Lütfen karakter ismi ve kişilik alanlarını boş bırakmayın.")
                
        if st.session_state.ozel_karakterler:
            st.markdown("### 👥 Yarattığın Canlı Karakterler")
            for char in st.session_state.ozel_karakterler:
                st.info(f"🤖 **{char['name']}** | 📍 Konum: {char['bg']} | İlk Sözü: '{char['greet']}'")

    # --- 3. SOHBET GRUPLARI ---
    elif menu == "💬 Sohbet Grupları":
        st.markdown("## 👥 Topluluk Sahilleri (Instagram & Discord Modeli)")
        st.write("Kullanıcıların kendi aralarında gruplar kurduğu, fotoğraflar paylaştığı akış alanı.")
        st.info("💡 **İpucu:** Kendi grubunu kurmak ve Instagram gibi sınırsız paylaşım yapmak için Premium üye olmalısın.")
        
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("### ☕ #GeceKahvesi Grubu")
            st.write("*Aktif Üye: 1,420 kişi*")
            st.button("Gruba Katıl", key="g1")
        with col_g2:
            st.markdown("### 🛹 #SörfçülerSahili")
            st.write("*Aktif Üye: 810 kişi*")
            st.button("Gruba Katıl", key="g2")

    # --- 4. OYUN ALANI ---
    elif menu == "🎮 Oyun Alanı":
        st.markdown("## 🎮 Çok Oyunculu Sanal Oyun Sahası")
        st.write("Yapay zeka karakterleriyle veya odadaki diğer gerçek insanlarla oynayabileceğin kelime oyunları ve fantezi RPG lobileri çok yakında aktife edilecek!")

    # --- 5. ÖDEME ENTEGRASYONU PANELİ ---
    elif menu == "💳 Ödeme & Premium VIP":
        st.markdown("## 💎 DeepBlue VIP Kulübüne Katıl (Para Kazanma Alanı)")
        st.markdown("<div class='premium-box'>👑 PREMIUM ÜYELİKLE SINIRLARI ORTADAN KALDIRIN</div>", unsafe_allow_html=True)
        
        st.write("Premium Paket Avantajları:")
        st.markdown("- ✨ Sınırsız Mesajlaşma (15 Kredi sınırı kalkar)")
        st.markdown("- 🛠️ Sınırsız Özel Yapay Zeka Karakteri Üretme Yetkisi")
        st.markdown("- 💬 Discord mantığında kendi Sohbet Odalarını/Gruplarını kurma gücü")
        st.markdown("- 👑 Profilinde altın renkli 'Sahil Sakini' onaylı hesap rozeti")
        
        st.markdown("---")
        st.subheader("💳 Güvenli Ödeme Yöntemini Seçin")
        
        fiyat = "99.00 TL / Aylık"
        st.markdown(f"### 💰 Ödenecek Tutar: **{fiyat}**")
        
        tab_pay1, tab_pay2 = st.tabs(["🇹🇷 iyzico (Kredi Kartı)", "🌍 Stripe (Global Ödeme)"])
        
        with tab_pay1:
            st.write("Türkiye'deki tüm banka ve kredi kartlarıyla 3D Secure güvencesiyle ödeyin.")
            # İleride iyzico API'sine bağlanacak olan tetikleyici buton
            if st.button("iyzico ile Güvenli Öde (99 TL)"):
                st.balloons()
                st.success("💳 iyzico Ödeme Sayfasına Yönlendiriliyorsunuz... (Sistem başarıyla tetiklendi, Premium hesabınız aktifleştiriliyor!)")
                st.session_state.kredi = 999999 # Kredi sınırını sonsuz yapıyoruz
                
        with tab_pay2:
            st.write("Yurt dışından katılacak kullanıcılar için uluslararası güvenli ödeme.")
            if st.button("Stripe ile Satın Al ($2.99)"):
                st.success("🌍 Stripe Checkout sayfasına aktarılıyorsunuz...")
