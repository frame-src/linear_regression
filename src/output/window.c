#include <stdio.h> 
#include <stdlib.h>
#define IMG_WIDTH 256
#define IMG_HEIGHT 256

int print_image() 
{
    FILE *file = fopen("./graphs/test.ppm", "w");
    if (file == NULL) {
        printf("Error opening the file.\n");
        exit(1); // Indicates an error
    }
    fprintf(file,"P3\n%i %i\n255\n",IMG_WIDTH,IMG_HEIGHT);

    for (int j = 0; j < IMG_HEIGHT; ++j) {
        for (int i = 0; i < IMG_WIDTH; ++i) {
            int r = 248;
            int g = 124;
            int b = 86;
            fprintf(file,"%i %i %i\n", r, g, b);
        }
    }
    fclose(file);
    return 1;
}


int main () 
{
    return print_image();
}