#! /usr/bin/node

const fs = require('fs');

if (process.argv.length < 4) {
    console.log('provide both details!');
    process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
        console.error(err);
    } else {
        console.log('Done');
    }
});