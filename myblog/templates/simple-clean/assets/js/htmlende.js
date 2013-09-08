/*
 * htmlende.js
 * Javascript function to encode / decode html tag inside <code>
*/

function htmlEncode(value){
  return $('<div/>').text(value).html();
}

function htmlDecode(value){
  return $('<div/>').html(value).text();
}

$(function() {
  $('code').each(function() {
    var code = $(this).html();
    var encode = htmlEncode(code);
    $(this).html(encode);
  });
});
