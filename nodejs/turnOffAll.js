var wpi = require("wiring-pi");
wpi.setup('wpi');
var value = 0;
for(var pin = 0 ; pin <=20; pin++){
  wpi.pinMode(pin, wpi.OUTPUT);
  wpi.digitalWrite(pin, value);
}
