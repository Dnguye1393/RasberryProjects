var wpi = require("wiring-pi");
wpi.setup('wpi');
var pin = 0 ;
var value = 1;
wpi.pinMode(pin, wpi.OUTPUT);
setInterval(function() {
  wpi.digitalWrite(pin, value);
  //console.log("Testing");
  value = +!value;
}, 500);
