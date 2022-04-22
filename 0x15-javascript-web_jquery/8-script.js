$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
  const results = data.results;
  for (const res of results) {
    $('UL#list_movies').append($('<li></li>').text(res.title));
  }
});
