#include <bits/stdc++.h>

using namespace std;
typedef pair <int, int> intPair;

int triplets(vector <int> arr, int n)
{
    // map.find() returns iterator to the passed 'key' element
    // If not present then it returns iterator 'map.end()'
	map < int, int > dict;
	map < intPair, int > check;

	int count = 0;

	sort(arr.begin(),arr.end());

	for(int i=0; i<n; i++)
	{
	    // Check if element is present or not
	    // If not then add it to the dictionary
	    // Key - 'arr[i]'
        if (dict.find(arr[i]) == dict.end())
			dict[arr[i]] = 1;
	}

	for(int j=0; j<(n-1); j++)
	{
		int q = j + 1;
		while (q < arr.size())
		{

			// Check for the sum and duplicate
			// Pair represented as {a,b}
			if ( dict.find(arr[j] + arr[q]) != dict.end() && check[{arr[j], arr[q]}] != arr[j] + arr[q])
			{
				count += 1;
				check[{arr[j], arr[q]}] = arr[j] + arr[q];
			}

			q += 1;
		}
	}

	return count;
}

int main()
{
    int n, count;
    cin>>n;

	vector<int>arr(n);
	for(int i=0; i<n; i++)
        cin>>arr[i];

	count = triplets(arr, n);

	cout<<count;

	return 0;
}
