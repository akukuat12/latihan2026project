import streamlit as st

# Warna tema
warna = st.sidebar.selectbox(
    "Pilih Warna Tema",
    ["Biru", "Hijau", "Ungu", "Merah"]
)

if warna == "Biru":
    bg_color = "#D6EAF8"
elif warna == "Hijau":
    bg_color = "#D5F5E3"
elif warna == "Ungu":
    bg_color = "#E8DAEF"
else:
    bg_color = "#FADBD8"

st.markdown(f"""
<style>
.stApp {{
background-color: {bg_color};
}}
</style>
""", unsafe_allow_html=True)
menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Normalitas",
        "Molaritas",
        "BE",
        "BM",
        "Ar",
        "Konversi Suhu",
        "PPM",
        "Materi",
        "Rumus",
        "About Us",
        "Feedback"
    ]
)

elif menu == "Materi":
    st.header("📚 Materi Kimia")

    st.subheader("Normalitas (N)")
    st.write("""
    Normalitas adalah jumlah gram ekivalen zat terlarut
    dalam setiap liter larutan.

    Satuan: N (Normal)
    """)

    st.subheader("Molaritas (M)")
    st.write("""
    Molaritas adalah jumlah mol zat terlarut
    dalam setiap liter larutan.

    Satuan: M (Molar)
    """)
elif menu == "About Us":
    st.header("👨‍🔬 About Us")

    st.write("""
    ChemBuddy merupakan aplikasi kalkulator kimia digital
    yang membantu siswa menghitung:

    - Normalitas
    - Molaritas
    - Berat Molekul
    - Berat Ekivalen
    - PPM
    - Konversi Suhu

    Dibuat untuk mendukung pembelajaran kimia yang lebih mudah dan interaktif.
    """)
elif menu == "Feedback":
    st.header("💬 Feedback")

    nama = st.text_input("Nama")
    saran = st.text_area("Masukkan saran dan kritik")

    if st.button("Kirim Feedback"):
        st.success("Terima kasih atas feedback yang diberikan!")
