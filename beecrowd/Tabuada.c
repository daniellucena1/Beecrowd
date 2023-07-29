#include <stdio.h>

int main(){
    int n, i, produto;
    scanf("%d", &n);
    for(i = 1; i <= 10; i++){
        produto = i * n;
        printf("%d x %d = %d\n", i, n, produto);
    }
    return 0;
}