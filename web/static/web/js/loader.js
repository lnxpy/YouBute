function isURL(str) {
  var res = str.match(/https*:\/\/w*.*[yY][oO][uU][tT][uU][Bb][Ee].[Cc][Oo][Mm]\/.*/g);
  return (res !== null)
}

function NeedRatingList() {
  if (isURL(document.getElementById('url').value)) {
  $('.ajaxProgress').show()
}
}
