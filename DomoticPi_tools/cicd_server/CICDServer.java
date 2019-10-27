import java.net.*;
import java.io.*;

public class CICDServer {

    public static final int PORT = 10000;

    public static void main(String[] args) throws IOException {
        ServerSocket server = new ServerSocket(PORT);
        /* creación del socket */

        while (true) {
            Socket sock = server.accept();
            ServerThread deploy = new ServerThread(sock);
            Thread cicdDeployment = new Thread(deploy, "deployment");
            cicdDeployment.start();
        }
    }
}
