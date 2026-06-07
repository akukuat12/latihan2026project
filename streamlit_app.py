import streamlit as st
import base64
import pandas as pd
import os

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("background.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Data Ar unsur
data_ar = {
    "H": 1,
    "C": 12,
    "N": 14,
    "O": 16,
    "Na": 23,
    "Mg": 24,
    "Al": 27,
    "Si": 28,
    "P": 31,
    "S": 32,
    "Cl": 35.5,
    "K": 39,
    "Ca": 40,
    "Cr": 52,
    "Mn": 55,
    "Fe": 56,
    "Co": 59,
    "Ni": 59,
    "Cu": 63.5,
    "Zn": 65,
    "Br": 80,
    "Ag": 108,
    "I": 127,
    "Ba": 137,
    "Au": 197,
    "Hg": 201,
    "Pb": 207
}

st.set_page_config(page_title="ChemBuddy", page_icon="🧪")

st.sidebar.title("🧪 ChemBuddy")
st.sidebar.markdown("## Pilih Menu")

if st.sidebar.button("🏠 Beranda"):
    st.session_state.menu = "Beranda"

if st.sidebar.button("⚗️ Normalitas"):
    st.session_state.menu = "Normalitas"

if st.sidebar.button("🧫 Molaritas"):
    st.session_state.menu = "Molaritas"

if st.sidebar.button("🧪 BE"):
    st.session_state.menu = "BE"

if st.sidebar.button("⚖️ BM"):
    st.session_state.menu = "BM"

if st.sidebar.button("🧬 Ar"):
    st.session_state.menu = "Ar"

if st.sidebar.button("🌡️ Konversi Suhu"):
    st.session_state.menu = "Konversi Suhu"

if st.sidebar.button("🫧 PPM"):
    st.session_state.menu = "PPM"

if st.sidebar.button("ℹ️ About Us"):
    st.session_state.menu = "About Us"

menu = st.session_state.get("menu", "Beranda")

if menu == "Beranda":
    st.markdown("""
# Selamat Datang di ChemBuddy 🧪

**ChemBuddy** adalah platform pembelajaran yang dirancang untuk membantu mahasiswa, khususnya tingkat pertama, dalam memahami dan menyelesaikan perhitungan dasar pada mata kuliah **Kimia Dasar**,**Titrimetri**,dan **Fisika Dasar**.

Melalui ChemBuddy, pengguna dapat dengan mudah melakukan berbagai konversi dan perhitungan, seperti:

- Konversi Suhu
- Atom relatif (Ar)
- Berat Molekul (BM)
- Berat Ekivalen (BE)
- Normalitas (N)
- Molaritas (M)
- Parts Per Million (PPM)

Mata kuliah Kimia Dasar,Titrimetri, dan Fisika Dasar sering menjadi tantangan bagi mahasiswa baru karena banyaknya konsep dan perhitungan yang harus dipahami. Tidak sedikit mahasiswa yang harus mengulang mata kuliah tersebut akibat kesulitan dalam memahami materi dasar. Oleh karena itu, ChemBuddy hadir sebagai solusi praktis untuk membantu proses belajar menjadi lebih mudah, cepat, dan efisien.

Dengan fitur yang sederhana dan mudah digunakan, ChemBuddy diharapkan dapat menjadi teman belajar yang membantu mahasiswa meningkatkan pemahaman konsep serta mengurangi kesalahan dalam perhitungan.

> **Belajar lebih mudah, hitung lebih cepat, bersama ChemBuddy. 🧪✨**
""")

elif menu == "Normalitas":
    st.subheader("⚖️ Normalitas (N)")

    st.write("""
Normalitas adalah konsentrasi larutan yang menunjukkan jumlah ekuivalen zat terlarut dalam setiap liter larutan. Normalitas banyak digunakan dalam titrasi asam-basa, reaksi redoks, dan analisis kimia yang melibatkan perpindahan ion atau elektron.

Satuan normalitas adalah ekuivalen per liter (N) atau grek/L.

Contoh:

Massa zat = 4,9 gram

BE = 49 g/grek

Volume = 100 mL = 0,1 L

""")
    
    st.latex(r'''
N = \frac{4.9}{49 \times 0.1}
''')

    st.latex(r'''
N = 1\ \text{grek/L}
''')
    
    st.markdown("**Rumus Normalitas:**")

    st.latex(r'''
N = \frac{gram}{BE \times V(L)}
''')

    st.markdown("**Hubungan Normalitas dan Molaritas:**")

    st.latex(r'''
N = M \times a
''')

    st.write("""
Keterangan:

- N = Normalitas
- M = Molaritas
- a = Faktor ekuivalen
- BE = Berat Ekivalen
- V = Volume larutan (L)
""")

    gram = st.number_input("Massa zat (gram)", min_value=0.0)
    be = st.number_input("Berat Ekivalen (BE)", min_value=0.0)
    volume = st.number_input("Volume larutan (mL)", min_value=0.0)

    if st.button("Hitung Normalitas"):
        hasil = (gram / be) / (volume / 1000)
        st.success(f"Normalitas = {hasil:.4f} grek/L")

elif menu == "Molaritas":

    st.subheader("🧪 Molaritas (M)")

    st.write("""
Molaritas adalah konsentrasi larutan yang menyatakan jumlah mol zat terlarut dalam setiap liter larutan. Molaritas sangat sering digunakan dalam kimia untuk membuat larutan standar, menghitung konsentrasi reagen, dan melakukan perhitungan stoikiometri reaksi.

Satuan molaritas adalah mol/L atau M (molar).

Contoh:

Massa NaCl = 5,85 gram

BM NaCl = 58,5 g/mol

Volume = 500 mL = 0,5 L

""")

    st.latex(r'''
M = \frac{5.85\ g}{58.5\ g/mol \times 0.5\ L}
= 0.2\ mol/L
''')
    
    st.markdown("**Rumus Molaritas:**")
    
    st.markdown("**Jika jumlah mol diperoleh dari massa zat:**")

    st.latex(r'''
n = \frac{massa}{BM}
''')

    st.latex(r'''
M = \frac{massa}{BM \times V}
''')

    st.write("""
Keterangan:

- M = Molaritas (mol/L)
- n = Jumlah mol zat
- BM = Berat Molekul (g/mol)
- V = Volume larutan (L)


""")

    gram = st.number_input("Massa zat (gram)", min_value=0.0)
    bm = st.number_input("Berat Molekul (BM)", min_value=0.0)
    volume = st.number_input("Volume larutan (mL)", min_value=0.0)

    if st.button("Hitung Molaritas"):
        hasil = (gram / bm) / (volume / 1000)
        st.success(f"Molaritas = {hasil:.4f} mol/L")

elif menu == "BE":
    st.subheader("🧪 Berat Ekivalen (BE)")
    st.write("""Berat Ekivalen (BE) adalah massa suatu zat yang setara dengan satu ekuivalen dalam suatu reaksi kimia. BE digunakan dalam perhitungan normalitas, titrasi, serta analisis reaksi asam-basa dan reaksi redoks.

Rumus:

BE = BM / a

dengan:
- BE = Berat Ekivalen
- BM = Berat Molekul
- a = Faktor ekuivalen (valensi)

Satuan Berat Ekivalen adalah gram per ekuivalen (g/ekuivalen).

Contoh:

H₂SO₄

BM = 98 g/mol

a = 2

""")

    st.latex(r'''
BE = \frac{98}{2}
= 49\ \text{g/ekuivalen}
''')
    
    jumlah_unsur = st.number_input(
        "Jumlah jenis unsur",
        min_value=1,
        max_value=5,
        value=2,
        key="be_jumlah"
    )

    bm_total = 0

    for i in range(jumlah_unsur):
        col1, col2 = st.columns(2)

        with col1:
            unsur = st.selectbox(
                f"Unsur {i+1}",
                list(data_ar.keys()),
                key=f"be_unsur_{i}"
            )

        with col2:
            atom = st.number_input(
                f"Jumlah atom {i+1}",
                min_value=1,
                step=1,
                key=f"be_atom_{i}"
            )

        bm_total += data_ar[unsur] * atom

    valensi = st.number_input(
        "Valensi",
        min_value=1,
        value=1
    )

    if st.button("Hitung BE"):
        be = bm_total / valensi
        st.success(f"BM = {bm_total:.2f} g/mol")
        st.success(f"BE = {be:.2f} g/grek")
    
elif menu == "BM":

    st.subheader("⚖️ Berat Molekul (BM)")

    st.write("""
Berat Molekul atau Massa Molekul Relatif (Mr) merupakan jumlah massa atom relatif seluruh atom yang menyusun suatu molekul. BM digunakan untuk menghitung massa zat, jumlah mol, molaritas, dan berbagai perhitungan stoikiometri.

Rumus:
BM = Σ(Ar × jumlah atom)

Contoh:

H₂O = (2 × 1) + (1 × 16) = 18 g/mol

NaCl = 23 + 35,5 = 58,5 g/mol
""")

    jumlah_unsur = st.number_input(
        "Jumlah jenis unsur",
        min_value=1,
        max_value=5,
        value=2,
        key="bm_jumlah"
    )

    total_bm = 0

    for i in range(jumlah_unsur):
        col1, col2 = st.columns(2)

        with col1:
            unsur = st.selectbox(
                f"Unsur {i+1}",
                list(data_ar.keys()),
                key=f"bm_unsur_{i}"
            )

        with col2:
            atom = st.number_input(
                f"Jumlah atom {i+1}",
                min_value=1,
                step=1,
                key=f"bm_atom_{i}"
            )

        total_bm += data_ar[unsur] * atom

    if st.button("Hitung BM"):
        st.success(f"BM = {total_bm:.2f} g/mol")

elif menu == "Ar":
    st.subheader("🧬 Atom Relatif (Ar)")

    st.write("""Atom Relatif (Ar) adalah massa rata-rata suatu atom dibandingkan dengan 1/12 massa atom karbon-12. Ar menjadi dasar dalam perhitungan BM, Mr, mol, dan stoikiometri reaksi kimia. Contohnya, Ar hidrogen adalah 1 dan Ar oksigen adalah 16. Ar tidak memiliki satuan karena merupakan nilai perbandingan relatif.Nilai Ar diperoleh dari tabel periodik unsur dan digunakan sebagai dasar dalam perhitungan massa molekul suatu senyawa""")
    unsur = st.selectbox("Pilih unsur", list(data_ar.keys()))
    st.info(f"Ar {unsur} = {data_ar[unsur]}")

elif menu == "Konversi Suhu":

    st.subheader("🌡️ Suhu dan Skala Suhu")

    st.write("""
Suhu adalah besaran yang menunjukkan tingkat panas atau dingin suatu benda. Dalam ilmu kimia dan fisika terdapat beberapa skala suhu, yaitu Celsius (°C) yang umum digunakan sehari-hari, Kelvin (K) yang digunakan dalam perhitungan ilmiah karena merupakan skala absolut, Fahrenheit (°F) yang banyak digunakan di Amerika Serikat, dan Reamur (°R) yang kini jarang digunakan.

Suhu berperan penting dalam mengendalikan laju reaksi kimia, menentukan kondisi praktikum laboratorium, menghitung sifat gas, serta berbagai proses industri.

Satuan suhu yang digunakan bergantung pada skalanya, yaitu °C, K, °F, dan °R.

Rumus Konversi Suhu:""")

    st.write("**Rumus Konversi Suhu:**")

    st.markdown("**Celsius (°C) → Fahrenheit (°F)**")
    st.latex(r'''
    ^\circ F = \frac{9}{5}(^\circ C) + 32
    ''')
    
    st.markdown("**Celsius (°C) → Kelvin (K)**")
    st.latex(r'''
    K = ^\circ C + 273.15
    ''')
    
    st.markdown("**Celsius (°C) → Reamur (°R)**")
    st.latex(r'''
    ^\circ R = \frac{4}{5}(^\circ C)
    ''')
    
    st.markdown("**Fahrenheit (°F) → Celsius (°C)**")
    st.latex(r'''
    ^\circ C = \frac{5}{9}(^\circ F - 32)
    ''')
    
    st.markdown("**Fahrenheit (°F) → Kelvin (K)**")
    st.latex(r'''
    K = \frac{5}{9}(^\circ F - 32) + 273.15
    ''')
    
    st.markdown("**Fahrenheit (°F) → Reamur (°R)**")
    st.latex(r'''
    ^\circ R = \frac{4}{9}(^\circ F - 32)
    ''')
    
    st.markdown("**Kelvin (K) → Celsius (°C)**")
    st.latex(r'''
    ^\circ C = K - 273.15
    ''')
    
    st.markdown("**Kelvin (K) → Fahrenheit (°F)**")
    st.latex(r'''
    ^\circ F = \frac{9}{5}(K - 273.15) + 32
    ''')
    
    st.markdown("**Kelvin (K) → Reamur (°R)**")
    st.latex(r'''
    ^\circ R = \frac{4}{5}(K - 273.15)
    ''')
    
    st.markdown("**Reamur (°R) → Celsius (°C)**")
    st.latex(r'''
    ^\circ C = \frac{5}{4}(^\circ R)
    ''')
    
    st.markdown("**Reamur (°R) → Fahrenheit (°F)**")
    st.latex(r'''
    ^\circ F = \frac{9}{4}(^\circ R) + 32
    ''')
    
    st.markdown("**Reamur (°R) → Kelvin (K)**")
    st.latex(r'''
    K = \frac{5}{4}(^\circ R) + 273.15
    ''')
    
    jenis = st.selectbox(
        
        "Konversi",
        [
            "Celcius ke Fahrenheit",
            "Celcius ke Kelvin",
            "Celcius ke Reamur",
    
            "Fahrenheit ke Celcius",
            "Fahrenheit ke Kelvin",
            "Fahrenheit ke Reamur",
    
            "Kelvin ke Celcius",
            "Kelvin ke Fahrenheit",
            "Kelvin ke Reamur",
    
            "Reamur ke Celcius",
            "Reamur ke Fahrenheit",
            "Reamur ke Kelvin"
        ]
    )
    
    suhu = st.number_input("Masukkan suhu")
    
    if jenis == "Celcius ke Fahrenheit":
            hasil = (suhu * 9/5) + 32
            satuan = "°F"
    
    elif jenis == "Celcius ke Kelvin":
            hasil = suhu + 273.15
            satuan = "K"
    
    elif jenis == "Celcius ke Reamur":
            hasil = suhu * 4/5
            satuan = "°R"
    
    elif jenis == "Fahrenheit ke Celcius":
            hasil = (suhu - 32) * 5/9
            satuan = "°C"
    
    elif jenis == "Fahrenheit ke Kelvin":
            hasil = ((suhu - 32) * 5/9) + 273.15
            satuan = "K"
    
    elif jenis == "Fahrenheit ke Reamur":
            hasil = (suhu - 32) * 4/9
            satuan = "°R"
    
    elif jenis == "Kelvin ke Celcius":
            hasil = suhu - 273.15
            satuan = "°C"
    
    elif jenis == "Kelvin ke Fahrenheit":
            hasil = ((suhu - 273.15) * 9/5) + 32
            satuan = "°F"
    
    elif jenis == "Kelvin ke Reamur":
            hasil = (suhu - 273.15) * 4/5
            satuan = "°R"
    
    elif jenis == "Reamur ke Celcius":
            hasil = suhu * 5/4
            satuan = "°C"
    
    elif jenis == "Reamur ke Fahrenheit":
            hasil = (suhu * 9/4) + 32
            satuan = "°F"
    
    elif jenis == "Reamur ke Kelvin":
            hasil = (suhu * 5/4) + 273.15
            satuan = "K"

    if st.button("Konversi"):
            st.success(f"Hasil = {hasil:.2f} {satuan}")

elif menu == "PPM":
    st.subheader("🫧 Parts Per Million (PPM)")

    st.write("""
PPM atau Parts Per Million adalah satuan konsentrasi yang menyatakan jumlah bagian zat dalam satu juta bagian campuran. PPM biasanya digunakan untuk mengukur konsentrasi zat yang sangat kecil, seperti polutan dalam air, udara, tanah, atau kandungan logam berat.

Pada larutan air:

1 ppm ≈ 1 mg/L

Satuan yang digunakan adalah ppm.

Rumus:

PPM = massa zat terlarut (mg) / volume larutan (L)

Contoh:

Massa zat = 50 mg

Volume larutan = 2 L

PPM = 50 / 2 = 25 mg/L
""")

    massa = st.number_input(
        "Massa zat terlarut (mg)",
        min_value=0.0
    )

    volume = st.number_input(
        "Volume larutan (L)",
        min_value=0.0
    )

    if st.button("Hitung PPM"):
        hasil = massa / volume
        st.success(f"PPM = {hasil:.4f} mg/L")

elif menu == "About Us":
    st.header("Tentang ChemBuddy")
    st.write("""
    Kami adalah tim pengembang ChemBuddy, sebuah platform edukasi yang dibuat untuk membantu mahasiswa dalam memahami dan menyelesaikan berbagai perhitungan dasar pada mata kuliah Kimia Dasar, Titimetri dan Fisika Dasar.ChemBuddy hadir sebagai solusi praktis bagi mahasiswa, khususnya tingkat pertama, yang sering menghadapi kesulitan dalam melakukan konversi dan perhitungan kimia. Dengan menyediakan fitur konversi suhu, Berat Molekul (BM), Berat Ekivalen (BE), Molaritas, Normalitas, dan PPM, kami berharap dapat membantu proses belajar menjadi lebih efektif dan efisien.Website ini dikembangkan sebagai bentuk kontribusi kami dalam memanfaatkan teknologi untuk mendukung pembelajaran sains yang lebih mudah diakses dan dipahami """)

    st.write("Tim Pengembang ChemBuddy:")
    st.write("""
    1. *Asyifa Fadilla* (2460335)
    2. *Muhamad Daffa Alfath* (2460425)
    3. *Muhammad Al Fariz* (2460425)
    4. *Nadifah Adya Anggita* (2460449)
    5. *Ramdan Abdul Azis* (2460490)

    Kami percaya bahwa pembelajaran akan menjadi lebih menyenangkan ketika didukung oleh alat yang tepat. Oleh karena itu, melalui ChemBuddy kami berkomitmen untuk menghadirkan platform yang sederhana, bermanfaat, dan mudah digunakan oleh seluruh mahasiswa.

    >ChemBuddy — Your Smart Chemistry Learning Companion.🧪✨
        """)
    
    if os.path.exists("feedback.csv"):
        
        df = pd.read_csv("feedback.csv")
        rata_rata = df["Rating"].mean()

    st.metric(
    "⭐ Rata-rata Rating",
    f"{rata_rata:.1f}/5"
    )
    
    
        
   

st.caption("Bagaimana pengalaman Anda menggunakan ChemBuddy?")

rating = st.feedback("stars")

if rating is not None:

    rating_bintang = rating + 1

    st.success(f"Rating yang diberikan: {rating_bintang} ⭐")

    data = pd.DataFrame({
        "Rating": [rating_bintang]
    })

    if os.path.exists("feedback.csv"):
        data.to_csv(
            "feedback.csv",
            mode="a",
            header=False,
            index=False
        )
    else:
        data.to_csv(
            "feedback.csv",
            index=False
        )

st.markdown("""
<style>

/* Warna tombol menu sidebar */
[data-testid="stSidebar"] .stButton button {
    background-color: #003152; /* warna tombol */
    color: white;                
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Tombol menu sidebar */
[data-testid="stSidebar"] .stButton button {
    background-color: #588BAE !important;
    color: white !important;
}

/* Hover */
[data-testid="stSidebar"] .stButton button:hover {
    background-color: #003152 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #123456;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div[data-baseweb="input"] > div {
    background-color: #588BAE;
}

div[data-baseweb="input"] input {
    color:white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Kotak selectbox */
div[data-baseweb="select"] > div {
    background-color: #588BAE;
    color: white;
}

/* Teks di dalam selectbox */
div[data-baseweb="select"] span {
    color: white;
}
</style>
""", unsafe_allow_html=True)
      
