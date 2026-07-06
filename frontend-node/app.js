const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();

// Konfigurasi EJS
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Mengambil URL API Backend dari Environment Variable (diisi saat hosting nanti)
// Jika tidak ada, otomatis pakai localhost (untuk backup saat kamu coding offline)
const BACKEND_URL = process.env.BACKEND_API_URL || 'http://127.0.0.1:5000';

app.get('/', async (req, res) => {
    try {
        // Mengambil data langsung dari backend python
        const response = await axios.get(`${BACKEND_URL}/api/guitars`);
        res.render('index', { 
            namaToko: "Snyx Shop", 
            guitars: response.data 
        });
    } catch (error) {
        console.error("Error Fetching Data:", error.message);
        res.status(500).send("Gagal mengambil data dari Backend Python. Pastikan backend sudah kamu jalankan!");
    }
});

// Port dinamis untuk cloud hosting
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Frontend Snyx Shop berjalan di http://localhost:${PORT}`);
});