const post_mongo = require("../modules/mongo").post;
const Person = require("../class/person").Person;

function get (req, res) {
    res.render('create_persona');
}

async function post(req, res){
    const number = Math.floor(Math.random() * (100));
    let img;
    if(req.body.gender == "male")
        img = `https://randomuser.me/api/portraits/men/${number}.jpg`;
    else img = `https://randomuser.me/api/portraits/women/${number}.jpg`;

    const person = new Person(
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
        img,

        req.body.cpf,
    );

    const {__mongo_id, ...post_doc} = person;
    person.__mongo_id = (await post_mongo(post_doc))._id;

    const people = [];
    if (person.__mongo_id != undefined) people.push(person);

    res.render('index', { people: people });
}

module.exports = {
    get : get,
    post: post
}