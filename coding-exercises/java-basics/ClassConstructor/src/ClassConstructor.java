package com.java;

public class ClassConstructor {
    int x;

    // Create a class constructor for the MyClass class
    public ClassConstructor() {
        x = 5;
    }

    public static void main(String[] args) {
        ClassConstructor myObj = new ClassConstructor();
        System.out.println(myObj.x);
    }


}
