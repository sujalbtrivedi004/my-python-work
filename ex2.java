import java.io.*;

class ex2
{
    public static void main(String args[])
    {
        int[] a = {1, 2, 3};

        try
        {
            System.out.println("a[1] = " + a[1]);
        }
        catch (ArrayIndexOutOfBoundsException e)
        {
            System.out.println("Index not available");
        }
    }
}

