#include <stdio.h>

int main(int argc, char **argv) {


double value;
char inputUnit;

printf("Enter the value and unit you want to convert(e.g. 10 cm): ");
scanf("%lf %c", &value, &inputUnit);

switch (inputUnit) {
    case 'm':
        value = value * 1000;
        printf("%.2lf mm", value);
        break;
    case 'f':
        value = value / 3;
        printf("%.2lf yd", value);
        break;
    case 'y':
        value = value * 3;
        printf("%.2lf ft", value);
        break;
    default:
        printf("Invalid input unit. Please enter a valid unit (m, ft, yd)");
        break;
}
return 0;
}
