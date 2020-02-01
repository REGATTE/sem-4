#include <stdio.h>
int main(){
    int n = 0, rev = 0, rem, original;
    printf("enter an integer: ");
    scanf("%d", &n);
    original = n;

    while
    (n != 0){
        rem = n%10;
        rev = rev*10 + rem;
        n /= 10;
    }
    if(original == rev)
        printf("%d is a palindrome.",original);
    else
        printf("%d is not a palindrome.", original);

    return 0;
}