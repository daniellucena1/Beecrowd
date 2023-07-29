#include <stdio.h>

int main(){
    int n, con, a;
    scanf("%d", &n);
    con = 0;
    a = 1;
    while(con < n){
        printf("%d %.0f %.0f\n", a, pow(a,2), pow(a,3));
        printf("%d %.0f %.0f\n", a, pow(a,2) + 1, pow(a,3) + 1);
        a++;
        con++;
    }
    return 0;
}