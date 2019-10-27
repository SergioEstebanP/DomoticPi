import java.net.*;
import java.io.*;

public class Client {
    public static final int PORT = 10000;
    public static void main(String[] args) throws IOException {
        InetAddress addr = InetAddress.getByName("localhost");
        Socket client = new Socket(addr, PORT);
        try {
            PrintStream outred = new PrintStream(client.getOutputStream());
            outred.println("MAKE_DEPLOY");
        } catch (Exception e) {
            e.printStackTrace();
        }
        client.close();
    }
}