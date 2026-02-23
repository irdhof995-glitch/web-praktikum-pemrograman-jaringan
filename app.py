import streamlit as st
import google.generativeai as genai

# Pastikan nama di Secrets adalah GOOGLE_API_KEY
try:
    kunci_rahasia = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=kunci_rahasia)
    
    # Kita gunakan nama model yang paling stabil
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Gagal memuat API Key: {e}")

st.set_page_config(page_title="Asisten AI Saya")
st.title("🤖 Asisten AI Saya")
st.write("Silahkan ketik pertanyaanmu di bawah ini.")

pesan = st.text_input("Pertanyaan kamu:", placeholder="Contoh: Apa itu kecerdasan buatan?")

if st.button("Tanya Sekarang"):
    if pesan:
        with st.spinner("Sedang memikirkan jawaban..."):
            try:
                # Tambahkan penanganan jika model tidak ditemukan
                respon = model.generate_content(pesan)
                st.subheader("Jawaban AI:")
                st.write(respon.text)
            except Exception as e:
                # Jika masih error 404, coba ganti model ke 'gemini-pro'
                st.error(f"Maaf, ada masalah: {e}")
                st.info("Tips: Pastikan API Key di 'Secrets' sudah benar dan aktif.")
    else:
        st.warning("Ketik dulu pertanyaannya ya!")
