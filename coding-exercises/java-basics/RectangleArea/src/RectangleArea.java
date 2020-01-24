package com.java;
import java.util.Scanner;



public class RectangleArea {

    public static void main(String []args){
        double length,width,area;

        Scanner sc=new Scanner(System.in);

        //Read Length and Width of Rectangle
        System.out.print("Enter length: ");
        length=sc.nextDouble();
        System.out.print("Enter width: ");
        width=sc.nextDouble();

        //Calculate Area
        area= length*width;

        //Print Result
        System.out.println("Area of Rectangle: " + area);

    }



}
