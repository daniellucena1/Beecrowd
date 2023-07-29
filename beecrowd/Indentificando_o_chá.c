#include <stdio.h>

int main(){
    int tipo_cha, participantes[5], i, con, acm;
    scanf("%d", &tipo_cha);
    for(i = 0; i < 5; i++){
        scanf("%d", &participantes[i]);
    }
    con = 0;
    acm = 0;
    while(con < 5){
        if(participantes[con] == tipo_cha){
            acm++;
        }
        con++;
    }
    printf("%d\n", acm);
    return 0;
}