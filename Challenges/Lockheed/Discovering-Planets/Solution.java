// Problem 5: Discovering Planets

// Goal: Check if a planet is habitable

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < n; i++)
        {
            String dataLine = scanner.nextLine();

            ArrayList<String> data = new ArrayList<String>(Arrays.asList(dataLine.split(" ")));

            double temp = Double.parseDouble(data.get(0));
            boolean withWater = booleanParser(data.get(1));
            boolean withField = booleanParser(data.get(2));
            double eccen = Double.parseDouble(data.get(3));

            String result = testPlanet(temp, withWater, withField, eccen);

            System.out.println(result);
        }

        scanner.close();

    }

    public static boolean booleanParser(String strBool)
    {
        boolean result = (strBool.equalsIgnoreCase("false")) ? false : true;
        return result;
    }

    public static String testPlanet(double temp, boolean withWater, boolean withField, double eccen)
    {
        if (temp > 100)
        {
            return "The planet is too hot.";
        }

        else if (temp < 0)
        {
            return "The planet is too cold.";
        }

        else if (!withWater)
        {
            return "The planet has no water.";
        }

        else if (!withField)
        {
            return "The planet has no magnetic field.";
        }

        else if (eccen > 0.6)
        {
            return "The planet's orbit is not ideal.";
        }

        else
        {
            return "The planet is habitable.";
        }
    }
}