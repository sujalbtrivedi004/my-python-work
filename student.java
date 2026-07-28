import java.io.*;

public class student {

    class sujal {
        int sub1, sub2, sub3, total;

        // ✅ constructor name = class name
        sujal(int s1, int s2, int s3) {
            sub1 = s1;
            sub2 = s2;
            sub3 = s3;
        }

        void displayresult() {
            total = sub1 + sub2 + sub3;
            System.out.println("Total = " + total);
            System.out.println("Per = " + total / 3);
        }
    }

    public static void main(String[] args) {
        student outer = new student();              // outer class object
        sujal s = outer.new sujal(70, 80, 90);      // inner class object
        s.displayresult();
    }
}

