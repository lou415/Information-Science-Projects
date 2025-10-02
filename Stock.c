#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    int stock = 10;
    int num_bought = 0;

    while(num_bought < stock){
        num_bought++;
        
        if(stock - num_bought > 5){
            printf("So far we're ok\n");
        }
        else if (stock - num_bought > 3)
        {
            printf("Hmmm, getting a little worried.\n");
        }
        else if (stock - num_bought != 0)
        {
            printf("ORDER NOW!\n");
        }
        else{
            printf("We're fucked; it's all sold out!\n");
        }
        
    }

    return 0;
}