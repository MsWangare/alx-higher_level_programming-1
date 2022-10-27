$(document).ready(function () {
    $('INPUT#language_code').keydown(function (event) {
      if (event.which === 13) {
        const lang = $('INPUT#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
          console.log(data);
          $('DIV#hello').text(data.hello);
        });
      }
    });
    $('INPUT#btn_translate').on('click', function () {
      const lang = $('INPUT#language_code').val();
      $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
        console.log(data);
        $('DIV#hello').text(data.hello);
      });
    });
  });
  