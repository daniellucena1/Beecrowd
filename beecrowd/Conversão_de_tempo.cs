using System;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
      int segundos = Convert.ToInt32(Console.ReadLine());
      int[] tipos = {3600, 60};
      for(int i = 0; i < tipos.Length; i++){
        int horas = segundos/tipos[i];
        segundos = segundos%tipos[i];
        Console.Write("{0}:", horas );
      }
      Console.WriteLine("{0}", segundos);
    }
    }
}