import java.util.Scanner;
import java.util.ArrayList;

public class Solution
{
    public static void main(String[] args)
    {
        Scanner myScanner = new Scanner(System.in);

        System.out.println("Enter coordinates for first line (x1 y1 x2 y2)");
        String coors1StrForm = myScanner.nextLine();
        ArrayList<Double> coors1 = getIntListFromStr(coors1StrForm);

        System.out.println("Enter coordinates for second line (x1 y1 x2 y2)");
        String coors2StrForm = myScanner.nextLine();
        ArrayList<Double> coors2 = getIntListFromStr(coors2StrForm);

        myScanner.close();

        printLinesIntersect(coors1, coors2);

    }

    public static void printLinesIntersect(ArrayList<Double> coors1, ArrayList<Double> coors2)
    {
        // Get the slope of each line
        double slope1 = (coors1.get(3) - coors1.get(1)) / (coors1.get(2) - coors1.get(0));
        double slope2 = (coors2.get(3) - coors2.get(1)) / (coors2.get(2) - coors2.get(0));

        // Get boolean variables to check if one line is vertical or both lines are vertical
        boolean oneVertical = (slope1 == Double.POSITIVE_INFINITY || slope1 == Double.NEGATIVE_INFINITY) || (slope2 == Double.POSITIVE_INFINITY || slope2 == Double.NEGATIVE_INFINITY);
        boolean bothVertical = (slope1 == Double.POSITIVE_INFINITY || slope1 == Double.NEGATIVE_INFINITY) && (slope2 == Double.POSITIVE_INFINITY || slope2 == Double.NEGATIVE_INFINITY);

        // if both lines are vertical then print they're parallel - vertical
        if (bothVertical)
        {
            System.out.println("parallel - both vertical");
        }

        // if one line is vertical but the other is
        else if (oneVertical && !bothVertical)
        {
            System.out.println("intersecting - one vertical");
        }

        // otherwise both lines are inclined
        else
        {
            if (slope1 == slope2)
            {
                System.out.println("parallel");
            }

            else
            {
                System.out.println("intersecting");
            }
        }
    }

    public static ArrayList<Double> getIntListFromStr(String numsStrForm)
    {
        String[] numsSplittedList = numsStrForm.split(" ");
        ArrayList<Double> nums = new ArrayList<Double>();

        for (String digit : numsSplittedList)
        {
            double trueDigit = Double.valueOf(digit);
            nums.add(trueDigit);
        }

        return nums;
    }
}