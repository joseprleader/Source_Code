import java.util.ArrayList;
import java.util.Scanner;

public class Solution
{
    public static void main(String[] args)
    {
        Scanner myScanner = new Scanner(System.in);

        System.out.println("Enter the number");
        String numStrForm = myScanner.nextLine();
        myScanner.close();

        int weight = 0;
        int weightedSum = 0;

        ArrayList<Integer> digits = new ArrayList<Integer>();
        ArrayList<Integer> weights = new ArrayList<Integer>();

        for (char lilChar : numStrForm.toCharArray())
        {
            weight++;
            int digit = Integer.valueOf(String.valueOf(lilChar));
            digits.add(digit);
            weights.add(weight);

        }

        for (int i = 0; i < digits.size(); i++)
        {
            int product = digits.get(i) * weights.get(i);
            weightedSum += product;
        }

        System.out.println("weighted sum is " + weightedSum);

    }
}