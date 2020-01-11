package com.java;

public class BinaryToOctal {

    public static void main(String args[]){
        /* To take input from user, import the java.util.Scanner
         * package and write the following lines
         * Scanner scanner = new Scanner(System.in);
         * System.out.println("Enter the number: ");
         * int bnum = Integer.parseInt(scanner.nextLine(), 2);
         */
        String number = "10101";
        int bnum = Integer.parseInt(number, 2);
        String ostr = Integer.toOctalString(bnum);
        System.out.println("Octal Value after conversion is: "+ostr);
    }
}
