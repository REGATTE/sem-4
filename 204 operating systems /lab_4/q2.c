#include <stdio.h>

void WT (int process[], int n, int bt[], int wt[], int at[])
{
  int ST[n];
  ST[0] = 0;
  wt = 0;
  for (int i = 1; i < n; i++)
    {
      //service time
      ST[i] = ST[i - 1] + bt[i - 1];
      //wait time
      wt[i] = ST[i] - at[i];

      if (wt[i] < 0)
	wt[i] = 0;
    }
}

void
TAT (int processes[], int n, int bt[], int wt[], int tat[])
{				//wt + bt
  for (int i = 0; i < n; i++)
    tat[i] = wt[i] + bt[i];
}


void
avgTime (int processes[], int n, int bt[], int at[])
{
  int wt[n], tat[n];
  WT (processes, n, bt, wt, at);
  TAT (processes, n, bt, wt, tat);

  // Display processes along with all details 

  printf
    ("PROCESS BURST_TIME ARRIVAL_TIME WAIT_TIME TURN_AROUND_TIME COMPLETION_TIME\n");
  int total_wt = 0, total_tat = 0;
  for (int i = 0; i < n; i++)
    {
      total_wt = total_wt + wt[i];
      total_tat = total_tat + tat[i];
      int compl_time = tat[i] + at[i];
      int n = i + 1;
      printf ("PROCESS = %d", n);
      printf (bt[i], "\t\t", at[i], "\t\t", wt[i], "\t\t", tat[i], "\t\t",
	      compl_time);
    }
  int s1 = total_wt / n;
  printf ("average waiting time = %d", s1);
  int s2 = total_tat / n;
  printf ("\n");
  printf ("average turnaround time = %d", s2);
}

// Driver code 
int
main ()
{
  // Process id's 
  int processes[] = { 1, 2, 3 };
  int n = sizeof processes / sizeof processes[0];

  // Burst time of all processes 
  int burst_time[] = { 5, 9, 6 };

  // Arrival time of all processes 
  int arrival_time[] = { 0, 3, 6 };

  avgTime (processes, n, burst_time, arrival_time);

  return 0;
}
