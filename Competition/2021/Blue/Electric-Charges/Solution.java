// Intercollegiate Programming Competition 2021 Blue Track Problem 1
// Electric Charges

// Import Scanner utility to get input from STDIN
import java.util.Scanner;

public class Solution
{
    public static void main(String args[])
    {
        // Create Scanner to get input from STDIN
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the KW hours used: ");

        // Get hours of consumption from STDIN
        int hours = scanner.nextInt();

        // Close scanner once we got all input from STDIN
        scanner.close();

        // Get the bill to be paid
        double billToPay = totalBill(hours);

        // Show the bill to STDOUT
        System.out.println("Amount owed is $" + billToPay);
    }

    public static double centsToDollars(double cents)
    {
        return cents / 100;
    }

    public static double roundUp(double num)
    {
        // Round a double to 2 decimal praces
        return Math.round(num * 100.0) / 100.0;
    }

    public static double totalBill(int hours)
    {
        // Bill to be paid
        double bill = 0;

        // Electricity rates to be paid
        double rate_before_1000 = centsToDollars(7.633);
        double rate_after_1000 = centsToDollars(9.259);

        // Add extra rate if hours are more than 1000
        if (hours > 1000)
        {
            int hours_after_1000 = hours - 1000;
            double bill_before_1000 = 1000 * rate_before_1000;
            double bill_after_1000 = hours_after_1000 * rate_after_1000;
            bill = bill_before_1000 + bill_after_1000;
        }

        else
        {
            bill = hours * rate_before_1000;
        }

        // round up the result
        return roundUp(bill);
    }
}