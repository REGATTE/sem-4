#include <stdio.h>
int main(){
    int i, n, a1=0, a2=1, a;
    printf("enter the range of fibonacci seq: ");
    scanf("%d", &n);
    printf("series: ");
    for (i=1; i<=n; ++i){
        printf("%d", a1);
        a = a1 + a2;
        a1 = a2;
        a2 = a;
    }
    return 0;
}
