import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        int n = Integer.parseInt(br.readLine());

        int[] stack = new int[n];
        int top = -1;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            switch (s) {
                case "push":
                    int x = Integer.parseInt(st.nextToken());
                    stack[++top] = x;
                    break;
                case "pop":
                    if (top == -1) {
                        bw.write("-1\n");
                    } else {
                        bw.write(stack[top] + "\n");
                        top--;
                    }
                    break;
                case "size":
                    bw.write((top + 1) + "\n");
                    break;
                case "empty":
                    bw.write((top == -1 ? "1" : "0") + "\n");
                    break;
                case "top":
                    if (top == -1) {
                        bw.write("-1\n");
                    } else {
                        bw.write(stack[top] + "\n");
                    }
                    break;
                default:
                    break;
            }
        }
      
        bw.flush();
        bw.close();
        br.close();
    }
}
