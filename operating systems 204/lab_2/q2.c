#include <stdio.h>

int main(){
    int n = 0, rev = 0, rem;
    printf("enter a number: ");
    scanf("%d", &n);

    while(n != 0){
        rem = n%10;
        rev = rev *10 + rem;
        n /= 10;
    }
    printf("%d reversed number: ", rev);
    return 0;
}
