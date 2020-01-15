package com.java;

public class DoubleString {
    public static void main(String args[]){
        String str = "122.202";

        /* Convert String to double using
         * parseDouble(String) method of Double
         * wrapper class
         */
        double dnum = Double.parseDouble(str);

        //displaying the value of variable dnum
        System.out.println(dnum);
    }
}
