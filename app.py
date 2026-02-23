import streamlit as st
import google.generativeai as genai

# --- 1. SETTING HALAMAN ---
st.set_page_config(page_title="Asisten AI Saya", page_icon="🤖")

# --- 2. KONEKSI KE GOOGLE AI ---
try:
    # Mengambil kunci dari Secrets Streamlit
    kunci = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=kunci)
    
    # Gunakan nama model 'gemini-pro' (paling stabil untuk pemula)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Kunci API belum siap: {e}")

# --- 3. TAMPILAN ---
st.title("🤖 Chatbot AI Saya")
st.info("Tanyakan apa saja, saya akan menjawab menggunakan Google Gemini.")

pesan = st.text_input("Ketik pertanyaan kamu di sini:", placeholder="Contoh: Apa itu internet?")

if st.button("Tanya Sekarang"):
    if pesan:
        with st.spinner("Sabar ya, lagi mikir..."):
            try:
                # Proses tanya ke AI
                respon = model.generate_content(pesan)
                
                # Tampilkan hasil
                st.subheader("Jawaban:")
                st.markdown(f"> {respon.text}")
            except Exception as e:
                st.error(f"Terjadi kendala: {e}")
                st.info("Pastikan API Key di 'Secrets' Streamlit sudah benar.")
    else:
        st.warning("Kolomnya jangan dikosongin ya!")
