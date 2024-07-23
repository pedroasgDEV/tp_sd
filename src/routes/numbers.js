const express = require('express');
const router = express.Router();

router.post('/', (req, res) => {
    const { number } = req.body;
    if (number !== undefined) {
        res.send(`Retornamos as ${number} personas desejadas.`);
    } else {
        res.status(400).send('Número não fornecido.');
    }
});

module.exports = router;