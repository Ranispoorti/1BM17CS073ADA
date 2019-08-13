#include<iostream>
using namespace std;

int main()
{
	int n,a[50],max=0;
	cout<<"Enter value of n";
    cin>>n;

        for(int i=0;i<n;i++)
          {
            cin>>a[i];
             if(a[i]>max)
              max=a[i];
          }

    cout<<"Greatest is"<<max;
return 0;
}	