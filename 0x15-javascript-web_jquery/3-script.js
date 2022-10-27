// Turns the header red when the 'red header' text is clicked on
// by setting the header's class to red
$(document).ready(function () {
  $("#red_header").on("click", function () {
    $("header").addClass("red");
  });
});
