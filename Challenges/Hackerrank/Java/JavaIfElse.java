// Solution to challenge Java If-Else from Hackerrank

// These imports come from the challenge, don't worry about them
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

// ONLY USE THE CODE THAT IS CONTAINED INSIDE OF THE CLASS
// DO NOT CHANGE THE CLASS NAME FROM THE HACKERRANK CODE

public class JavaIfElse {

    // Make the scanner a private attribute of this Java class
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        // Take an integer from STDIN
        int N = scanner.nextInt();

        // Do not take the following characters from STDIN
        // Don't worry about this. It comes with the challenge
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        // Close the scanner. Stop taking data from STDIN
        scanner.close();

        // If the number is odd. Print "Weird"
        if (N % 2 != 0)
        {
            System.out.println("Weird");
        }
        
        // Otherwise ...
        else
        {
            // If the even number is in the range (2,5) print "Not Weird"
            if (N >= 2 && N <= 5)
            {
                System.out.println("Not Weird");
            }

            // Otherwise, if it is in the range (6,20) print "Weird"     
            else if (N >= 6 && N <= 20)
            {
                System.out.println("Weird");
            }

            // Print "Not Weird" for all other cases
            else
            {
                System.out.println("Not Weird");
            }
              
        }
    }
}