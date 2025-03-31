import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a,b;
        String str;
        str = sc.nextLine();
        String[] mobNum= str.split(" ");
        a= Integer.parseInt(mobNum[0]);
        b= Integer.parseInt(mobNum[1]);

        System.out.println(a+b);
    }
}