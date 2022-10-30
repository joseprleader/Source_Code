// Intercollegiate Programming Competition Blue Track 2021
// Challenge 8 It Add sUp

import java.util.*;
public class ItAddsUp {
    public static ArrayList<Integer> list = new ArrayList<Integer>();
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the desired sum, number of elements, each element: ");
        int sum = scan.nextInt();
        int n = scan.nextInt();

        for(int i = 0; i < n; i++) {
            list.add(scan.nextInt());
        }
        scan.close();
        //We compare the input and if the sum adds up, we save it in a new Pair object
        for(int i = 0; i < list.size() -1; i++) {
            for(int j = i + 1; j < list.size(); j++) {
                if(list.get(i) + list.get(j) == sum) {
                    Pair pair = new Pair(list.get(i), list.get(j), list);
                }
            }
        }
        ArrayList<Pair> pairs = Pair.getPairs();
        // We need to sort the pairs by the first element of the pair
        Collections.sort(pairs, new Comparator<Pair>() {
            @Override
            public int compare(Pair p1, Pair p2) {
                return p1.compareTo(p2);
            }
        });

        if(pairs.size() == 0) {
            System.out.println("No pairs found");
        } else {
            for(Pair pair : pairs) {
                System.out.println(pair.toString() + " found at " + pair.getLoc());
            }
        }
    }
}
// We Create a private class so we can store the pairs in a list
class Pair {
    int a;
    int b;
    //We store the location of the pair in the array
    private static ArrayList<Pair> pairs = new ArrayList<Pair>();

    private ArrayList<Integer> list;
    public Pair(int a, int b, ArrayList<Integer> list) {
        this.a = a;
        this.b = b;
        pairs.add(this);
        this.list = list;

    }
    public int getA() {
        return a;
    }
    public int getB() {
        return b;
    }
    public String toString() {
        return "(" + a + ", " + b + ")";
    }
    public String getLoc() {
        return "[" + (list.indexOf(a) +1) + "][" + (list.indexOf(b) +1) + "]";
    }
    public int getLocA() {
        return list.indexOf(a);
    }
    public int getLocB() {
        return list.indexOf(b);
    }
    public static ArrayList<Pair> getPairs() {
        return pairs;
    }
    //We override the compareTo method so we can sort the pairs and get the pairs in the right order
    public int compareTo(Pair p){
        if(this.getLocA() < p.getLocA()) {
            return -1;
        } else if(this.getLocA() > p.getLocA()) {
            return 1;
        } else {
            if(this.getLocB() < p.getLocB()) {
                return -1;
            } else if(this.getLocB() > p.getLocB()) {
                return 1;
            } else {
                return 0;
            }
        }
    }



}