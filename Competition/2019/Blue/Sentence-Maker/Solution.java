/* IPC Problem 7: Sentence Maker

 a) Process data from STDIN
 b) Check if the sentence can be made from the characters given
 b) Return output to the console
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Solution
{
    public static void main(String[] args)
    {
        // String to check if making sentence is possible
        String possible = "";

        // Get input from STDIN
        Scanner myScanner = new Scanner(System.in);

        System.out.println("Enter the list of letters:");
        String chars = myScanner.nextLine();

        System.out.println("Please enter the sentence to be formed:");
        String sentence = myScanner.nextLine();

        myScanner.close();

        // Get ArrayLists of characters out of the strings given by the user
        ArrayList<Character> allChars = getCharArrFromStr(chars);
        ArrayList<Character> sentenceChars = getCharArrFromStr(sentence);

        // Remove all characters in the sentence Chars from the allChars array
        for (Character theChar : sentenceChars)
        {
            if (allChars.contains(theChar))
            {
                allChars.remove(theChar);
            }

            else
            {
                possible = "not possible";
                break;
            }
        }

        if (possible.length() == 0)
        {
            possible = "possible";
        }

        System.out.println(possible);
    }

    public static ArrayList<Character> getCharArrFromStr(String myStr)
    {
        ArrayList<Character> charArr = new ArrayList<Character>();

        for (char theChar : myStr.toCharArray())
        {
            if (Character.isAlphabetic(theChar))
            {
                charArr.add(theChar);
            }
        }

        return charArr;
    }
}