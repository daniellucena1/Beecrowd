#include <stdio.h>

int main(){
    int I, J, con;
    I = 1;
    while(I <= 9){
        con = 0;
        J = 7;
        while(con < 3){
            printf("I=%d J=%d\n", I, J);
            con++;
            J -= 1;
        }
        I += 2;
    }
}