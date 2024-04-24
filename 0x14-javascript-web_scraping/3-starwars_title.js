#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <movie ID>');
  process.exit(1);
}

// Extract the movie ID from command line arguments
const movieID = process.argv[2];

// Define the API endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const data = JSON.parse(body);

  // Print the title of the movie
  console.log(data.title);
});
