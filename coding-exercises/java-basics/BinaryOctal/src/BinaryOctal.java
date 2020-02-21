package com.java;

public class BinaryOctal {

    public static void main(String args[]){

        String number = "10101";
        int bnum = Integer.parseInt(number, 2);
        String ostr = Integer.toOctalString(bnum);
        System.out.println("Octal Value after conversion is: "+ostr);
    }


}
