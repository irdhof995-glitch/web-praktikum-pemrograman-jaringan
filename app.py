import streamlit as st
import google.generativeai as genai

# 1. Ambil Kunci Rahasia
kunci_rahasia = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=kunci_rahasia)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Tampilan Web
st.title("🤖 Asisten AI Saya")
st.write("Halo! Silahkan ketik pertanyaanmu di bawah ini.")

# Input teks dari user
pesan = st.text_input("Pertanyaan kamu:", placeholder="Contoh: Apa itu kecerdasan buatan?")

# 3. Logika: Kirim HANYA jika tombol diklik
if st.button("Tanya Sekarang"):
    if pesan: # Cek apakah pesan tidak kosong
        with st.spinner("Sedang memikirkan jawaban..."):
            try:
                respon = model.generate_content(pesan)
                st.subheader("Jawaban AI:")
                st.write(respon.text)
            except Exception as e:
                st.error(f"Aduh, ada masalah teknis: {e}")
    else:
        # Jika user klik tombol tapi belum ngetik apa-apa
        st.warning("Eits, ketik dulu pertanyaannya ya!")
