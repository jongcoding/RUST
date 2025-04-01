import java.util.Scanner;

public class Main {
    public static long fibo(int n) {
        if (n==0) {
            return 0;
        }
        else if (n<=2) {
            return 1;
        }
        int a=0;
        int b=1;
        int c=1;
        for(int i=2;i<=n;i++) {
            c=a+b;
            a=b;
            b=c;
        }
        return c;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(fibo(n));

    }
}
