#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.log('Usage: node filename url file-path');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error: ', error);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf-8', (error) => {
        if (error) {
          console.error(error);
        } else {
          console.log('File written successfully');
        }
      });
    } else {
      console.log(`Error fetching, Status: ${response.statusCode}`);
    }
  }
});
