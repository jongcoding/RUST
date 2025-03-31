import java.io.*;

public class Main {
    // 커스텀 빠른 입력 클래스
    static class Reader {
        final private int BUFFER_SIZE = 1 << 16; // 버퍼 크기
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        // 정수를 빠르게 읽는 메서드
        public int nextInt() throws Exception {
            int ret = 0;
            byte c = read();
            // 공백 문자(스페이스, 개행 등) 건너뛰기
            while (c <= ' ') {
                c = read();
            }
            boolean neg = (c == '-');
            if (neg) {
                c = read();
            }
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg) {
                return -ret;
            }
            return ret;
        }

        // 버퍼에서 한 바이트씩 읽기
        private byte read() throws Exception {
            if (bufferPointer == bytesRead) {
                fillBuffer();
            }
            return buffer[bufferPointer++];
        }

        // 버퍼 채우기
        private void fillBuffer() throws Exception {
            bytesRead = din.read(buffer, 0, BUFFER_SIZE);
            if (bytesRead == -1) {
                buffer[0] = -1;
            }
            bufferPointer = 0;
        }
    }

    public static void main(String[] args) throws Exception {
        Reader in = new Reader();
        int a = in.nextInt();
        int b = in.nextInt();
        System.out.println(a + b);
    }
}
