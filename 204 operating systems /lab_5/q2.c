#include <stdio.h>
#include <stdlib.h>

struct Process
{
    int id;
    int burst_t;
    int priority;
} ;

void shuffle(int *array, size_t n)
{
    if (n > 1)
    {
        size_t i;
        for (i = 0; i < n - 1; i++)
        {
            size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
            int t = array[j];
            array[j] = array[i];
            array[i] = t;
        }
    }
}

int main()
{
    srand(0);
    int n = 8;
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};
    shuffle(arr, n);

    struct Process p[n],temp;
    printf("Input:\nProcessID\tBurstTime\tPriority\n");
    for (int i = 0; i < n; i++)
    {
        p[i].id = rand() % 100;
        p[i].burst_t = rand() % 10 + 1;
        p[i].priority = arr[i];
        printf("%d\t\t%d\t\t%d\n", p[i].id, p[i].burst_t, p[i].priority);
    }

     for (int i = 1; i < n; i++)
      for (int j = 0; j < n - i; j++) {
         if (p[j].priority > p[j + 1].priority) {
            temp = p[j];
            p[j] = p[j + 1];
            p[j + 1] = temp;
         }
      }

    int wait_t[n], turn_t[n], avg_wait = 0, avg_tat = 0;
    wait_t[0] = 0;
    turn_t[0] = p[0].burst_t + wait_t[0];
    avg_tat = turn_t[0];
    printf("\n\nOutput:\nPriority\tProcessID\tBurstTime\tWait Time\tTurn Around Time\n");
    printf("%d\t\t%d\t\t%d\t\t%d\t\t%d\n", p[0].priority, p[0].id, p[0].burst_t, wait_t[0], turn_t[0]);
    for (int i = 1; i < n; i++)
    {
        wait_t[i] = p[i - 1].burst_t + wait_t[i - 1];
        turn_t[i] = p[i].burst_t + wait_t[i];
        avg_wait += wait_t[i];
        printf("%d\t\t%d\t\t%d\t\t%d\t\t%d\n", p[i].priority, p[i].id, p[i].burst_t, wait_t[i], turn_t[i]);
    }
    return 0;
}

// gcc q1.c && ./a.out
