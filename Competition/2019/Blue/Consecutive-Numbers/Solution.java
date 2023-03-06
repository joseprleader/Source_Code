import java.util.Scanner;
import java.util.ArrayList;

public class Solution
{
    public static void main(String[] args)
    {
        Scanner myScanner = new Scanner(System.in);

        System.out.println("Enter your numbers separated by a space");
        String numsStrForm = myScanner.nextLine();
        myScanner.close();

        String[] numsStrSplit = numsStrForm.split(" ");
        ArrayList<Integer> nums = new ArrayList<Integer>();

        for (String numStr : numsStrSplit)
        {
            int num = Integer.valueOf(numStr);
            
            nums.add(num);
        }

        int consecNums = 0;
        int prevNum = Integer.MIN_VALUE;

        for (int num : nums)
        {
            if (num == prevNum)
            {
                consecNums++;
            }

            else
            {
                consecNums = 0;
            }

            if (consecNums == 2)
            {
                break;
            }

            prevNum = num;
        }

        if (consecNums == 2)
        {
            System.out.println("Consecutive values found for " + prevNum);
        }

        else
        {
            System.out.println("Consecutive values not found");
        }
    }
}