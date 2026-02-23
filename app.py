import streamlit as st
import google.generativeai as genai

# Di sini kita bilang: "Tolong ambil kunci dari brankas rahasia"
kunci_rahasia = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=kunci_rahasia)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Aplikasi AI Saya")
pesan = st.text_input("Mau tanya apa hari ini?")

if st.button("Kirim"):
    respon = model.generate_content(pesan)
    st.write(respon.text)