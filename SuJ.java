public class SuJ {
    import java.io.*;

class stt
{
    static void printdata()
    {
        System.out.println("static method");
    }
}

public class staticex {

    // ✅ static variables (CLASS LEVEL)
    static int a = 10;
    static int b = 20;

    static void display()
    {
        System.out.println(a);
        System.out.println(b);
    }

    static
    {
        System.out.println("static block executed");
    }

    public static void main(String[] args) {
        display();
        stt.printdata();
    }
}

}
