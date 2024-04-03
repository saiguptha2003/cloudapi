markdown
Copy code
# Node.js Express Tutorial: Adding Sessions and Connecting to MongoDB & MySQL

In this tutorial, we'll walk through adding session management to a Node.js Express application and connecting it to both MongoDB and MySQL databases.

## Prerequisites

Before getting started, make sure you have the following installed:

- Node.js and npm
- MongoDB (if using MongoDB)
- MySQL (if using MySQL)

## Step 1: Set Up Express Application

First, let's set up a basic Express application:

```bash
mkdir express-session-tutorial
cd express-session-tutorial
npm init -y
npm install express express-session
Create a server.js file with the following content:
```

```javascript
Copy code
const express = require('express');
const session = require('express-session');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(session({
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: true
}));

app.get('/', (req, res) => {
  req.session.views = (req.session.views || 0) + 1;
  res.send(`You have visited this page ${req.session.views} times.`);
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
Now, run your server:

bash
Copy code
node server.js
Visit http://localhost:3000 in your browser. You should see the visit count increment each time you refresh.

```

Step 2: Connect to MongoDB
To connect to MongoDB, you'll need to install mongodb package:

bash
Copy code

```bash
npm install mongodb
Now, modify server.js to connect to MongoDB:

```

javascript
Copy code

```javascript
const express = require('express');
const session = require('express-session');
const { MongoClient } = require('mongodb');

const app = express();
const PORT = process.env.PORT || 3000;

const client = new MongoClient('mongodb://localhost:27017', { useUnifiedTopology: true });

app.use(session({
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: true
}));

app.get('/', async (req, res) => {
  try {
    const db = client.db('test');
    const counter = db.collection('counter');
    const doc = await counter.findOneAndUpdate({}, { $inc: { count: 1 } }, { upsert: true });
    res.send(`You have visited this page ${doc.value.count} times.`);
  } catch (error) {
    console.error(error);
    res.status(500).send('Server Error');
  }
});

client.connect().then(() => {
  app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  });
});
```
Step 3: Connect to MySQL
To connect to MySQL, you'll need to install mysql package:


```bash
npm install mysql
Now, modify server.js to connect to MySQL:
```


javascript
Copy code

```js
const express = require('express');
const session = require('express-session');
const mysql = require('mysql');

const app = express();
const PORT = process.env.PORT || 3000;

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'your-username',
  password: 'your-password',
  database: 'your-database'
});

app.use(session({
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: true
}));

app.get('/', (req, res) => {
  connection.query('SELECT COUNT(*) AS count FROM visits', (error, results) => {
    if (error) {
      console.error(error);
      return res.status(500).send('Server Error');
    }
    const count = results[0].count;
    res.send(`You have visited this page ${count} times.`);
  });
});

connection.connect((error) => {
  if (error) {
    console.error('Error connecting to MySQL:', error);
    return;
  }
  console.log('Connected to MySQL');
  
  app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  });
});

```
```bash
npm install dotenv
```


```js
require('dotenv').config();
const dbHost = process.env.DB_HOST;
const dbUser = process.env.DB_USER;
const dbPassword = process.env.DB_PASSWORD;
const dbDatabase = process.env.DB_DATABASE;
```

```text
DB_HOST=localhost
DB_USER=myuser
DB_PASSWORD=mypassword
DB_DATABASE=mydatabase
```


```.gitignore
# Ignore node_modules directory
node_modules/

# Ignore .env file
.env

# Ignore log files
*.log
```


docker 
```docker
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag

```

```docker
docker run --name some-mongo -d mongo:tag


docker exec -it some-mongo bash


docker logs some-mongo
```
