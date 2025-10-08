#include <stdio.h>
#include <stdlib.h>

int main(void){
    int secret_num = 5;
    int guess;

    while (guess != secret_num){
        printf("Enter a number: ");
        scanf("%d", &guess);
        printf("Not quite the secret number, guess again!\n");
    }
    printf("Yes, you guessed the secret number!\n");
    return 0;
}