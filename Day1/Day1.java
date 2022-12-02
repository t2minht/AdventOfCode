

//Import statements
import java.util.*; //util - Need it for Scanner    by putting .* at the end, you import everything under java.util
import java.io.*;   //io - stands for input output      Needed for Files
import static java.lang.System.*;       // Allows you to just write out.println instead of System.out.println

public class Day1{
    // Handles FileNotFoundException for Scanners, allows you to avoid using try/catch statements
    public static void main(String[] args) throws IOException{
        //Scanner Object allows you to read Files, takes in a File object as a parameter
        Scanner sc = new Scanner(new File("Day1Input.txt"));
        int maxCalories = 0;
        int currentCalories = 0;
        while(sc.hasNextLine()){    //While the Scanner has a next line to read      
            String line = sc.nextLine();    // Store that next line into a string

            // Check to see if line is blank, blank line means end of that elf's calories
            if(line.equals("")){   //use equals() method to compare strings, not ==
                maxCalories = Math.max(maxCalories, currentCalories);   //Math doesn't need an import statement     Math class contains many useful math functions
                currentCalories = 0;

                // continue means for the current loop (in this case, the while loop), to skip all of the code after the continue, and go back to the beginning of the loop
                continue;       //break; is a similar thing, except it stops the loop, no matter the conditions
            }
            currentCalories += Integer.parseInt(line);      // Integer.parseInt() allows you to convert a String into an Integer
        }
        out.println("Max Calories: " + maxCalories);
    }
}