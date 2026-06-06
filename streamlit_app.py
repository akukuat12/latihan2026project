<!DOCTYPE html>
<html lang="id">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>DigiChem</title>

  <style>
    :root {
      --primary-color: #2563eb;
      --primary-hover: #1d4ed8;
      --secondary-color: #1e3a8a;
      --bg-gradient-1: #0f172a;
      --bg-gradient-2: #1e3a8a;
      --text-white: #ffffff;
      --text-light: #cbd5e1;
      --card-bg: rgba(255, 255, 255, 0.95);
      --result-bg: #dbeafe;
      --result-text: #1e3a8a;
      --border-color: #cbd5e1;
      --focus-color: #2563eb;
    }

    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
    }

    body{
      font-family: 'Segoe UI', Arial, sans-serif;
      background: linear-gradient(135deg, var(--bg-gradient-1), var(--bg-gradient-2));
      background-attachment: fixed;
      min-height:100vh;
      padding:20px;
      padding-bottom: 60px;
    }

    .container{
      width:100%;
      max-width:800px;
      margin: 0 auto;
    }

    h1{
      color:var(--text-white);
      text-align:center;
      font-size:48px;
      margin-bottom:10px;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .subtitle{
      text-align:center;
      color:var(--text-light);
      margin-bottom:30px;
      font-size:18px;
    }

    .card{
      background:var(--card-bg);
      padding:30px;
      border-radius:20px;
      box-shadow:0 10px 30px rgba(0,0,0,0.3);
      margin-bottom:25px;
    }

    .card-title {
      font-size:24px;
      margin-bottom:20px;
      color:var(--secondary-color);
      font-weight:bold;
      border-bottom: 3px solid var(--primary-color);
      padding-bottom:10px;
    }

    label{
      display:block;
      margin-bottom:10px;
      font-weight:bold;
      color:var(--secondary-color);
    }

    select,
    input,
    textarea{
      width:100%;
      padding:14px;
      border-radius:12px;
      border:1px solid var(--border-color);
      margin-bottom:18px;
      font-size:16px;
      background: white;
    }

    textarea {
      resize: vertical;
      min-height: 100px;
    }

    input:focus,
    select:focus,
    textarea:focus{
      outline:none;
      border-color:var(--focus-color);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }

    button{
      width:100%;
      padding:15px;
      border:none;
      border-radius:12px;
      background:var(--primary-color);
      color:var(--text-white);
      font-size:17px;
      font-weight:bold;
      cursor:pointer;
      transition:0.3s;
    }

    button:hover{
      background:var(--primary-hover);
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba(37, 99, 235, 0.3);
    }

    #hasil{
      margin-top:25px;
      padding:20px;
      border-radius:15px;
      background:var(--result-bg);
      color:var(--result-text);
      font-size:20px;
      font-weight:bold;
      text-align:center;
    }

    .form-title{
      font-size:18px;
      margin-bottom:15px;
      color:var(--secondary-color);
      font-weight:bold;
    }

    /* Materi Section */
    .materi-section {
      display: none;
      margin-top: 20px;
    }

    .materi-section.active {
      display: block;
    }

    .materi-content {
      background: #f8fafc;
      padding: 20px;
      border-radius: 12px;
      border-left: 4px solid var(--primary-color);
      margin-bottom: 15px;
    }

    .materi-content h3 {
      color: var(--secondary-color);
      margin-bottom: 10px;
      font-size: 20px;
    }

    .materi-content p {
      color: #475569;
      line-height: 1.6;
      margin-bottom: 10px;
    }

    .materi-content .formula {
      background: #e0f2fe;
      padding: 15px;
      border-radius: 8px;
      font-family: 'Courier New', monospace;
      font-size: 16px;
      margin: 10px 0;
      text-align: center;
      font-weight: bold;
      color: var(--secondary-color);
    }

    .materi-content .example {
      background: #fef3c7;
      padding: 15px;
      border-radius: 8px;
      margin: 10px 0;
    }

    .materi-content .example strong {
      color: #92400e;
    }

    .materi-content ul {
      margin-left: 20px;
      color: #475569;
    }

    .materi-content li {
      margin: 8px 0;
    }

    /* Navigation Tabs */
    .nav-tabs {
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }

    .nav-tab {
      flex: 1;
      min-width: 120px;
      padding: 12px;
      border: none;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.2);
      color: var(--text-white);
      font-size: 14px;
      font-weight: bold;
      cursor: pointer;
      transition: 0.3s;
      text-align: center;
    }

    .nav-tab:hover {
      background: rgba(255, 255, 255, 0.3);
    }

    .nav-tab.active {
      background: var(--primary-color);
      box-shadow: 0 3px 10px rgba(37, 99, 235, 0.4);
    }

    /* About Us Section */
    .about-section {
      display: none;
    }

    .about-section.active {
      display: block;
    }

    .about-content h2 {
      color: var(--secondary-color);
      margin-bottom: 15px;
    }

    .about-content p {
      color: #475569;
      line-height: 1.8;
      margin-bottom: 15px;
    }

    .about-content .tip-box {
      background: #d1fae5;
      padding: 15px;
      border-radius: 10px;
      border-left: 4px solid #10b981;
      margin: 15px 0;
    }

    .about-content .tip-box h4 {
      color: #065f46;
      margin-bottom: 10px;
    }

    .about-content .tip-box code {
      background: #ffffff;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: 'Courier New', monospace;
      color: #1e3a8a;
    }

    /* Feedback Section */
    .feedback-section {
      display: none;
    }

    .feedback-section.active {
      display: block;
    }

    .feedback-success {
      background: #d1fae5;
      color: #065f46;
      padding: 15px;
      border-radius: 10px;
      text-align: center;
      margin-top: 15px;
      display: none;
    }

    /* Footer */
    .footer {
      text-align: center;
      color: var(--text-light);
      margin-top: 30px;
      padding: 20px;
      font-size: 14px;
    }

    /* Responsive */
    @media (max-width: 600px) {
      h1 {
        font-size: 36px;
      }
      
      .card {
        padding: 20px;
      }
      
      .nav-tab {
        min-width: 100px;
        font-size: 13px;
        padding: 10px;
      }
    }
  </style>
