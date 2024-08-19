
const get_one = require("../modules/mongo").get_one
const update = require("../modules/mongo").put
const del_doc = require("../modules/mongo").del
const Person = require("../class/person").Person
const getDif = require("../utils/objDiff").getObjectDifference

async function get (req, res) {
    const person = await get_one(req.params.id.slice(1));
    res.render('update_persona', { person: person } );
}

async function post (req, res){
    const person = await get_one(req.params.id.slice(1));

    const person_update = new Person(
        //name
        req.body.name,
        //email
        req.body.email,
        //Phone
        req.body.phone,

        //Number
        req.body.number,
        //street
        req.body.street,
        //city,
        req.body.city,
        //state
        req.body.state,
        //countru
        req.body.country,
        //postcode
        req.body.postcode,

        //Img
        person.img,
        req.body.cpf,
        person.mongo_id
    );

    const diff = getDif(person, person_update)
    await update(diff, req.params.id.slice(1))

    const people = []; people.push(person_update)

    res.render('index', { people: people });
}

async function del (req, res){
    await del_doc(req.params.id.slice(1));
    res.render('index', { people: [] });
}

module.exports = {
    get : get,
    post: post,
    del: del
}