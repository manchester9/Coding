package com.java;

public class ConstructorWithParameters {

    int modelYear;
    String modelName;

    public ConstructorWithParameters(int year, String name) {
        modelYear = year;
        modelName = name;
    }

    public static void main(String[] args) {
        ConstructorWithParameters myCar = new ConstructorWithParameters(1969, "Mustang");
        System.out.println(myCar.modelYear + " " + myCar.modelName);
    }


}
