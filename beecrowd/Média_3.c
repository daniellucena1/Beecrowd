#include <stdio.h>

int main(){
    float nota_1, nota_2, nota_3, nota_4, media, novamedia, nota_extra;
    scanf("%f %f %f %f", &nota_1, &nota_2, &nota_3, &nota_4);
    media = ((nota_1 * 2) + (nota_2 * 3) + (nota_3 * 4) + (nota_4 * 1)) / 10;
    if(media >= 7.0){
        printf("Media: %.1f\n", media);
        printf("Aluno aprovado.\n");
    }
    else if(media < 5.0){
        printf("Media: %.1f\n", media);
        printf("Aluno reprovado.\n");
    }
    else{
        printf("Media: %.1f\n", media);
        printf("Aluno em exame.\n");
        scanf("%f", &nota_extra);
        printf("Nota do exame: %.1f\n", nota_extra);
        novamedia = (media + nota_extra) / 2;
        if(novamedia >= 5){
            printf("Aluno aprovado.\n");
            printf("Media final: %.1f\n", novamedia);
        }
        else if(novamedia < 5.0){
            printf("Aluno reprovado\n");
            printf("Media final: %.1f", novamedia);
        }
    }
    return 0;
}