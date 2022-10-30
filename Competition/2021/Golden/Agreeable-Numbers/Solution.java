// Intercollegiate Programming Competition 2021 Golden Track 
// Problem 3 Agreeable Numbers

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution
{
    public static void main(String args[])
    {
        // Get data from STDIN
        ArrayList<Integer> numsToCheck = new ArrayList<Integer>();

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter two numbers separated by a space");

        for (int i = 0; i < 2; i++)
        {
            numsToCheck.add(scanner.nextInt());
        }

        scanner.close();

        if (areAgreeable(numsToCheck.get(0), numsToCheck.get(1)))
        {
            System.out.println("Agreeable numbers");
        }

        else
        {
            System.out.println("Not agreeable numbers");
        }
    }

    public static ArrayList<Integer> getDivisors(int number)
    {
        // Number to regulate while loop, (exclude number itself)
        int numWhile = number - 1;

        // List of divisors starting with 1
        ArrayList<Integer> divisors = new ArrayList<Integer>(Arrays.asList(1));

        // Loop through all numbers that are less than the given number exluding 1
        while (numWhile > 1)
        {
            // If the division remainder is 0, the number is a divisor
            if (number % numWhile == 0)
            {
                divisors.add(numWhile);
            }

            // Subtract one from numWhile
            numWhile--;
        }

        return divisors;

    }

    public static int ArraySum(ArrayList<Integer> divisors)
    {
        // Return the total sum of all numbers in a list
        int sum = 0;

        for (int divisor : divisors)
        {
            sum += divisor;
        }

        return sum;

    }

    public static boolean areAgreeable(int num1, int num2)
    {
        // Find the divisors of both numbers
        ArrayList<Integer> div1 = getDivisors(num1);
        ArrayList<Integer> div2 = getDivisors(num2);
 
        // If the sum of the divisors of num1 is equal to num2 and the sum of divisors of num2 is equal to num1
        // the numbers are agreeable, otherwise they are not
        return ArraySum(div1) == num2 && ArraySum(div2) == num1;
    }
}