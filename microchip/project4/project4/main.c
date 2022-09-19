#include <stdio.h>
#include "c4mlib.h"
#define student_ini {0}
typedef struct{
	char name[20];
	long int studentID;
	int8_t score[3];
} student;
void swap(int *a, int *b);
int main(void)
{
   C4M_DEVICE_set();
   int i, j, sum[5];
   student student_data[5]=student_ini,*p[6];
	int bytes=sizeof(student_data[0]);
	for(i=0;i<5;i++)
	{
		p[i]=&student_data[i];
		HMI_snget_struct("i8_20,i32_1,i8_3",bytes,&student_data[i]);
		sum[i]=student_data[i].score[0]+student_data[i].score[1]+student_data[i].score[2];
	}
   for(i=5;i>0;i--)
   {
		for(j=0;j<(i-1);j++)
		{
			if(sum[j]>sum[j+1])
			{
				swap(&sum[j], &sum[j+1]);
				p[5]=p[j];
				p[j]=p[j+1];
				p[j+1]=p[5];
			}
		}
   }
   for(i=0;i<5;i++){
	HMI_snput_struct("i8_20,i32_1,i8_3",bytes,p[i]);}
	return 0;
}


void swap(int *a, int *b)
{
	int tmp;
	tmp=*a;
	*a=*b;
	*b=tmp;
}


