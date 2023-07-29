using System;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
      int dias = Convert.ToInt32(Console.ReadLine());
      int[] tipos = {365, 30};
      for(int i = 0; i < tipos.Length; i++){
        int anos = dias/tipos[i];
        dias = dias%tipos[i];
        if(i == 0){
          Console.WriteLine("{0} ano(s)", anos);
        }
        else{Console.WriteLine("{0} mes(es)", anos);}
      }
      Console.WriteLine("{0} dia(s)", dias);
    }
    }
}