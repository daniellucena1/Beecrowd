using System;

class MyAplications
{
    static void Main(string[] args)
    {
        int i = 1, j = 60;
        for(int k = 0; k <= 12; k++)
        {
            Console.WriteLine("I={0} J={1}", i, j);
            i += 3;
            j -= 5;
        }
    }
}