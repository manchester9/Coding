package com.java;

public class SuspendThread {
    private int countDown = 5;
    private static int threadCount = 0;

    public SuspendThread() {
        super("" + ++threadCount);
        start();
    }

    private void start() {
    }

    public String toString() {
        return "#" + getName() + ": " + countDown;
    }

    private String getName() {
    }

    public void run() {
        while (true) {
            System.out.println(this);
            if (--countDown == 0) return;
            try {
                sleep(100);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }

    private void sleep(int i) {
    }

    public static void main(String[] args) throws InterruptedException {
        for (int i = 0; i < 5; i++) new SuspendThread().join();
        System.out.println("The thread has been suspened.");
    }

    private void join() {
    }


}
