import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Collections;

public class Solution
{
    public static void main(String[] args)
    {
        // Hashmap that will contain numbers and their counts
        HashMap<Integer, Integer> numNCounts = new HashMap<Integer, Integer>();

        // Get STDIN from the user
        Scanner myScanner = new Scanner(System.in);

        System.out.println("Enter your numbers separated by a space");

        // Convert string given by the user to an ArrayList of numbers in the 1-100 range
        String numsStrForm = myScanner.nextLine();
        myScanner.close();

        String[] numsStrSplit = numsStrForm.split(" ");   
        ArrayList<Integer> nums = new ArrayList<Integer>();

        for (String numStr : numsStrSplit)
        {
            int num = Integer.valueOf(numStr);
            
            if (num >= 1 && num <= 100)
            {
                nums.add(num);
            }
        }

        for (int num : nums)
        {
            try
            {
                numNCounts.put(num, numNCounts.get(num) + 1);
            }

            catch (Exception e)
            {
                numNCounts.put(num, 1);
            }
        }

        // Loop through the sorted version of keys of the numNCounts HashMap
        ArrayList<Integer> sortedKeys = new ArrayList<Integer>(numNCounts.keySet());
        Collections.sort(sortedKeys);

        for (int keyNum : sortedKeys)
        {
            System.out.println(keyNum + " appears " + numNCounts.get(keyNum) + " times");
        }
    }
}