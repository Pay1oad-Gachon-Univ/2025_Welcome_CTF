const express = require('express');
const basicAuth = require('express-basic-auth');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 9999;
const flag = fs.readFileSync('flag.txt', 'utf8');

const genRanHex = size =>
  [...Array(size)].map(() => Math.floor(Math.random() * 16).toString(16)).join('');

const users = {
  'admin': genRanHex(16),
};

const loginRequired = basicAuth({
  authorizer: (username, password) => users[username] == password,
  challenge: true,
  unauthorizedResponse: 'Unauthorized',
});

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  if (users[username] == password) {
    return res.send(`<h1>Welcome, ${username}!</h1><p>Flag: ${flag}</p>`);
  }
  return res.send('<h1>Login Failed</h1><p>Invalid credentials</p>');
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Server listening at http://localhost:${port}`);
});