const express = require("express");
const app = express();
const path = require('path');
const mongoose = require('mongoose');
const methodOverride = require('method-override');

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
//lets you get the stuff from form body
app.use(express.urlencoded({ extended: true }))


app.get('/test', (req, res) => {
    res.send('here we are');
})

app.get('/', (req, res) => {
    res.render('home');
})

app.post('/inputDoc', async (req, res) => {
    //Ideally we should be veryfying the object from the form
  const input = req.body;
  console.log(req.body);
//   console.log(document)
  const docName = input.document.name;
  console.log(docName);
  res.render('summary', {docName})
})
app.listen(3000, () => {
    console.log("APP IS LISTENING ON PORT 3000")
})
