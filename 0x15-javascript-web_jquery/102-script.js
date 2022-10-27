$(document).ready(function () {
    $('INPUT#btn_translate').on('click', function () {
      const lang = $('INPUT#language_code').val();
      $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
        console.log(data);
        $('DIV#hello').text(data.hello);
      });
    });
  });
  