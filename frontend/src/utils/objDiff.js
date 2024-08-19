const { Person } = require("../class/person");

const person = require("../class/person").Person

function getObjectDifference(obj1, obj2) {
    const diff = {};

    for (let key in obj1) {
        if (obj1[key] !== obj2[key]) {
            diff[key] =  obj2[key];
        }
    }

    return diff;
}

exports.getObjectDifference = getObjectDifference;