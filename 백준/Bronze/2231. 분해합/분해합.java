import java.util.Scanner;

public class Main {


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = 0;


        int digits = String.valueOf(n).length();
        int start = Math.max(1, n - digits * 9);

        for (int m = start; m < n; m++) {
            if (m + cal(m) == n) {
                a = m;
                break;
            }
        }
        System.out.println(a);
    }
    private static int cal(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}
