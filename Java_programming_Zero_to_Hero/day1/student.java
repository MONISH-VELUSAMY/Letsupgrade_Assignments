import java.util.Scanner;
public class student{
     public static void main(String args[]){
         getinfo obj = new getinfo();
   
         obj.input();
         obj.display();
   
     }
}
class getinfo{


     int roll;
     String name;
     Float marks;
     Scanner sc = new Scanner(System.in);
     Scanner sc1 = new Scanner(System.in);

     void input(){

          
          System.out.print("enter the roll:");
          roll=sc.nextInt();
          System.out.print("enter the name:");
           name=sc1.nextLine();
          System.out.print("enter the mark:");
           marks=sc.nextFloat();

     }
      void display(){
        

          System.out.print("Roll: "+roll+"\n");
          System.out.print("Name: "+name+"\n");
          System.out.print("Mark: "+marks+"\n");









      }

   



}