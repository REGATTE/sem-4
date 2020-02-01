#include<stdio.h>

void WT(int processes[], int n, int bt[], int wt[])
{
//waiting time
    wt[0]=0; //arrival time is 0, hence wait time for P1 is 0
    for (int  i = 1; i < n ; i++ )  
        wt[i] =  bt[i-1] + wt[i-1];
}

void TA( int processes[], int n, int bt[], int wt[], int tat[]) 
{ 
    //turn around time
    // add all
    for (int  i = 0; i < n ; i++)  
        tat[i] = bt[i] + wt[i];  
}  

void AT( int processes[], int n, int bt[])  
{  
    int wt[n], tat[n], total_wt = 0, total_tat = 0;  
    
    
    WT(processes, n, bt, wt);  
    
    
    TA(processes, n, bt, wt, tat);  
    

    printf("Processes   Burst time   Waiting time   Turn around time\n");  
    
    for (int  i=0; i<n; i++) 
    {  
        total_wt = total_wt + wt[i];  
        total_tat = total_tat + tat[i];  
        printf("   %d ",(i+1)); 
        printf("       %d ", bt[i] ); 
        printf("       %d",wt[i] ); 
        printf("       %d\n",tat[i] );  
    }  
    int s=(float)total_wt / (float)n; 
    int t=(float)total_tat / (float)n; 
    printf("Average waiting time = %d",s); 
    printf("\n"); 
    printf("Average turn around time = %d ",t);  
}  
 
int main()  
{  
    int processes[] = { 1, 2, 3};  
    int n = sizeof processes / sizeof processes[0];  
    
    //Burst time of all processes  
    int  burst_time[] = {24,3,4};  
    
    AT(processes, n,  burst_time);  
    return 0;  
}