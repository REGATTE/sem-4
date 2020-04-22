"""

Ex2 Dharmendra the talented athlete

Dharmendra is a talented Athlete who is capable of jumping 1 meter, 2 meter and 3 meters distance. Now given a distance X, what is the count C of total number of ways to cover this distance X starting from 0. For example if N = 3 then output C = 4 as possibilities are [1,1,1], [1,2], [2,1], [3] If N = 4 then C = 7. Possibilities are [1,1,1,1], [1,2,1], [2,1,1], [1,1,2], [2,2], [3,1], [1,3]

Input Format

3

Constraints

NA

Output Format

4

"""
#include <iostream> 
using namespace std; 
const int MAXN = 1e6 + 1;

int main() { 
    int dp[MAXN];
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    int n; cin >> n;
    for(int i = 3;i <= n;i++) {
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1];
    }

    cout << dp[n] << '\n';
}
