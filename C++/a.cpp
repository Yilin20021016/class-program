#include <stdio.h>
#include <iostream>

int function(int x)//檢查質數
{
    int tmp=0;
    for(int i=2;i<=x;i++)
    {
        if(x%i==0)
        {
            tmp+=1;
        }
    }
    if(tmp==1)
    {
        return 1;//是質數
    }
    else
    {
        return 0;//不是質數
    }
}

int x=0;

void f2(int y, int array[])//儲存質數進array內
{
    array[x]=y;
    x++;
}

void f3(int start[],int end,int th)
{
    printf("%d's multiple:",start[th]);
    int mul=1;
    while(start[th]*mul<=end)
    {
        printf("%d ",start[th]*mul);
        mul++;
    }
    printf("\n");
}



int main()
 {
    while(1)
    {
        double num=0;
        x=0;
        int *array;
        int a=0;
        printf("Please keyin a number:\n");
        if(scanf("%lf",&num))//判定輸入是否為數字
        {
            if(num == (int)num && num>0)//判定輸入是否為正整數
            {
                for(int i=1;i<=num;i++)//檢查有多少質數
                {
                    if(function(i))
                    {
                        a+=1;
                    }
                }
                array=new int[a];
                for(int j=1;j<=num;j++)//存質數進array[]
                {
                    if(function(j))
                    {
                        f2(j,array);
                    }
                }
                for(int k=0;k<a;k++)
                {
                    printf("%d ",array[k]);
                }
                printf("\n");

                for(int l=0;l<a;l++)
                {
                    f3(array,num,l);
                }

                delete [] array;
            }
            else
            {
                printf("Float or Negative\n");
                while(getchar() != '\n')
                continue;
            }
        }
        else
        {
            printf("please keyin a NUMBER\n");
            while(getchar() != '\n')
            continue;
        }
        system("pause");
    }
    return 0;
}

