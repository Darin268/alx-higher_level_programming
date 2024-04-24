#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <API URL>');
  process.exit(1);
}

// Extract the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the provided API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const data = JSON.parse(body);

  // Initialize an object to store the number of completed tasks for each user
  const completedTasksByUser = {};

  // Iterate through each task
  data.forEach(task => {
    // Check if the task is completed
    if (task.completed) {
      // Increment the count of completed tasks for the user
      if (completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId]++;
      } else {
        completedTasksByUser[task.userId] = 1;
      }
    }
  });

  // Print the number of completed tasks by user
  console.log(completedTasksByUser);
});
