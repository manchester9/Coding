package com.java;

public class MultipleAttributes {

    String fname = "John";
    String lname = "Doe";
    int age = 24;

    public static void main(String[] args) {
        MultipleAttributes myObj = new MultipleAttributes();
        System.out.println("Name: " + myObj.fname + " " + myObj.lname);
        System.out.println("Age: " + myObj.age);
    }

}
