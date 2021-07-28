#include <stdio.h>
int main()

{
int readings[] = {8129, 7154, 7312, 6287, 5908};
int sum = 0;
int avg;
for (int i=1; i<=5; i++)
sum += readings[i];
avg = sum / 5;
printf("Mean reading = %d\n", avg);
return 0;
}

