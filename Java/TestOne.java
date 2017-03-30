public class TestOne{
  private String name = "First Test";
  public static void main(String args[]){
    TestOne us = new TestOne();
    System.out.println(us.getName());
  }

  public String getName(){
    return name;
  }
}
