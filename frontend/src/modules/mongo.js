const axios = require("axios");
const { json } = require("express/lib/response");
const Person = require("../class/person").Person

const link = "http://localhost:3030/api/person/"

//Array
async function get_many(qnt){
    result = (await axios.get(link + qnt)).data;

    result.forEach( (val, i, array) => {
        array[i] = convert(val)
    });

    return result;
}

//Obj
async function get_one(id){
    result = (await axios.get(link + `id:${id}`)).data;
    result = convert(result);
    return result;
}

async function post(doc) {
    result = (await axios.post(link, doc)).data;
    return result;
}

async function put(doc, id) {
    result = (await axios.put(link + `${id}`, doc)).data;
    return result;
}

async function del(id) {
    result = (await axios.delete(link + `${id}`)).data;
    return result;
}

function convert(doc){
    return new Person (
        //name
        doc.name,
        //email
        doc.email,
        //Phone
        doc.phone,

        //Number
        doc.address.number,
        //street
        doc.address.street,
        //city,
        doc.address.city,
        //state
        doc.address.state,
        //countru
        doc.address.country,
        //postcode
        doc.address.postcode,

        //Img
        doc.img,

        doc.cpf.cpf,

        doc._id
    )
}

module.exports = {
    "get_many" : get_many,
    "get_one" : get_one,
    "post" : post,
    "put" : put,
    "del" : del
}