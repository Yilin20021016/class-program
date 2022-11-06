#include <iostream>
#include <stdlib.h>
using namespace std;
char *strNcat(char *str1,char *str2, int n)
{
    int i,j;
    for(i=0;str1[i]!='\0';i++){};
    for(j=0;j<n;j++)
    {
        str1[i+j]=str2[j];
    }
    str1[i+j]='\0';
    return str1;
}

int main(void)
{
    char str1[] = "12345";
    char str2[] = "fuck you sb";
    cout << "7-1 strNcat(str1,str2,3)" << endl << "連接前:str1:" << str1 << endl << "連接前:str2:" << str2 << endl << "連接後:" << strNcat(str1,str2,11);
    return 0;
}
