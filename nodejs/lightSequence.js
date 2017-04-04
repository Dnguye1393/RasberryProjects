var wpi = require("wiring-pi");
wpi.setup('wpi');
var pins =[0,15,16] ;
var  value = 1;
pins.forEach(function(item) {
  wpi.pinMode(item, wpi.OUTPUT);
  console.log(item);
});
setInterval(function() {
  pins.forEach(function(item) {
    wpi.digitalWrite( item, value);
  });
  //console.log("Testing");
  value = +!value;
}, 500);
