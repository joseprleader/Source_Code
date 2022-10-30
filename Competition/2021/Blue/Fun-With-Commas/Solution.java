// Intercollegiate Programming Competition 2021 Blue Track Problem 2
// Fun With Commas

// Import utilities to extract data from STDIN
import java.util.Scanner;

// Import utilities to use resizable array ArrayList
import java.util.ArrayList;

public class Solution
{
    public static void main(String args[])
    {
        // Words given by the user, excluding 'quit'
        ArrayList<String> allWords = new ArrayList<String>();

        // Create a Scanner to get input from STDIN
        Scanner scanner = new Scanner(System.in);

        // Make a String place for the word to be entered
        String word = "";

        // Keep prompting the user for words until the word 'quit' is entered
        do
        {
            // Add the entered word to the ArrayList of all words
            System.out.print("Enter next word or quit: ");
            word = scanner.nextLine();

            // Do not add the quit word to the list
            if (!word.equals("quit"))
            {
                allWords.add(word);
            }

        } while (!(word.equals("quit")));

        // Close the scanner when it's of no use anymore
        scanner.close();

        // Concatenate all words in the required format
        String finalStr = concatenateWords(allWords);

        System.out.println(finalStr);
    }

    public static String concatenateWords(ArrayList<String> wordsArrayList)
    {
        /* Concatenate words of a list in a string of
         * the format: a, b, c and d.
         */

         // Final string to the printed
         String finalStr = "";

        // Iterate through all words of the list except the last one
        for (int i = 0; i < wordsArrayList.size() - 1; i++)
        {
            // Add the comma for words that are before the one in index -2 (The one before the last word in the ArrayList)

            // String to concatenate
            String toConcat = "";

            if (i != wordsArrayList.size() - 2)
            {
                toConcat = wordsArrayList.get(i) + ", ";
            } 

            else
            {
                toConcat = wordsArrayList.get(i) + " ";
            }

            finalStr += toConcat;
        }

        // If more that one word was given, add 'and' to the end
        if (wordsArrayList.size() > 1)
        {
            finalStr += "and " + wordsArrayList.get(wordsArrayList.size() - 1);
        }
        else
        {
            finalStr = wordsArrayList.get(wordsArrayList.size() - 1);
        }

        // Return the final string
        return finalStr;
    }
}