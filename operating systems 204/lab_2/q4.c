#include <stdio.h>
int main(){
    int n = 0, a, i;
    printf("enter the range of natural numbers: ");
    scanf("%d", &n);
    for(i=1; i<=n; ++i){
        a = (i * (i+1))/2;
    }
    printf("sum = %d", a);
    return 0;
}