</head>

<body>

  <div class="container">

    <h1>🧪 DigiChem</h1>

    <p class="subtitle">
      Digital Chemistry Calculator & Learning Platform
    </p>

    <!-- Navigation Tabs -->
    <div class="nav-tabs">
      <button class="nav-tab active" onclick="showTab('calculator')">🔬 Kalkulator</button>
      <button class="nav-tab" onclick="showTab('materi')">📚 Materi</button>
      <button class="nav-tab" onclick="showTab('about')">ℹ️ About Us</button>
      <button class="nav-tab" onclick="showTab('feedback')">💬 Feedback</button>
    </div>

    <!-- Calculator Tab -->
    <div id="calculator-tab" class="tab-content">
      <div class="card">

        <label>Pilih Kalkulator</label>

        <select id="menu" onchange="ubahForm()">

          <option value="normalitas">
            Normalitas (N)
          </option>

          <option value="molaritas">
            Molaritas (M)
          </option>

          <option value="be">
            BE (Berat Ekivalen)
          </option>

          <option value="bm">
            BM (Berat Molekul)
          </option>

          <option value="ar">
            Ar (Massa Atom Relatif)
          </option>

          <option value="suhu">
            Konversi Suhu
          </option>

          <option value="ppm">
            PPM
          </option>

        </select>

        <div id="formArea"></div>

        <button onclick="hitung()">
          Hitung
        </button>

        <div id="hasil">
          Hasil akan muncul di sini
        </div>

      </div>
    </div>

    <!-- Materi Tab -->
    <div id="materi-tab" class="tab-content materi-section">
      <div class="card">
        <div class="card-title">📚 Materi Pembelajaran Kimia</div>

        <!-- Normalitas -->
        <div class="materi-content">
          <h3>1. Normalitas (N)</h3>
          <p><strong>Definisi:</strong> Normalitas adalah jumlah mol ekivalen zat terlarut per liter larutan. Normalitas digunakan untuk mengukur konsentrasi larutan dalam reaksi kimia.</p>
          
          <div class="formula">
            N = (massa / BE) ÷ (volume / 1000)<br>
            atau<br>
            N = (massa × 1000) / (BE × volume)
          </div>

          <p><strong>Keterangan:</strong></p>
          <ul>
            <li>N = Normalitas (N atau ek/L)</li>
            <li>massa = massa zat terlarut (gram)</li>
            <li>BE = Berat Ekivalen (gram/ekivalen)</li>
            <li>volume = volume larutan (mL)</li>
          </ul>

          <div class="example">
            <strong>Contoh Soal:</strong><br>
            Hitung normalitas larutan H₂SO₄ dengan massa 98 gram dan volume 500 mL (BE = 49)<br><br>
            N = (98 / 49) ÷ (500 / 1000)<br>
            N = 2 ÷ 0.5<br>
            N = 4 N
          </div>
        </div>

        <!-- Molaritas -->
        <div class="materi-content">
          <h3>2. Molaritas (M)</h3>
          <p><strong>Definisi:</strong> Molaritas adalah jumlah mol zat terlarut per liter larutan. Ini adalah satuan konsentrasi yang paling umum digunakan dalam kimia.</p>
          
          <div class="formula">
            M = (massa / BM) ÷ (volume / 1000)<br>
            atau<br>
            M = (massa × 1000) / (BM × volume)
          </div>

          <p><strong>Keterangan:</strong></p>
          <ul>
            <li>M = Molaritas (M atau mol/L)</li>
            <li>massa = massa zat terlarut (gram)</li>
            <li>BM = Berat Molekul/Massa Molar (g/mol)</li>
            <li>volume = volume larutan (mL)</li>
          </ul>

          <div class="example">
            <strong>Contoh Soal:</strong><br>
            Hitung molaritas larutan NaCl dengan massa 58.5 gram dan volume 1 L (BM = 58.5)<br><br>
            M = (58.5 / 58.5) ÷ (1000 / 1000)<br>
            M = 1 ÷ 1<br>
            M = 1 M
          </div>
        </div>

        <!-- Perbedaan N dan M -->
        <div class="materi-content">
          <h3>3. Perbedaan Normalitas (N) dan Molaritas (M)</h3>
          
          <table style="width:100%; border-collapse: collapse; margin: 15px 0;">
            <tr style="background: #e0f2fe;">
              <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">Aspek</th>
              <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">Normalitas (N)</th>
              <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">Molaritas (M)</th>
            </tr>
            <tr>
              <td style="padding: 12px; border: 1px solid #cbd5e1;"><strong>Satuan</strong></td>
              <td style="padding: 12px; border: 1px solid #cbd5e1;">mol ekivalen/L</td>
              <td style="padding: 12px; border: 1px solid #cbd5e1;">mol/L</td>
            </tr>
            <tr style="background: #f8fafc;">
              <td style="padding: 12px; border: 1px solid #cbd5e1;"><strong>Konsep</strong></td>
              <td style="padding: 12px; border: 1px solid #cbd5e1;">Menghitungkan ekivalen aktif</td>
              <td style="padding: 12px; border: 1px solid #cbd5e1;">Menghitungkan mol total</td>
            </tr>
            <tr>
              <td style="padding: 12px; border: 1px solid #cbd5e1;"><strong>Rumus BE/BM</strong></td>
              <td style="padding: 12px; border: 1px solid #cbd5e1;">BE = BM / valensi</td>
              <td style="padding: 12px; border: 1px solid #cbd5e1;">BM = massa molekul</td>
            </tr>
            <tr style="background: #f8fafc;">
              <td style="padding: 12px; border: 1px solid #cbd5e1;"><strong>Penggunaan</strong></td>
              <td style="padding: 12px; border: 1px solid #cbd5e1;">Reaksi asam-basa, redoks</td>
              <td style="padding: 12px; border: 1px solid #cbd5e1;">Umum, stoikiometri</td>
            </tr>
            <tr>
              <td style="padding: 12px; border: 1px solid #cbd5e1;"><strong>Hubungan</strong></td>
              <td colspan="2" style="padding: 12px; border: 1px solid #cbd5e1;">N = M × valensi</td>
            </tr>
          </table>

          <p><strong>Catatan Penting:</strong></p>
          <ul>
            <li>Untuk asam/basa monoprotik (HCl, NaOH): N = M</li>
            <li>Untuk asam/basa diprotik (H₂SO₄, Ca(OH)₂): N = 2M</li>
            <li>Untuk asam/basa tripotik (H₃PO₄): N = 3M</li>
          </ul>
        </div>

        <!-- Berat Ekivalen -->
        <div class="materi-content">
          <h3>4. Berat Ekivalen (BE)</h3>
          <p><strong>Definisi:</strong> Berat ekivalen adalah massa zat yang bereaksi dengan atau setara dengan 1 mol elektron, 1 mol H⁺, atau 1 mol OH⁻.</p>
          
          <div class="formula">
            BE = BM / valensi
          </div>

          <p><strong>Keterangan:</strong></p>
          <ul>
            <li>BE = Berat Ekivalen (g/ek)</li>
            <li>BM = Berat Molekul (g/mol)</li>
            <li>valensi = jumlah H⁺ (untuk asam) atau OH⁻ (untuk basa) yang dapat dilepaskan</li>
          </ul>

          <div class="example">
            <strong>Contoh:</strong><br>
            H₂SO₄: BM = 98, valensi = 2 (dapat melepas 2 H⁺)<br>
            BE = 98 / 2 = 4
