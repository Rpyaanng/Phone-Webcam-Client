import javax.imageio.*;

import java.io.*;  
import java.net.*;
import java.awt.image.*;
public class App {
    public static String HOST = "localhost";
    public static int PORT = 5000;
    public static void main(String[] args) {  
        try{  
            ServerSocket ss=new ServerSocket(PORT);  
            Socket s = ss.accept();//establishes connection
            System.out.println("Connection Established"); 
            InputStream input = s.getInputStream();
            byte[] data = input.readAllBytes();
            BufferedImage image = ImageIO.read(new ByteArrayInputStream(data));
            ImageIO.write(image, "png", new File("image.png")); 
            ss.close();  
        }catch(Exception e){
            e.printStackTrace();
        }  
    }  
}  
