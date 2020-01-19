import java.util.Timer;
import java.util.TimerTask;

public class Stopping {
    public static void main(String[] args) {
        final com.java.StopThread stoppable = new com.java.StopThread();
        stoppable.start();

        new Timer(true).schedule(new TimerTask() {
                                     public void run() {
                                         System.out.println("Requesting stop");
                                         stoppable.requestStop();
                                     }
                                 },
                350);
    }

}
