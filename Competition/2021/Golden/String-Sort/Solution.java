import java.util.Scanner;
import java.util.ArrayList;

public class Solution
{
    // Steps to follow
    // 1) Create a new ArrayList for ordered words
    // 2) Find the word with least length in unordered ArrayList of words
    // 3) Add that word to the ArrayList of ordered words
    // 4) Remove that word from the list of ArrayList unordered words
    // 5) Repeat steps 1-4 until the length of the unordered words ArrayList is 0
    
    public static void main(String args[])
    {
        ArrayList<String> words = stdin();
        
        // Initialize another ArrayList<String> named orderedWords
        ArrayList<String> orderedWords = new ArrayList<String>();

        while (words.size() > 0)
        {
            // Get shortest word
            String shortestWord = shortestString(words);
            
            // Add this word to the list of ordered Words
            orderedWords.add(shortestWord);

            // Remove the shortest word from the list of unordered words
            words.remove(words.indexOf(shortestWord));
        }

        System.out.println(orderedWords);
        
    }

    public static ArrayList<String> stdin()
    {
        // Receive input from STDIN
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter count of words: ");

        int count = Integer.parseInt(scanner.nextLine());

        ArrayList<String> words = new ArrayList<String>();

        for (int i = 0; i < count; i++)
        {
            System.out.print("Enter next word: ");
            String word = scanner.nextLine();
            words.add(word);
        }

        scanner.close();

        return words;

    }

    public static String shortestString(ArrayList<String> unorderedWords)
    {
        // Find the shortest string in a ArrayList of strings in java
        String shortest = unorderedWords.get(0);

        for (String word: unorderedWords)
        {
            if (word.length() < shortest.length())
            {
                shortest = word;
            }
        }

        return shortest;
    }

}