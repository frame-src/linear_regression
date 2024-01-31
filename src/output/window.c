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

int clc_max(int * n, int len)
{
    int max = n[0];
    for ( int i = 0; i < len ; i++)
        max = (max < n[i] ? max : n[i]);
} 

int *normalize_points( int *p_x, int* p_y, int len)
{
    int *rtrn = malloc(3 * sizeof(int));
    int max_y, max_x;
    max_y = calculate_max (p_y, len);
    max_x = calculate_max (p_x, len);

    for (int i = 0 ; i< len ; i++){

    }
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

    int * points = normalize_points(NULL, 3);

    fprintf(file,"P3\n%i %i\n255\n",IMG_WIDTH,IMG_HEIGHT);
    for (int j = 0; j < IMG_HEIGHT; ++j){
        for (int i = 0; i < IMG_WIDTH; ++i){
            if ( i  == origin[0] || j == IMG_HEIGHT - origin[0] ||
                 i <= origin[0] - 3 && i <= origin[0] && origin[1]%10 == 0)
                fprintf(file,"%i %i %i\n", axes[0], axes[1], axes[2]);
            else if (  )
                continue;
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