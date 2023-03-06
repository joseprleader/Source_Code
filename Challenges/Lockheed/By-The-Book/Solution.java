// Problem 6: By the Book

// Goal: Check an ISBN is valid
import java.util.Scanner;
import java.util.ArrayList;

public class Solution
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < n; i++)
        {
            String isbn = scanner.nextLine();
            ArrayList<Integer> isbnNums = isbnDigits(isbn);
            System.out.println(isbnValidity(isbnNums));
        }

        scanner.close();
    }

    public static ArrayList<Integer> isbnDigits(String isbn)
    {
        ArrayList<Integer> isbnNums = new ArrayList<Integer>();

        for (int i = 0; i < isbn.length(); i++)
        {
            int numDigit;

            if (isbn.charAt(i) == 'X')
            {
                numDigit = 10;
            }

            else
            {
                numDigit = Integer.parseInt(String.valueOf(isbn.charAt(i)));
            }

            isbnNums.add(numDigit);
        }

        return isbnNums;

    }

    public static String isbnValidity(ArrayList<Integer> isbnNums)
    {
        int lenIsbn = isbnNums.size();

        int total = 0;
        int newTotal = 0;

        for (int i = 0; i < lenIsbn - 1; i++)
        {
            int current = isbnNums.get(i) * (lenIsbn - i);
            total += current;
        }

        newTotal = total;

        while (newTotal % 11 != 0)
        {
            newTotal++;
        }

        int diff = newTotal - total;

        if (diff == isbnNums.get(isbnNums.size() - 1))
        {
            return "VALID";
        }

        else
        {
            return "INVALID";
        }

    }

}