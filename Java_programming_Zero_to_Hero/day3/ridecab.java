//MINI PROJECT CAB FARE GENERATOR


import java.util.*;
 class cab {
    int fare;
    int d;
    public  cab(){
        fare=50;
    }
    
    public cab(int amt){
        fare=amt;
    }
    
    
}
public class ridecab
{
    
    public static void main(String args[]){
    Scanner ob = new Scanner(System.in);
    int cd;
    System.out.print("enter the distance of cab from the user:");
    cd=ob.nextInt();
    if(cd > 5){
        cab c = new cab(50+10*(cd-5));
        System.out.print("Total fare:"+c.fare+"\n");
    }
    else{
        cab c = new cab();
        System.out.print("enter the distance travelled:");
        c.d=ob.nextInt();
        c.fare+=c.d*10;
        System.out.print("Total fare:"+c.fare+"\n");
    }
    
    }
    
}
    
