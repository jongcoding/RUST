import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int sum =0;
        sc.nextLine();
        String b = sc.nextLine();
        int[] digits =new int[b.length()];
        for (int i = 0; i < b.length(); i++) {
            digits[i] = b.charAt(i) - '0';
        }
        int result0=a*digits[2];
        int result1=a*digits[1];
        int result2=a*digits[0];
        sum+=result0;
        sum+=result1*10;
        sum+=result2*100;
        System.out.println(result0);
        System.out.println(result1);
        System.out.println(result2);
        System.out.println(sum);

    }
}
