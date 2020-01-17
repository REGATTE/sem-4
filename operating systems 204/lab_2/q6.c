#include <stdio.h>
int main (){
  int n = 0, i, mark=0;
  printf ("enter a number: ");
  scanf ("%d", &n);

  for (i = 2; i <= n / 2; ++i){
      if (n % i == 0){
	    mark = 1;
	    break;}}
      if (n == 1){
	    printf("1 is not a prime, or a composite number");
      }
      else{
	    if (mark == 0)
	      printf ("%d is a prime number", n);
	    else
	      printf ("%d is not a prime number", n);
  }
  return 0;
}
