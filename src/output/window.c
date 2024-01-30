#include <stdio.h> 
#include <stdlib.h>

#define IMG_WIDTH 256
#define IMG_HEIGHT 256
#define BG {248,124,86}

FILE* open_file( char *fpath)
{
    FILE *file = fopen(fpath, "w");
    if (file == NULL) {
        printf("Error opening the file.\n");
        exit(1);
    }
    return file;
}

int print_image() 
{
    FILE *file = open_file("./graphs/test.ppm");
    int rgb[] = BG;

    fprintf(file,"P3\n%i %i\n255\n",IMG_WIDTH,IMG_HEIGHT);
    for (int j = 0; j < IMG_HEIGHT; ++j) {
        for (int i = 0; i < IMG_WIDTH; ++i) {
            fprintf(file,"%i %i %i\n", rgb[0], rgb[1], rgb[2]);
        }
    }
    fclose(file);
    return 1;
}


int main () 
{
    return print_image();
}