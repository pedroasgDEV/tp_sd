const fs = require('fs');
const path = require('path');

const personasFilePath = path.join(__dirname, '..', 'data', 'personas.json');

const generatePersonas = (req, res) => {
    const { numPersonas, region, state } = req.body;

    if (typeof numPersonas !== 'number' || numPersonas <= 0) {
        return res.status(400).json({ message: 'Número de personas deve ser um número maior que 0.' });
    }

    const personas = Array.from({ length: numPersonas }, (_, i) => ({
        id: i + 1,
        name: `Persona ${i + 1}`,
        region: region || 'Todas',
        state: state || 'Todos'
    }));

    res.status(200).json({ message: `Foram geradas ${numPersonas} personas.`, personas });
};

const savePersona = (req, res) => {
    const newPersona = req.body;

    const requiredFields = ['name', 'email', 'phone', 'street', 'number', 'city', 'state', 'country', 'zip'];
    for (const field of requiredFields) {
        if (!newPersona[field]) {
            return res.status(400).json({ message: `O campo ${field} é obrigatório.` });
        }
    }

    fs.readFile(personasFilePath, 'utf8', (err, data) => {
        if (err && err.code !== 'ENOENT') {
            return res.status(500).json({ message: 'Erro ao ler arquivo.' });
        }

        let personas = [];
        if (data) {
            personas = JSON.parse(data);
        }
        const newId = personas.length > 0 ? personas[personas.length - 1].id + 1 : 1;
        newPersona.id = newId;
        personas.push(newPersona);

        fs.writeFile(personasFilePath, JSON.stringify(personas, null, 2), 'utf8', (err) => {
            if (err) {
                return res.status(500).json({ message: 'Erro ao salvar persona.' });
            }
            res.status(201).json({ message: 'Persona criada com sucesso!' });
        });
    });
};

module.exports = { generatePersonas, savePersona };
