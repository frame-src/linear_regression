
#include "gradient_descent.h"
#include "utils.h"

float learning_rate()
{
    return (1);
}
// price;
int price[13] = {3650,3800,4400};//,4450,5250,5350,5800,5990,5999,6200,6390,6390,6600};
int km[13] = {240000, 139800,150500};//, 185530, 176000, 114800,166800,89000, 144500,84000,82029,63060,7400};
int len = 13;

/*
    q = mx - y
*/
float init_intercept( float x_m, float y_m, float slope)
{
    return ((slope * x_m) - y_m);
}

/*
    N: sum (x_i - x_m) ( y_i - y_m)
    D: sum (x_i - x_m)^2    
*/
float init_slope (int *x, int *y, float x_m, float y_m, int len)
{
    float num = 0;
    float den = 0;

    for ( int i = 0; i < len; i ++){
        num += (x[i] - x_m) * (y[i] - y_m);
        den += square(x[i] - x_m);
    }
    return (num / den);
}


float *ordinary_least_squares( void *x, void *y, int len, float *prms)
{
    float y_m = mean(y, len);
    float x_m = mean(x, len);

    prms[0] = init_slope(x, y, x_m,y_m, len);
    prms[1] = init_intercept(x_m, y_m, prms[0]);
    printf("%f, %f\n", prms[0], prms[1]);
    return prms;
}

void gradient_descent()
{
    float min = 1;
    float *prms;

    prms = malloc ( sizeof(float) * 2);
    prms = ordinary_least_squares(km, price, len, prms);
    
    while( min != 0 || min > 0.009) {
        float *tmp = calculate_derivative_rss(km, price, len, prms);
        prms[0] = tmp[0];
        prms[1] = tmp[1];
        min = calculate_rss( km, price, len, prms);
        break;
    }
    printf("min %f \n", min);
    free (prms);
    // printf("%f,%f ", prmtrs[0], prmtrs[1]);
}