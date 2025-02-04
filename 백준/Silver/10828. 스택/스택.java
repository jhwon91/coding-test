
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private Node top;

    public class Node{
        int data;
        Node next;

        public Node(int data){
            this.data = data;
            this.next = null;
        }
    }

    public void push(int data){
        Node newNode = new Node(data);
        newNode.next = top;
        top = newNode;
    }

    public void pop(){
        if(top == null){
            System.out.println(-1);
        } else {
            System.out.println(top.data);
            top = top.next;
        }
    }

    public void size(){
        if(top == null){
            System.out.println(0);
            return;
        }

        int count = 1;
        Node current = top;
        while(current.next != null){
            count++;
            current = current.next;
        }

        System.out.println(count);
    }

    public void empty(){
        if(top == null){
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }

    public void top(){
        if(top == null){
            System.out.println(-1);
        } else {
            System.out.println(top.data);
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Main stack = new Main();

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine()," ");
            String type = st.nextToken();

            switch (type){
                case "push":
                    int data = Integer.parseInt(st.nextToken());
                    stack.push(data);
                    break;
                case "pop":
                    stack.pop();
                    break;
                case "size":
                    stack.size();
                    break;
                case "empty":
                    stack.empty();
                    break;
                case "top":
                    stack.top();
                    break;
            }
        }
    }
}
