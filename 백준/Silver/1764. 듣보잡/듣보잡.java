import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());


        HashSet<String> heardSet = new HashSet<>();
        for (int i = 0; i < n; i++) {
            heardSet.add(br.readLine());
        }


        ArrayList<String> resultList = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String name = br.readLine();
            if (heardSet.contains(name)) {
                resultList.add(name);
            }
        }

       //정렬 딸깍~
        Collections.sort(resultList);

        bw.write(resultList.size() + "\n");
        for (String name : resultList) {
            bw.write(name + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
