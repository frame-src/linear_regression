
#include "gradient_descent.h"

float learning_rate()
{
    return (1);
}

int price[13] = {3650,3800,4400,4450,5250,5350,5800,5990,5999,6200,6390,6390,6600};
int km[13] = {240000, 139800,150500, 185530, 176000, 114800,166800,89000, 144500,84000,82029,63060,7400};
int len = 13;


float calculate_slope(float x, float y, float x_m, float y_m)
{
    float num = (x - x_m) * ( y - y_m );
    float den = square (x - x_m);
    return num / den;
}

float calculate_intercept( float slope, float x, float y)
{
    return (y - (x * slope));
}

float *least_square(int *x, int *y, int len)
{
    float slp;
    float m_x = mean(x, len);
    float m_y = mean(y, len);
    float *prmtrs = (float *)safe_malloc(sizeof(float) * 2);

    slp = 0;
    for(int i = 0; i < len; i++)
        slp += calculate_slope(x[i], y[i], m_x, m_y);
    prmtrs[0] = slp;
    prmtrs[1] = calculate_intercept(slp, m_x, m_y);
    return prmtrs;
}

void gradient_descent()
{
    float min = 1;
    // float prmtrs[2] = {1,0};
    printf("INITIAL VALUE: km: %i,  price: %i \n ", km[1], price[1]);
    float *prmtrs = least_square(km, price, len);
    printf("INITIAL PARAMS: %f,%f \n", prmtrs[0], prmtrs[1]);
    int a = 1;
    while( min != 0 || min > 0.009) {
        float *tmp = calculate_derivative_rss(price, km, len, prmtrs);
        if(a == 1)
            // printf("GRADIENT RESULT: %f, %f \n ", tmp[0], tmp[1]);
        a = 0;
        prmtrs[0] = tmp[0];
        prmtrs[1] = tmp[1];
        // printf("RSS calculat:  %f, %f\n",prmtrs[0], prmtrs[1]);
        min = calculate_rss(price, km, len, prmtrs);
        free(tmp);
        // break;
    }
    printf("min = %f\n", min);
}