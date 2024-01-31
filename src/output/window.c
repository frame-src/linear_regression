#include "graph.h"

FILE* open_file( char *fpath)
{
    FILE *file = fopen(fpath, "w");
    if (file == NULL) {
        printf("Error opening the file.\n");
        exit(1);
    }
    return file;
}
int price[13] = {3650,3800,4400};
int km[13] = {240000, 139800,150500};

int calculate_max(int * n, int len)
{
    int max = n[0];
    for ( int i = 0; i < len ; i++)
        max = (max < n[i] ? max : n[i]);
    return max;
} 

double *normalize_points( int *n, int len)
{
    double *normalized = malloc(len * sizeof(double));
    int max;
    max = calculate_max (n, len);

    for (int i = 0 ; i<len ; i++)
        normalized[i] = (double)((n[i] / max) +1);
    return normalized;
}

/*
    PPM header:
 
    P3
    width_value height_value
    255

*/  
int print_image() 
{
    FILE *file = open_file("./graphs/test.ppm");
    int bg[] = COLOR_BG;
    int axes[] = COLOR_AXES;
    int origin[] = COORD_ORIGIN;

    double *x = normalize_points(price, 3);
    double *y = normalize_points(km, 3);
    int index = 0;

    fprintf(file,"P3\n%i %i\n255\n",IMG_WIDTH,IMG_HEIGHT);
    for (int j = 0; j < IMG_HEIGHT; ++j){
        for (int i = 0; i < IMG_WIDTH; ++i){
            if ( i  == origin[0] || j == IMG_HEIGHT - origin[0] ||
                 (i >= origin[0] - 3 && i <= origin[0] && origin[1]%10 == 0))
                fprintf(file,"%i %i %i\n", axes[0], axes[1], axes[2]);
            else if ((int)(x[index] * IMG_WIDTH) == i){
                if( (int)(x[index] * IMG_WIDTH) ==  j)
                    fprintf(file,"%i %i %i\n", axes[0], axes[1], axes[2]);
            }
            else 
                fprintf(file,"%i %i %i\n", bg[0], bg[1], bg[2]);
        }
    }
    fclose(file);
    return 1;
}


int main () 
{
    return print_image();
}