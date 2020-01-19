package com.java;
import java.util.Timer;
import java.util.TimerTask;

public class StopThread extends Thread{

    private volatile boolean stop = false;
    private int counter = 0;

    public void run() {
        while (!stop && counter < 10000) {
            System.out.println(counter++);
        }
        if (stop)
            System.out.println("Detected stop");
    }
    public void requestStop() {
        stop = true;
    }
}
