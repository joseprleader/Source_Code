// Intercollegiate Programming Competition 2021 Gold Track
// Problem 2 Single Digit

import java.util.Scanner;
import java.util.ArrayList;
import java.lang.Math;

public class Solution
{
    public static void main(String args[])
    {

        // Get input from STDIN
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");

        // Get number as a string
        String numStr = scanner.nextLine();

        scanner.close();

        // Get the list of digits from the number
        ArrayList<Integer> digits = splitToDigits(numStr);

        // List to be used in the while loop to find final single digit
        ArrayList<Integer> resultingList = new ArrayList<Integer>();

        for (int digit : digits)
        {
            resultingList.add(digit);
        }

        // Variable that controls if the final result is one single digit
        boolean oneDigit = resultingList.size() == 1;

        // As long as the final result is not single digit, keep subtracting
        while (!(oneDigit))
        {
            resultingList = getSubDigits(resultingList);

            if (onlyOne(resultingList).size() == 1 || resultingList.size() == 1)
            {
                oneDigit = true;
            }
        }

        if (onlyOne(resultingList).size() == 1)
        {
            System.out.println(onlyOne(resultingList).get(0));
        }

        else
        {
            System.out.println(resultingList.get(0));
        }

    }

    public static ArrayList<Integer> splitToDigits(String num)
    {

        // Final Array List of Digits
        ArrayList<Integer> digits = new ArrayList<Integer>();

        // Loop through every digit of the number
        for (int i = 0; i < num.length(); i++)
        {
            int digit = Integer.parseInt(String.valueOf(num.charAt(i)));
            digits.add(digit);
        }

        return digits;

    }

    public static ArrayList<Integer> onlyOne(ArrayList<Integer> digits)
    {

        // Make a list of items greater than 0
        ArrayList<Integer> greater0 = new ArrayList<Integer>();

        // Loop through the list of digits
        for (int digit : digits)
        {
            if (digit > 0)
            {
                greater0.add(digit);
            }
        }

        return greater0;

    }

    public static ArrayList<Integer> getSubDigits(ArrayList<Integer> digits)
    {

        // Final list of sub digits
        ArrayList<Integer> subDigits = new ArrayList<Integer>();

        // Loop through all digits but the last one
        for (int i = 0; i < digits.size() - 1; i++)
        {
            // Don't consider negative results, use absolute value
            int subDigit = Math.abs(digits.get(i) - digits.get(i + 1));

            // Add the result to the list of sub-digits
            subDigits.add(subDigit);
        }

        return subDigits;

    }
}