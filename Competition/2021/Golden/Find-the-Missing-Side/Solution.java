/*  
Intercollegiate Programming Competition 2021 Golden Track Problem 1
Find the Missing Side

 Right Triangle Sides:
       AB -> Cathetus
       BC -> Cathetus
       AC -> Hypothenuse
*/

// Import Scanner to take input from STDIN
import java.util.Scanner;

// Import the math module to deal with square roots
import java.lang.Math;

// Use ArrayList and Arrays to make things simples
import java.util.ArrayList;
import java.util.Arrays;

public class Solution
{
    // Private attribute for triangle sides names
    private static String[] sidesNames = {"AB", "BC", "AC"};

    public static void main(String[] args)
    {
        // Create a Scanner object to get data from STDIN
        Scanner scanner = new Scanner(System.in);

        // Get data about the first side
        String[] firstData = getStdinData("first", scanner);

        // Get data about the second side
        String[] secondData = getStdinData("second", scanner);

        // Close Scanner, no more data will come from STDIN
        scanner.close();

        // Get the name of the third triangle side
        String missingName = getName(firstData, secondData);

        // Get the length of the third triangle side
        int missingLength = getLength(firstData, secondData);

        // Show the results to STDOUT
        System.out.println(missingName + " " + missingLength);

    }

    public static String[] getStdinData(String orderVal, Scanner scanner)
    {
        // Order val would be equal to "first" or "second"

        // Get side name from STDIN
        System.out.print("Enter " + orderVal + " segment: ");
        String sideName = scanner.nextLine();

        // Get length from STDIN
        System.out.print("Enter " + orderVal + " segment: ");
        String sideLength = scanner.nextLine();

        // Create an array that holds the value of both the side
        // and the name that come from STDIN
        String [] sideData = {sideName, sideLength};

        // Return data about this side
        return sideData;
    }

    public static boolean isHypo(String[] sideData)
    {
        // Return true if "AC" is equal to the first element
        // of the array, otherwise return false
        if (sideData[0].equals("AC"))
        {
            return true;
        }

        else
        {
            return false;
        }
    }

    public static String getName(String[] firstData, String[] secondData)
    {
        // Save the names of the given sides in an array
        ArrayList<String> givenSides = new ArrayList<String>(Arrays.asList(firstData[0], secondData[0]));

        // Loop through the array of all possible triangle sides
        for (int i = 0; i < sidesNames.length; i++)
        {
            // If a side is not present in the tuple of given
            // sides, return it.
            // For that is the name of the missing side
            if (!(givenSides.contains(sidesNames[i])))
            {
                return sidesNames[i];
            }
        }

        // Write this to make the program work properly
        return "";
    }

    public static int getLength(String[] firstData, String[] secondData)
    {
        // Parse the given lengths as integers and store them in an array
        int[] givenLengths = {Integer.parseInt(firstData[1]), Integer.parseInt(secondData[1])};

        // Check if any of the given sides is a hypothenuse
        boolean firstHypo = isHypo(firstData);
        boolean secondHypo = isHypo(secondData);

        // Create an integer variable space for the length of the missing side
        int missingLength;

        // NOTE: Math.sqrt() and Math.pow() always return doubles
        // You must convert the final result of Math.sqrt() to an integer to make it all work
        
        // If none of the given sides are hypothenuses, then the missing side is
        // If the missing side is a hypothenuse, use the formula
        // Math.sqrt(Math.pow(firstLen, 2) + Math.pow(secondLen, 2))
        if (!(firstHypo || secondHypo))
        {
            missingLength = (int)(Math.sqrt(Math.pow(givenLengths[0],2) + Math.pow(givenLengths[1],2)));
        }

        // Otherwise, if the first side is the hypothenuse, then the missing side is a cathetus
        // If the missing side is a cathetus and the first a hypothenuse, use the following formula:
        // Math.sqrt(Math.pow(firstLen, 2) -  Math.pow(secondLen, 2))
        else if (firstHypo)
        {
            missingLength = (int)(Math.sqrt(Math.pow(givenLengths[0], 2) - Math.pow(givenLengths[1], 2)));
        }

        // In all other cases, the second given side is the hypothenuse
        // Use the following formula to calculate the length of the missing side
        // Math.sqrt(Math.pow(secondLen, 2) - Math.pow(firstLen, 2))

        else
        {
            missingLength = (int)(Math.sqrt(Math.pow(givenLengths[1],2) - Math.pow(givenLengths[0], 2)));
        }

        return missingLength;
    }
}