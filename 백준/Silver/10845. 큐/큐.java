import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        int n = Integer.parseInt(br.readLine());

        int[] queue = new int[n];

        int front = 0, rear = 0;


        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            switch (s) {
                case "push":
                    int x = Integer.parseInt(st.nextToken());
                    queue[rear++] = x;
                    break;
                case "pop":
                    if (front == rear) {
                        bw.write("-1\n");
                    } else {
                        bw.write(queue[front++] + "\n");
                    }
                    break;
                case "size":
                    bw.write((rear - front) + "\n");
                    break;
                case "empty":
                    bw.write((front == rear ? "1" : "0") + "\n");
                    break;
                case "front":
                    if (front == rear) {
                        bw.write("-1\n");
                    } else {
                        bw.write(queue[front] + "\n");
                    }
                    break;
                case "back":
                    if (front == rear) {
                        bw.write("-1\n");
                    } else {
                        bw.write(queue[rear - 1] + "\n");
                    }
                    break;
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
