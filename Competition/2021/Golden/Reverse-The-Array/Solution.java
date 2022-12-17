import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Solution
{
    public static void main(String args[])
    {
        ArrayList<Integer> oriNums = stdin();

        ArrayList<Integer> finalNums = new ArrayList<Integer>();

        for (int oriNum: oriNums)
        {
            finalNums.add(oriNum);
            Collections.reverse(finalNums);
        }

        System.out.println(finalNums);
    }

    public static ArrayList<Integer> stdin()
    {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter count, integers separated by a space:");

        String countNNums = scanner.nextLine().substring(2);

        scanner.close();

        ArrayList<String> strNums = new ArrayList<String>(Arrays.asList(countNNums.split(" ")));

        ArrayList<Integer> nums = new ArrayList<Integer>();

        for (String strNum : strNums)
        {
            Integer num = Integer.parseInt(strNum);
            nums.add(num);
        }

        return nums;

    }
}