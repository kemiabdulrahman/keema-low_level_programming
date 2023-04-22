#include <stdio.h>
#include "calc.h"


int main(int argc, char **argv) {
int x = 13;
int y = 156;
    float temp_c, temp_f;
    char line_text[50];
    cent_to_farh(temp_f, temp_c, line_text);
add(x,y);
sub(x, y);
return (0);
}

