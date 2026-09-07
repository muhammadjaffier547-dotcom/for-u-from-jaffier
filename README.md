# 📸 Olivia Rodrigo — Drop Dead (TikTok Aesthetic 4-Photo Lyrics Player)

[![GitHub Pages](https://img.shields.io/badge/Live-GitHub%20Pages-brightgreen?style=for-the-badge&logo=github)](https://muhammadjaffier547-dotcom.github.io/for-u-from-jaffier/)
[![TikTok Edit](https://img.shields.io/badge/TikTok-Edit%20by%20Jaffier-fe2c55?style=for-the-badge&logo=tiktok)](https://muhammadjaffier547-dotcom.github.io/for-u-from-jaffier/)

Project web player lirik aesthetic bergaya TikTok viral dengan fitur **4-Photo Transition bergaya kamera shutter snap ("Cekrek-cekrek")**, dynamic ambient glow backdrop, visualizer audio LED dot-matrix, dan sinkronisasi lirik vokal presisi.

> 🌐 **Live Demo Website**: [https://muhammadjaffier547-dotcom.github.io/for-u-from-jaffier/](https://muhammadjaffier547-dotcom.github.io/for-u-from-jaffier/)

---

## ✨ Fitur Utama

1. **🎬 Intro Layar Hitam & Dot-Matrix Glow:**
   - Animasi judul lagu `Drop Dead` & artis `Olivia Rodrigo` bergaya retro dot-matrix pixel.
   - Progress bar LED dan visualizer gelombang audio reaktif.
2. **🎤 Sinkronisasi Lirik Presisi:**
   - Lirik karaoke real-time per kata yang menyala (*word-by-word highlight*) tepat pada suku kata vokal.
3. **📸 4-Photo Dynamic Transition ("Cekrek"):**
   - Transisi 4 foto bergantian otomatis saat chorus dengan efek shutter flash kamera, frame jitter, dan lens click:
     - **Foto 1 (23.2s):** *"All pressed up in the bathroom line..."*
     - **Foto 2 (26.7s):** *"Told me that she loved my shoes..."*
     - **Foto 3 (31.0s):** *"Girl who only goes one way..."*
     - **Foto 4 (34.1s):** *"Girl who's gonna drop dead, gonna drop dead..."*
     - **Outro (39.2s):** Card aesthetic *"EDIT BY JAFFIER"*.
4. **🌌 9:16 Smart Framing & Ambient Blurred Backdrop:**
   - Foto tampil tajam dan utuh (*contain*) di tengah layar tanpa terpotong, didukung oleh latar ambient blur dinamis yang berubah warna mengikuti foto aktif.
5. **⚙️ Modal Pengaturan Foto Kustom (2x2 Grid):**
   - Kamu dapat mengganti ke-4 foto secara instan langsung dari browser via menu drawer/modal tanpa perlu edit kode! Foto tersimpan aman di `localStorage`.
6. **📱 Responsif & Touch Friendly:**
   - Didesain optimal untuk smartphone (iPhone/Android vertical format 9:16) dan layar desktop monitor.

---

## 🚀 Cara Menjalankan

### Opsi 1: Buka Langsung di Web (Tanpa Install Apapun)
Cukup buka link live GitHub Pages:
👉 **[https://muhammadjaffier547-dotcom.github.io/for-u-from-jaffier/](https://muhammadjaffier547-dotcom.github.io/for-u-from-jaffier/)**

### Opsi 2: Buka di VS Code ("Open with Live Server")
1. Clone repositori ini:
   ```bash
   git clone https://github.com/muhammadjaffier547-dotcom/for-u-from-jaffier.git
   ```
2. Buka folder di VS Code.
3. Klik kanan pada `index.html` -> pilih **"Open with Live Server"**.
4. Tekan **F11** untuk pengalaman fullscreen.

### Opsi 3: Jalankan via Node.js
```bash
node server.js
```
Akses di browser: `http://localhost:3000`

---

## 🎮 Kontrol & Shortcut

- **Spacebar / Klik Layar**: Play / Pause musik dan animasi.
- **F / F11**: Layar penuh (Fullscreen).
- **⚙️ Ganti Foto**: Klik tombol foto untuk membuka modal 2x2 grid dan upload 4 foto kustom pilihanmu.
- **Timeline Bar**: Klik di mana saja pada garis progress bar untuk melompat langsung ke bait lirik favoritmu.

---

## 📁 Struktur File

- `index.html` — Halaman utama web player (HTML5 Audio, Canvas Visualizer, CSS Shutter Animation, LocalStorage manager).
- `drop_dead.mp3` — File audio resmi Olivia Rodrigo — Drop Dead (TikTok Audio Cut 42s).
- `photo1.jpg`, `photo2.png`, `photo3.jpg`, `photo4.jpg` — Preset default 4 foto aesthetic.
- `background.jpg`, `outro.jpg` — Asset pendukung visual.
- `server.js` — Simple static HTTP server Node.js.

---

## 👤 Credits

- **Sound & Track**: *Drop Dead* by Olivia Rodrigo
- **Web Player & Edit**: **Jaffier** ([@muhammadjaffier547-dotcom](https://github.com/muhammadjaffier547-dotcom))
