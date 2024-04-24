#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: node 101-starwars_characters.js <Movie ID>');
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

  // Function to fetch character data by URL
  const fetchCharacterData = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  };

  // Array to store promises for character data fetching
  const promises = [];

  // Iterate through each character URL
  data.characters.forEach(characterUrl => {
    // Create a promise for fetching character data
    promises.push(fetchCharacterData(characterUrl));
  });

  // Resolve all promises and print character names
  Promise.all(promises)
    .then(characters => {
      characters.forEach(character => {
        console.log(character);
      });
    })
    .catch(error => {
      console.error(error);
    });
});
