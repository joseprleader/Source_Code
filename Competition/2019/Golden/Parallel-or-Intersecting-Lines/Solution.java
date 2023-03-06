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

        /*
        
        GraphLine line1 = new GraphLine(coors1.get(0), coors1.get(1), coors1.get(2), coors1.get(3));
        GraphLine line2 = new GraphLine(coors2.get(0), coors2.get(1), coors2.get(2), coors2.get(3));
        
        boolean oneVertical = line1.getLineType().equals("Vertical") || line2.getLineType().equals("Vertical");
        boolean bothVertical = line1.getLineType().equals("Vertical") && line2.getLineType().equals("Vertical");

        if (oneVertical && !bothVertical)
        {
            System.out.println("intersecting - one vertical");
        }

        else if (oneVertical && bothVertical)
        {
            System.out.println("parallel - both vertical");
        }

        else
        {
            if (line1.getSlope() != line2.getSlope())
            {
                System.out.println("intersecting");
            }

            else
            {
                System.out.println("parallel");
            }
        }*/

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