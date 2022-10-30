// Intercollegiate Programming Competition 2021 Blue Track Problem 4
// Where Am I?

// Q1 -> (+,+)
// Q2 -> (-,+)
// Q3 -> (-,-)
// Q4 -> (+,-)

// Import Scanner class to take input from STDIN
import java.util.Scanner;
import java.util.Arrays;
import java.util.List;

public class Solution
{
    public static void main(String[] args)
    {
        // Create a Scanner object to take input from STDIN
        Scanner scanner = new Scanner(System.in);

        // Take the coordinates from STDIN
        System.out.print("Enter X and Y separated by a space: ");
        String coordinates = scanner.nextLine();

        // Close the scanner once you've taken all input from STDIN
        scanner.close();

        // Split the coordinates String into a list with the first element
        // being the X coordinate and the last element being the Y coordinate
        List<String> coors = Arrays.asList(coordinates.split(" "));

        // No need to convert coordinates to integers, just check if the '-' character is present
        // Check which coordinates are positives or negatives
         // Use indexOf method of Strings to find out if "-" is present in a String
        // If the method returns -1, "-" is not in the String

        // Conditions for Q1
        if (coors.get(0).indexOf("-") == -1 && coors.get(1).indexOf("-") == -1)
        {
            System.out.println("Q1");
        }

        // Conditions for Q2
        else if (coors.get(0).indexOf("-") != -1 && coors.get(1).indexOf("-") == -1)
        {
            System.out.println("Q2");
        }

        // Conditions for Q3
        else if (coors.get(0).indexOf("-") != -1 && coors.get(1).indexOf("-") != -1)
        {
            System.out.println("Q3");
        }

        // Anything else belongs to Q4
        else
        {
            System.out.println("Q4");
        }
    }
}