#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node {file name} www.example.com');
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('Error: ', error);
  } else {
    console.log('Code: ' + response.statusCode);
  }
});
