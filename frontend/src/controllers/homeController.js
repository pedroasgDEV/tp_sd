//modulos
const get_many = require("../modules/mongo").get_many;

function get (req, res) {
    res.render('index', { people: [] });
}

async function post (req, res) {
    const count = parseInt(req.body.count);
    const people = await get_many(count);
    res.render('index', { people: people });
};

module.exports = {
    get : get,
    post : post
}