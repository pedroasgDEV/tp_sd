const sessionAuth = (req, res, next, getTestingValue) => {
    const token = req.headers.authorization;

    if (token === 'Bearer 123') {
        next(); 
    } else {
        res.status(401).json({ message: 'Unauthorized' });
    }
};

module.exports = {
    sessionAuth
};
