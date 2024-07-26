const express = require('express');
const router = express.Router();
const personasController = require('../controllers/personasController');
const authMiddleware = require('../middlewares/authMiddleware');

router.post('/generate', authMiddleware, personasController.generatePersonas);
router.post('/save', authMiddleware, personasController.savePersona);

module.exports = router;
