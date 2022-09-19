#include "c4mlib.h"

int ExtPort_get(uint8_t in);
void ExtPort_put(uint8_t out,int in,int MASK);

int main(void){
	C4M_DEVICE_set();
	uint8_t data=0x00;
	uint8_t input=0x00;
	uint8_t output=0xff;
	int i=0,num=0,tmp=0,MASK=0xff;
	REGFPT(&DDRB,0x70,0,0x70);
	REGFPT(&DDRE,0x18,0,0x18);
	REGFPT(&PORTB,255,0,0xff);
	uint8_t a=0b00000001;
	while(1)
	{
		ExtPort_put(output,a,MASK);
		
	}
}


int ExtPort_get(uint8_t in)
{
	int tmp;
	REGPUT(&DDRD,1,&in);
	REGFPT(&PORTE,0x08,0,0x08);
	REGGET(&PIND,1,&tmp);
	REGFPT(&PORTE,0x08,0,0x00);
	return(tmp);
}

void ExtPort_put(uint8_t out, int in,int MASK)
{
	REGFPT(&DDRD,255,0,out);
	REGFPT(&PORTE,0x10,0,0x00);
	REGFPT(&PORTD,MASK,0,in);
	REGFPT(&PORTE,0x10,0,0xff);
}

// #include "c4mlib.h"
// 
// int ExtPort_get(uint8_t in);
// void ExtPort_put(uint8_t out,int in,int MASK);
// 
// int main(void){
// 	C4M_DEVICE_set();
// 	uint8_t data=0x00;
// 	uint8_t input=0x00;
// 	uint8_t output=0xff;
// 	int i=0,num=0,tmp=0,MASK=0xff;
// 	REGFPT(&DDRB,0x70,0,0x70);
// 	REGFPT(&DDRE,0x18,0,0x18);
// 	REGFPT(&PORTB,255,0,0x00);
// 	int c=7;
// 	data=ExtPort_get(input);//取得起點
// 	num=128/data;
// 	while (num!=1)//差
// 	{
// 		i++;
// 		num=num/2;
// 	}
// 	
// 	while(i>0)
// 	{
// 		tmp=data;
// 		for(int k=0;k<i+1;k++)
// 		{
// 			ExtPort_put(output,tmp,MASK);
// 			_delay_ms(200);
// 			tmp<<=1;
// 		}
// 		num=1;
// 		
// 		for(int j=0;j<c;j++)
// 		{
// 			num=num*2;
// 		}
// 		c--;
// 		MASK=MASK-num;
// 		i--;
// 	}
// 	ExtPort_put(output,data,data);
// }
// 
// 
// int ExtPort_get(uint8_t in)
// {
// 	int tmp;
// 	REGPUT(&DDRD,1,&in);
// 	REGFPT(&PORTE,0x08,0,0x08);
// 	REGGET(&PIND,1,&tmp);
// 	REGFPT(&PORTE,0x08,0,0x00);
// 	return(tmp);
// }
// 
// void ExtPort_put(uint8_t out, int in,int MASK)
// {
// 	REGFPT(&DDRD,255,0,out);
// 	REGFPT(&PORTE,0x10,0,0x00);
// 	REGFPT(&PORTD,MASK,0,in);
// 	REGFPT(&PORTE,0x10,0,0xff);
// }
// 
