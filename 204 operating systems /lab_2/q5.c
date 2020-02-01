#include <stdio.h>
#include <string.h>
int main(int argc, const char  * argv[]){
    char example[100];
    strcpy(example,  "HI");
    strcat(example, " BYE");
    printf("%s\n", example);
    return 0;
}
