#include <stdio.h>
#include <math.h>
#include "c4mlib.h"

/*float sqr(float x,int n);
int main(void)
{
	C4M_DEVICE_set();
	float x;
	int n;
	printf("Please keyin two numbers.\n");
	printf("x=?\n");
	scanf("%f",&x);
	printf("n=?\n");
	scanf("%d",&n);
	float return_value;
	return_value=sqr(x,n);
	printf("Ans=%f\n",return_value);
}

float sqr(float x,int n){
	float y=1;
	//y=pow(x,n);
	int i;
	for(i=0;i<n;i++){
			y=y*x;
	}
	return(y);
}*/

/*int swap(float *, float *);
int main(void){
	C4M_DEVICE_set();
	float a,b;
	printf("Please keyin two number.\n");
	printf("a=?\n");
	scanf("%f",&a);
	printf("b=?\n");
	scanf("%f",&b);
	printf("a=%g, b=%g\n", a, b);
	swap(&a,&b);
	printf("-----change------\n");
	printf("a=%g, b=%g\n", a, b);
}
int swap(float *c, float *d){
	float tmp;
	tmp=*c;
	*c=*d;
	*d=tmp;
}*/


int a,b,c,d;
float StateSpace(int ut);
int main(void){
	C4M_DEVICE_set();
	printf("a=?\n");
	scanf("%d",&a);
	printf("b=?\n");
	scanf("%d",&b);
	printf("c=?\n");
	scanf("%d",&c);
	printf("d=?\n");
	scanf("%d",&d);
	int i,ut;
	printf("u=?\n");
	scanf("%d",&ut);
	for(i=0;i<10;i++)
	{
		printf("%f\n",StateSpace(ut));
	}
}

float StateSpace(int ut){
	float yt;
	static int xt=0;
	xt=a*xt+b*ut;
	yt=c*xt+d*ut;
	return yt;
}