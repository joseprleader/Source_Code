// Intercollegiate Programming Competition 2021 Blue Track Problem 3
// Largest Quotient

// Import scanner to get data from STDIN
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class Solution
{
    public static void main(String args[])
    {
        // Create a Scanner Object to get input from STDIN
        Scanner scanner = new Scanner(System.in);
    
        System.out.println("Enter integers separated by a space.");

        String nums = scanner.nextLine();

        // Close scanner when all data from STDIN has been taken
        scanner.close();
        // Format data as the program requires

        ArrayList<Integer> numsList = formatData(nums);

        // Show the maximun quotient to STDOUT
        int quotient = largestQuotient(numsList);

        System.out.println(quotient);
    }

    public static ArrayList<Integer> formatData(String nums)
    {
        // Firstly, get an array of string numbers from the string of numbers
        List<String> numsStr = Arrays.asList(nums.split(" "));

        // Cast it to an ArrayList to be able to change elements from it
        ArrayList<String> numsStrArr = new ArrayList<String>(numsStr);

        // Exclude the last number, a 0
        numsStrArr.remove(numsStr.size() - 1);

        // Make an empty ArrayList for integers
        ArrayList<Integer> numsInt = new ArrayList<Integer>();

        // Loop through the list of number strings to convert them to integers
        // and add them to the arraylist of integers
        for (int i = 0; i < numsStrArr.size(); i++)
        {
            int num = Integer.parseInt(numsStrArr.get(i));
            numsInt.add(num);
        }

        // Return the ArrayList of integers to the user
        return numsInt;

    }

    public static int largestQuotient(ArrayList<Integer> numsList)
    {
        // Get the largest number from the arrayList
        int maxNum = Collections.max(numsList);

        // Get the minimum number from the list
        int minNum = Collections.min(numsList);

        // Divide both numbers and get the largest quotient

        int maxQuotient = maxNum / minNum;

        return maxQuotient;
    }
}