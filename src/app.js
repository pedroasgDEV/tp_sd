const express = require('express');
const app = express();

app.use(express.json());

const indexRouter = require('./routes/index');
const numbersRouter = require('./routes/numbers');
const { sessionAuth } = require('./middlewares/authMiddleware');

app.use((req, res, next) => {
    const getTestingValue = (req) => req.body.testing;
    sessionAuth(req, res, next, getTestingValue);
});

app.use('/', indexRouter);
app.use('/numbers', numbersRouter);

module.exports = app;