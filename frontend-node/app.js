const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Gunakan variabel yang baru saja kita atur di Vercel
const BACKEND_URL = process.env.BACKEND_API_URL || 'https://snyxshop.pythonanywhere.com';

app.get('/', async (req, res) => {
    try {
        const response = await axios.get(`${BACKEND_URL}/api/guitars`);
        res.render('index', { 
            namaToko: "Snyx Shop", 
            guitars: response.data 
        });
    } catch (error) {
        res.status(500).send(`Gagal akses data di: ${BACKEND_URL}. Error: ${error.message}`);
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server berjalan di port ${PORT}`));