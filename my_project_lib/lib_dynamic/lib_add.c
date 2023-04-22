#include <stdio.h>
#include "calc.h"

void add(int x, int y)
{
	printf("Addition of %d and %d is %d\n", x, y , x + y);
}



void cent_to_farh(float temp_f, float temp_c, char line_text[50]) {
	printf("Input a temperature (in Centigrade): ");
	fgets(line_text, sizeof(line_text), stdin);
	sscanf(line_text, "%f", &temp_c);

	temp_f = ((9.0 / 5.0) * temp_c) + 32.0;
	printf("%f degrees Fahrenheit.\n", temp_f);

}

