import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long A,B,V;
        A=sc.nextLong();
        B=sc.nextLong();
        V=sc.nextLong();
        long day=(V-A)/(A-B);
        if((V-A)%(A-B)!=0) {
            day++;
        }
        day++;
        System.out.println(day);
    }
}
