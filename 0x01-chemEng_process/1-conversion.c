#include <stdio.h>

int main() {
    double value, result;
    char fromUnit, toUnit;

    printf("Enter a value to convert: ");
    scanf("%lf", &value);

    printf("Enter the unit to convert from (m, mm, ft, yd): ");
    scanf(" %s", &fromUnit);

    printf("Enter the unit to convert to (m, mm, ft, yd): ");
    scanf(" %s", &toUnit);

    switch (fromUnit) {
        case 'm':
            switch (toUnit) {
                case 'm':
                    result = value;
                    break;
                case 'mm':
                    result = value * 1000;
                    break;
                case 'ft':
                    result = value * 3.28084;
                    break;
                case 'yd':
                    result = value * 1.09361;
                    break;
                default:
                    printf("Invalid unit to convert to.\n");
                    return 1;
            }
            break;
        case 'mm':
            switch (toUnit) {
                case 'm':
                    result = value / 1000;
                    break;
                case 'mm':
                    result = value;
                    break;
                case 'ft':
                    result = value / 1000 * 3.28084;
                    break;
                case 'yd':
                    result = value / 1000 * 1.09361;
                    break;
                default:
                    printf("Invalid unit to convert to.\n");
                    return 1;
            }
            break;
        case 'ft':
            switch (toUnit) {
                case 'm':
                    result = value / 3.28084;
                    break;
                case 'mm':
                    result = value / 3.28084 * 1000;
                    break;
                case 'ft':
                    result = value;
                    break;
                case 'yd':
                    result = value / 3;
                    break;
                default:
                    printf("Invalid unit to convert to.\n");
                    return 1;
            }
            break;
        case 'yd':
            switch (toUnit) {
                case 'm':
                    result = value / 1.09361;
                    break;
                case 'mm':
                    result = value / 1.09361 * 1000;
                    break;
                case 'ft':
                    result = value * 3;
                    break;
                case 'yd':
                    result = value;
                    break;
                default:
                    printf("Invalid unit to convert to.\n");
                    return 1;
            }
            break;
        default:
            printf("Invalid unit to convert from.\n");
            return 1;
    }

    printf("%.2lf %c is %.2lf %c\n", value, fromUnit, result, toUnit);

    return 0;
}

