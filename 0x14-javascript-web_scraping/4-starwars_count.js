#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <API URL>');
  process.exit(1);
}

// Extract the API URL from command line arguments
const apiUrl = process.argv[2];

// Define the character ID for Wedge Antilles
const characterID = 18;

// Make a GET request to the Star Wars API films endpoint
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const data = JSON.parse(body);

  // Initialize a counter for movies containing Wedge Antilles
  let movieCount = 0;

  // Iterate through each movie
  data.results.forEach(movie => {
    // Check if Wedge Antilles is present in the characters list
    if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterID}/`)) {
      movieCount++;
    }
  });

  // Print the number of movies containing Wedge Antilles
  console.log(movieCount);
});
