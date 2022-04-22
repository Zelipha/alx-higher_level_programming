document.addEventListener('DOMContentLoaded', () => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
    $('#hello').text(data.hello);
  });
});
