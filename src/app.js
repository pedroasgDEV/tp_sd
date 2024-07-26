const express = require('express');
const app = express();
const personasRoute = require('./routes/personas');
const path = require('path');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/personas', personasRoute);

app.use(express.static(path.join(__dirname, 'view')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'view', 'index.html'));
});

app.get('/gerar', (req, res) => {
    res.sendFile(path.join(__dirname, 'view', 'gerar.html'));
});

app.get('/personasGeradas', (req, res) => {
    res.sendFile(path.join(__dirname, 'view', 'personasGeradas.html'));
});

app.get('/criar', (req, res) => {
    res.sendFile(path.join(__dirname, 'view', 'criar.html'));
});

module.exports = app;
