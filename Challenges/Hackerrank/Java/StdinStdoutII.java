// Solution to challenge Java Stdin and Stdout II from Hackerrank

import java.util.Scanner;

// ONLY USE THE CODE THAT IS CONTAINED INSIDE OF THE CLASS
// DO NOT CHANGE THE CLASS NAME FROM THE HACKERRANK CODE

public class StdinStdoutII {

    public static void main(String[] args) {

        // Take input from STDIN
        Scanner scan = new Scanner(System.in);

        // Take an integer from STDIN
        int i = scan.nextInt();

        // Take a double from STDIN
        double d = scan.nextDouble();

        // Go to the next line of the Scanner
        scan.nextLine();

        // Take a string from STDIN
        String s = scan.nextLine();
        
        // Close the scanner
        scan.close();
        // Write your code here.

        // Print the user's input
        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}