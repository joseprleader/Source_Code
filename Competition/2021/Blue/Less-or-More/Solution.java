// # Intercollegiate Programming Competition 2021 Blue Track Problem 7
// Less or More

import java.util.Scanner;
import java.util.ArrayList;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter count, integers separated by a space: ");
        int n = scan.nextInt();
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i < n; i++) {
            list.add(scan.nextInt());
        }
        scan.close();

        int count = 0;
        for(int i = 0; i < list.size() -1; i++) {
            for(int j = i + 1; j < list.size(); j++) {
                if(list.get(i) > list.get(j)) {
                    count++;
                    break;
                }
            }
        }
        
        System.out.println(count);
    }
}