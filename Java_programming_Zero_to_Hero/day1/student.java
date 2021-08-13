import java.util.Scanner;
class student{
  
     public static void main(String args[]){
         Scanner sc = new Scanner(System.in);
         Scanner sc1 = new Scanner(System.in);
          Scanner sc2 = new Scanner(System.in);
          System.out.println("enter the roll:");
          int roll=sc.nextInt(); 
          System.out.print("enter the name:");

          String name=sc1.nextLine();
          System.out.println("enter the marks:");
          Float marks=sc2.nextFloat();
          System.out.println("student's name:"+ name);
          System.out.println("student's roll:"+ roll);
          System.out.println("student's marks:"+ marks);


     }


    
}
