#include <stdio.h>
#include "c4mlib.h"

uint8_t keybroad(void); int time(int y);
void change(uint8_t new,uint8_t *w,uint8_t *x,uint8_t *y,uint8_t *z);
void write(uint8_t data1,uint8_t data2,uint8_t data3,uint8_t data4);

int main(void){
	C4M_DEVICE_set();
	
	REGFPT(&DDRB,255,0,0x70);
	REGFPT(&DDRE,0x18,0,0x18);
	REGFPT(&DDRD,255,0,0xff);
	REGFPT(&PORTB,0x70,0,0x70);
	REGFPT(&PORTE,0x18,0,0);
	REGFPT(&PORTD,255,0,0);
	
	uint8_t data_tmp=0;
	uint8_t data1=0x00,data2=0x00,data3=0x00,data4=0x00;
	
	while(1)
	{
		data_tmp=0;
		data_tmp=keybroad();
		if(data_tmp!=0)
		{
		printf("%d\n",data_tmp);
		change(data_tmp,&data1,&data2,&data3,&data4);
		write(data1,data2,data3,data4);
		}
	}
}

uint8_t keybroad(void)
{
	uint8_t data=0;
	uint8_t data2 = 0b00001111;
	uint8_t data3 = 0b00011000;
	int trans[4][4];
	trans[0][0]=0,trans[1][0]=10,trans[2][0]=11,trans[3][0]=15;
	trans[0][1]=1,trans[1][1]=2,trans[2][1]=3,trans[3][1]=14;
	trans[0][2]=4,trans[1][2]=5,trans[2][2]=6,trans[3][2]=13;
	trans[0][3]=7,trans[1][3]=8,trans[2][3]=9,trans[3][3]=12;
	

	REGPUT(&DDRE,1,&data3);
	REGPUT(&DDRD,1,&data2);
	REGFPT(&DDRB,112,0,112);
	REGFPT(&PORTE,24,0,0);
	REGFPT(&PORTD,24,0,0);

	int tmp;
		int A=1;
		for(int n=0;n<4;n++)
		{
			REGFPT(&PORTB,0x70,0,0x70);
			REGFPT(&PORTE,0x18,0,0x00);
			REGFPT(&PORTD,0x0f,0,A);
			REGFPT(&PORTE,0x18,0,0xff);
			A<<=1;
			REGFPT(&DDRD,0xf0,0,data);
			REGFGT(&PIND,0xf0,0,&data);
			for(int j=4;j<8;j++)
			{
				
				if(data==time(j))
				{
					tmp=trans[n][j-4];
				}
			}
			do
			{
				REGFGT(&PIND,240,0,&data);
			}
			while (data!=0);
		}
	return(tmp);
}

int time(int y){
	int ans=1;
	int i;
	for( i=0;i<y;i++)
	{
		ans*=2;
	}
	
	return(ans);
}

void change(uint8_t new,uint8_t *w,uint8_t *x,uint8_t *y,uint8_t *z)
{
	*z=*y;
	*y=*x;
	*x=*w;
	*w=new;
}

void write(uint8_t data1,uint8_t data2,uint8_t data3,uint8_t data4)
{
	REGFPT(&DDRD,255,0,0xff);
	REGFPT(&PORTB,0x70,0,0x00);
	REGFPT(&PORTE,255,0,0x10);
	REGFPT(&PORTD,255,0,data1);
	REGFPT(&PORTE,255,0,0x00);
	REGFPT(&PORTB,0x70,0,0x40);
	REGFPT(&PORTE,255,0,0x10);
	REGFPT(&PORTD,255,0,data2);
	REGFPT(&PORTE,255,0,0x00);
	REGFPT(&PORTB,0x70,0,0x20);
	REGFPT(&PORTE,255,0,0x10);
	REGFPT(&PORTD,255,0,data3);
	REGFPT(&PORTE,255,0,0x00);
	REGFPT(&PORTB,0x70,0,0x60);
	REGFPT(&PORTE,255,0,0x10);
	REGFPT(&PORTD,255,0,data4);
	REGFPT(&PORTE,255,0,0x00);
}



// int main(void)
// {
// 	C4M_DEVICE_set();
// 	REGFPT(&DDRD,255,0,255);
// 	REGFPT(&DDRB,0x70,0,0x70);
// 	REGFPT(&DDRE,0x18,0,0x18);
// 	REGFPT(&PORTB,0x70,0,0x30);
// 	REGFPT(&PORTE,255,0,0x10);
// 	REGFPT(&PORTD,255,0,0x02);
// 	REGFPT(&PORTE,255,0,0x00);
// 	printf(".\n");
// }