import java.net.*;
import java.io.*;

public class ServerThread implements Runnable {

    private final Socket s;

    public ServerThread(Socket s) {
        this.s = s;
    }

    public void run() {
        PrintStream outred = null;
        try (BufferedReader inred = new BufferedReader(new InputStreamReader(s.getInputStream()))) {
            outred = new PrintStream(s.getOutputStream());
            String line;
            while ((line = inred.readLine()) != null) {
                if ("MAKE_DEPLOY".equals(line)) {
                    // comandos de powershell para gestion de docker 
                    StringBuffer sb = new StringBuffer();
                    try {
                        Process command = Runtime.getRuntime().exec("docker-compose up");
                        command.waitFor();
                        BufferedReader reader = new BufferedReader(new InputStreamReader(command.getInputStream()));
                        String commandOutput = "";			
                        while ((commandOutput = reader.readLine())!= null) {
                            sb.append(commandOutput + "\n");
                        }
                        System.out.println(sb.toString());
                        System.out.println("Command executed Successfully");
                    } catch (Exception e) {
                        System.out.println("Error executing docker commands");
                        e.printStackTrace();
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace(); 
        }
        outred.close();
    }
}