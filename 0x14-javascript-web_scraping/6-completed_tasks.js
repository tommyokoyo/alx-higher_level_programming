#! /usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: script url');
  process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const completedTasks = {};

      for (const todo of todos) {
        if (todo.completed) {
          if (!completedTasks[todo.userId]) {
            completedTasks[todo.userId] = 1;
          } else {
            completedTasks[todo.userId]++;
          }
        }
      }

      for (const userId in completedTasks) {
        console.log(`User ID: ${userId}, Completed task: ${completedTasks[userId]}`);
      }
    } else {
      console.log('Error connecting to the api');
    }
  }
});
