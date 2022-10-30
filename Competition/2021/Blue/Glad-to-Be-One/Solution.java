// Intercollegiate Programming Competition 2021 Blue Track Problem 6
// Glad to be One

// Import Scanner to get data from STDIN
import java.util.Scanner;

// Import resizible lists
import java.util.ArrayList;

public class Solution
{
    public static void main(String[] args)
    {
        // Create a Scanner Object to take data from STDIN
        Scanner scanner = new Scanner(System.in);

        // Get an integer from STDIN
        System.out.print("Enter a positive integer: ");
        int num = scanner.nextInt();

        // Close the Scanner for no more data will come from STDIN
        scanner.close();

        // Determine whether our number is glad or not
        boolean gladNum = isGlad(num);

        // Print Glad Number if the number is glad,
        // Otherwise print Not a Glad Number
        if (gladNum)
        {
            System.out.println("Glad Number");
        }

        else
        {
            System.out.println("Not a Glad Number");
        }
    }

    public static ArrayList<Integer> getDigits(int num)
    {
        // Convert the gotten integer into a String
        String numStr = Integer.toString(num);

        // Make an empty array list to append individual
        // digits on it, each digit will have its own space
        ArrayList<Integer> digits = new ArrayList<Integer>();

        // Loop through all the digits of the string version of the
        // number we made, make them integers and append them to
        // the ArrayList of Integers
        for (int i = 0; i < numStr.length(); i++)
        {
            // Convert each character of the numStr to an integer
            int digit = Integer.parseInt(String.valueOf(numStr.charAt(i)));

            // Add the digit to the list of digits
            digits.add(digit);
        }

        return digits;
    }

    public static boolean isGlad(int num)
    {

        // Make an integer variable that will control if the
        // loop to check keeps going on or not
        int result = 0;

        // Make an ArrayList of all gotten results
        // If there is repetition cut off the loop, the number won't be glad
        ArrayList<Integer> allResults = new ArrayList<Integer>();

        // As long as the result is not equal to one, keep checking
        while (result != 1)
        {
            // If the number has only one digit, square it and make that the result
            if (getDigits(num).size() == 1)
            {
                result = num * num;
            }

            // If the number has more than one digit, square each and
            // sum them up
            else
            {
                int subResult = 0;

                // Reference to Java for-each loop
                // https://www.w3schools.com/java/java_foreach_loop.asp
                for (int i = 0; i < getDigits(num).size(); i++)
                {
                    int squareNum = getDigits(num).get(i) * getDigits(num).get(i);
                    subResult += squareNum;
                }
                // Make the result equal to the total sum of the squares of each digit
                result = subResult;
            }

             // Update the value of the number to the gotten result
             num = result;

              // If the result is already present in the list of allResults,
            // cut the loop off by returning false
            if (allResults.contains(result))
            {
                return false;
            }

            // Add the gotten result to the list of allResults
            allResults.add(result);
        }

        // By this point there is a sequence that ends in 1,
        // so return True
        return true;

    }
    
}