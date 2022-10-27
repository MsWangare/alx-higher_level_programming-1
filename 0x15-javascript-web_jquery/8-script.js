$(document).ready(function () {
  $.ajax({
    type: "GET",
    url: "https://swapi-api.hbtn.io/api/films/?format=json",
    success: function (data) {
      for (const film in data.results) {
        $("#list_movies").append(`<li> ${data.results[film].title}</li>`);
      }
    },
  });
});
