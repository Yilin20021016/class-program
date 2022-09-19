#include <bits/stdc++.h>
using namespace std;

int main()
{
    srand(time(NULL));
    int a = rand()%3;
    if(a==0)
        cout << "kuva";
    else if(a==1)
        cout << "xinshe";
    else
        cout << "i hotel";
    cout << "\n";
    system("pause");
    return 0;
}