<?php
//TheFreeElectron 2015, http://www.instructables.com/member/TheFreeElectron/
//This page is requested by the JavaScript, it updates the pin's status and then print it
//Getting and using values
if (isset ( $_GET["pic"] )) {
	$pic = strip_tags ($_GET["pic"]);

	//test if value is a number
	if ( (is_numeric($pic)) && ($pic <= 7) && ($pic >= 0) ) {

		# phpinfo();
	  $status = array ( 0 );
	  //set pins mode to output

	  system ( "gpio mode " . 29 . " out" );
	  system ( "gpio mode " . 26 . " out" );
	  system ( "gpio mode " . 24 . " out" );

	  //turns on the LEDs
	  system ( "gpio write " . 29 . " 1" );
	  sleep ( 1 );
	  system ( "gpio write " . 26 . " 1" );
	  sleep ( 1 );
	  system ( "gpio write " . 24 . " 1" );


	  //reads and prints the LEDs status
	  exec ( "gpio read " . 29 . $status );
	  exec ( "gpio read " . 26 . $status );
	  exec ( "gpio read " . 24 . $status );
	  echo ( $status[0] );

	  //waits 2 seconds
	  sleep ( 2 );
	  //turns off the LEDs
	  system ( "gpio write " . 24 . " 0" );
	  sleep ( 1 );
	  system ( "gpio write " . 26 . " 0" );
	  sleep ( 1 );
	  system ( "gpio write " . 29 . " 0" );

	}
	else { echo ("fail"); }
} //print fail if cannot use values
else { echo ("fail"); }
?>
