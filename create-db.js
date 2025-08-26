const sqlite3 = require('sqlite3')
const fs = require('fs')
const filepath = './data.db'


if (fs.existsSync(filepath)) {
    console.log('file exists.');
    const database = new sqlite3.Database("data.db")
}

else {
    const new_db = new sqlite3.Database("data.db")
    console.log('creating new database')
}