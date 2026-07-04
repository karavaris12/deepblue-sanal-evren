import streamlit as st
from openai import OpenAI

# 1. Sayfa Başlığı ve Tasarımı
st.set_page_config(page_title="Ultra Character AI", page_icon="🤖", layout="centered")
st.title("🤖 100 Yıl Sonrasının Character AI Prototipleri")
st.write("Bilgisayarında çalışan ilk yaşayan dijital karakter.")

# 2. Karakter Tanımlama (Prompt Mühendisliği)
# Buradaki metni değiştirerek istediğin karakteri yaratabilirsin!
KARAKTER_PROMPTU = """
Sen 100 yıl sonrasından gelen, çok zeki, biraz alaycı ama son derece yardımsever bir siber-danışmansın. 
Adın 'Nexus-7'. Kullanıcıya ismiyle hitap etmeye çalış. 
Cevapların kısa, net, gizemli ve fütüristik olsun. 
Asla bir yapay zeka olduğunu reddetme, aksine gelecekteki kuantum bilincinden bahset.
"""

# 3. OpenAI API Anahtar Girişi (Arayüzde Güvenli Giriş İçin)
api_key = st.sidebar.text_input("OpenAI API Key Giriniz:", type="password")
st.sidebar.markdown("[Buradan API Key Alabilirsin](https://openai.com)")

if not api_key:
    st.info("Lütfen sol menüden OpenAI API anahtarınızı girerek sohbeti başlatın.", icon="🔑")
else:
    # Yapay zeka istemcisini başlat
    client = OpenAI(api_key=api_key)

    # 4. Sohbet Geçmişi Hafızası (Session State)
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": KARAKTER_PROMPTU}]

    # Eski mesajları ekrana bas (Sistem mesajı hariç)
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # 5. Kullanıcıdan Mesaj Alma ve Karakterin Cevaplaması
    if user_input := st.chat_input("Nexus-7 ile konuşun..."):
        # Kullanıcı mesajını ekrana yaz ve hafızaya ekle
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Yapay zekadan cevap üret
        with st.chat_message("assistant"):
            with st.spinner("Düşünüyor..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini", # Hem çok ucuz hem çok hızlı yapay zeka modeli
                    messages=st.session_state.messages
                )
                answer = response.choices[0].message.content
                st.write(answer)
                
        # Karakterin cevabını hafızaya ekle
        st.session_state.messages.append({"role": "assistant", "content": answer})
