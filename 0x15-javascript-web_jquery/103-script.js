document.addEventListener('DOMContentLoaded', () => {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
    $.get(url, function (data, textStatus) {
      $('#hello').text(data.hello);
    });
  });
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      const lang = $('#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
      $.get(url, function (data, textStatus) {
        $('#hello').text(data.hello);
      });
    }
  });
});
