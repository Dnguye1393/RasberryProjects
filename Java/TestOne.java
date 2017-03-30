import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;

public class TestOne{
  private String name = "First Test";
  public static void main(String args[]){
    TestOne us = new TestOne();
    System.out.println(us.getName());
    final GpioController gpio = GpioFactory.getInstance();

    // provision gpio pin #01 as an output pin and turn on
    final GpioPinDigitalOutput pin = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_29, "MyLED", PinState.HIGH);

    System.out.println("--> GPIO state should be: ON");

    Thread.sleep(5000);

    // turn off gpio pin #01
    pin.low();
    System.out.println("--> GPIO state should be: OFF");

    Thread.sleep(5000);
    gpio.shutdown();

  }

  public String getName(){
    return name;
  }
}
