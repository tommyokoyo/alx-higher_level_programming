const request = require('request');

if (process.argv.length < 3) {
  console.log('Please provide the Movie Id');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      let numberOfMovies = 0;

      for (let film of films) {
        if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          numberOfMovies++;
        }
      }

      console.log(`Found ${numberOfMovies} movies`);
    } else {
      console.log('Error connecting to the api');
    }
  }
});
