#include "graph.h"
#include <math.h>

FILE* open_file( char *fpath)
{
    FILE *file = fopen(fpath, "w");
    if (file == NULL) {
        printf("Error opening the file.\n");
        exit(1);
    }
    return file;
}
int price[13] = {3500, 3650,3800,4400};
int km[13] = {100000, 240000, 139800,150500};

int calculate_max(int * n, int len)
{
    int max = n[0];
    for ( int i = 0; i < len ; i++)
        max = (max > n[i] ? max : n[i]);
    return max;
} 

int calculate_min(int * n, int len)
{
    int min = n[0];
    for ( int i = 0; i < len ; i++)
        min = (min < n[i] ? min : n[i]);
    return min;
} 

double *normalize_points( int *n, int len)
{
    double *normalized = malloc(len * sizeof(double));
    double max, min;
    max = (double)calculate_max (n, len);
    min = (double)calculate_min (n, len);

    for (int i = 0 ; i<len ; i++){
        normalized[i] = ((n[i] - min) / (max - min));
    }
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

    double *x = normalize_points(price, 4);
    double *y = normalize_points(km, 4);
    fprintf(file,"P3\n%i %i\n255\n",IMG_WIDTH,IMG_HEIGHT);
    for (int j = 0; j < IMG_HEIGHT; ++j){
        int index = 0;
        for (int i = 0; i < IMG_WIDTH; ++i){
            if ( i  == origin[0] || j == IMG_HEIGHT - origin[0] )
                 fprintf(file,"%i %i %i\n", axes[0], axes[1], axes[2]);      
            else if ( ( i >= origin[0] - 3 && i <= origin[0] && j%10 == 0 )||
                      ( j <= IMG_HEIGHT - origin[1] + 3 && j >= IMG_HEIGHT - origin[0] && i%10 == 0 && i > 1))
                fprintf(file,"%i %i %i\n", axes[0], axes[1], axes[2]);
            else if (ceil(x[index] * IMG_WIDTH) == i) {
                // ceil(y[index] * IMG_HEIGHT);
                printf("value of i: \t%d \t norm: %f \nvalue of j: \t%d \t norm: %f \n", i, ceil(x[index] * IMG_WIDTH), j,ceil(y[index] * IMG_HEIGHT));
                fprintf(file,"%i %i %i\n", axes[0], axes[1], axes[2]);
                index++;
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