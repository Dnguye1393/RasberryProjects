var gpio = require('pi-gpio');

var servoControllerPin = 26;

exports.blinkInterval = function(req, res){
	blink(servoControllerPin, req.params.interval);
	res.json(200, {message: 'success'});
}

exports.blink = function(req, res){
	blink(servoControllerPin);
	res.json(200, {message: 'success'});

}
exports.turnRight = function(req, res){
	console.log('turning right');
	res.json(200, {message: 'success'});
}

function blink(pin, interval, blinkTime){
	//set default value of interval
	//time between turning on and off
	if(interval == undefined) interval = 500;
	//set default time for blinkTime
	//number of times to blink the light on and off
	if(blinkTime == undefined) blinkTime = 5;

	//initialize the counting variable
	var i = 1;

	//timed loop to turn on and off the loop
	function myloop(){
		setTimeout(function(){
			//alternating between off and on
			if(i%2 == 0){
				writeHigh(pin);
			} else {
				writeLow(pin);
			}
			i++;
			if(i <= blinkTime*2){
				//still blinking
				myloop();
			} else {
				//the light has blinked blinkTime times
				// we are done with pin
				//closePin(pin)
			}
		}, interval);
	}
	//first call of the loop
	myloop();
}

function writeHigh(pin){
	console.log(pin + " high");
	gpio.open(pin, "output", function(err) {
	    gpio.write(pin, 1, function() {
	        gpio.close(pin);
	    });
	});
}

function writeLow(pin){
	console.log(pin + " low");
		gpio.open(pin, "output", function(err) {
	    gpio.write(pin, 0, function() {
	        gpio.close(pin);
	    });
	});
}

function closePin(pin){
	console.log('Turning pin off since we are done.');
	console.log(pin + " -");
		gpio.open(pin, "output", function(err) {
	    gpio.write(pin, 0, function() {
	        gpio.close(pin);
	    });
	});
}
