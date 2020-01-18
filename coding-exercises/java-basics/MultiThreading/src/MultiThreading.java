package com.java;

public class MultiThreading<Threads> extends Threads {
    public void run(){
        System.out.println("My thread is in running state.");
    }
    public static void main(String args[]){
        MultiThreading obj=new MultiThreading();
        obj.start();
    }

    private void start() {

    }


}
