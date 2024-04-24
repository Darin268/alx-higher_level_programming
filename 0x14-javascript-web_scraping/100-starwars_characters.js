#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: node 100-starwars_characters.js <Movie ID>');
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

  // Print all characters of the movie
  data.characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse the character data
      const characterData = JSON.parse(body);

      // Print the character's name
      console.log(characterData.name);
    });
  });
});
