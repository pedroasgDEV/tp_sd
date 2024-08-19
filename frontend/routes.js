//modulos
const express = require('express');
const routes = express.Router();

//Controlers
const home = require('./src/controllers/homeController');
const create = require('./src/controllers/createUser')
const update = require('./src/controllers/updateUser')

routes.get("/", home.get);
routes.post("/", home.post);

routes.get('/createPersona', create.get)
routes.post('/createPersona', create.post)

routes.get('/updatePersona/:id', update.get)
routes.post('/updatePersona/:id', update.post)
routes.get('/delete/:id', update.del)

module.exports = routes;

