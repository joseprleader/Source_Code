// Solution to challenge Java Stdin and Stdout I from Hackerrank

import java.util.Scanner;

// ONLY USE THE CODE THAT IS CONTAINED INSIDE OF THE CLASS
// DO NOT CHANGE THE CLASS NAME FROM THE HACKERRANK CODE

public class StdinStdoutI {

    public static void main(String[] args) {

        // Take input from STDIN
        Scanner scan = new Scanner(System.in);

        // Get a number
        int a = scan.nextInt();
        // Complete this line

        // Get another number 
        int b = scan.nextInt();
        // Complete this line

        // Get the last number 
        int c = scan.nextInt();

        // Close scanner object that takes data from STDIN
        scan.close();

        // Print all numbers the user entered
        System.out.println(a);
        // Complete this line
        System.out.println(b);
        // Complete this line
        System.out.println(c);
    }
}