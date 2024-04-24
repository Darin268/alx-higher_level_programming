#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}

// Extract the URL from command line arguments
const url = process.argv[2];

// Make a GET request to the provided URL
request(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }

  // Print the status code
  console.log(`code: ${response.statusCode}`);
});
