import java.util.HashMap;
import java.util.Scanner;
import java.lang.StringBuilder;

public class Solution
{
    public static void main(String[] args)
    {
        HashMap<Character, Integer> charNNums = new HashMap<Character, Integer> ();
        charNNums.put('A', 2);
        charNNums.put('B', 2);
        charNNums.put('C', 2);
        charNNums.put('D', 3);
        charNNums.put('E', 3);
        charNNums.put('F', 3);
        charNNums.put('G', 4);
        charNNums.put('H', 4);
        charNNums.put('I', 4);
        charNNums.put('J', 5);
        charNNums.put('K', 5);
        charNNums.put('L', 5);
        charNNums.put('M', 6);
        charNNums.put('N', 6);
        charNNums.put('O', 6);
        charNNums.put('P', 7);
        charNNums.put('Q', 7);
        charNNums.put('R', 7);
        charNNums.put('S', 7);
        charNNums.put('T', 8);
        charNNums.put('U', 8);
        charNNums.put('W', 9);
        charNNums.put('X', 9);
        charNNums.put('Y', 9);
        charNNums.put('Z', 9);

        StringBuilder myStrBuilder = new StringBuilder();

        String finalPhoneNum = "";

        Scanner myScanner = new Scanner(System.in);

        System.out.println("Enter phone number:");
        String userPhoneNum = myScanner.nextLine();

        for (char lilChar : userPhoneNum.toCharArray())
        {
            if (Character.isAlphabetic(lilChar))
            {
                int phoneDigit = charNNums.get(Character.toUpperCase(lilChar));
                myStrBuilder.append(phoneDigit);
            }

            else
            {
                myStrBuilder.append(lilChar);
            }
        }

        finalPhoneNum = myStrBuilder.toString();

        System.out.println(finalPhoneNum);
        

    }
}