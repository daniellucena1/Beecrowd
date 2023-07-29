#include <stdio.h>

int main(){
    int n, i;
    float x, y, z, media;
    scanf("%d", &n);
    for(i = 0; i < n; i++){
        scanf("%f %f %f", &x, &y, &z);
        media = ((x * 2) + (y * 3) + (z * 5)) / 10;
        printf("%.1f\n", media);
    }
    return 0;
}