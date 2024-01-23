#include "rss.h"
#include "utils.h"

/*  
    y = ax + b
    a = slope  &&  b = intercept
*/
float estimate_slope(int x, int y, float m, float q)
{
    float d = y - ( q + ( x * m));
    return( -2 * x * d );
}

/*  
    y = ax + b
    a = slope  &&  b = intercept
*/
float estimate_intercept(int x, int y, float m, float q)
{
    float d = y - ( q + ( x * m));
    return( -2 * d);
}

/*
    NOTE:
    values[ slope , intercept];
*/
float *calculate_derivative_rss(int *x, int *y, int len, float * values)
{
    int i = 0;
    float rss_inter, rss_slope;

    rss_inter = 0; 
    rss_slope = 1;

    while(i < len){
        rss_inter += estimate_intercept(x[i], y[i], values[0], values[1]);
        rss_slope += estimate_slope(x[i], y[i], values[0], values[1]);
        i++;
    }
    values[0] = rss_slope;
    values[1] = rss_inter;
    return values;
}


/*
    NOTE:
        values[0] = m;
        values[1] = q;

        (m = slope, q = intercept);
*/
float calculate_rss(int *x, int *y,int len, float *values)
{
    float rss = 0;
    // printf("Valie %f, %f\n",values[0], values[1]);
    for(int i = 0; i < len; i++){
        rss += square(y[i] - line_equation(values[0], values[1],x[i]));
    }
    // printf("RSS: %i \n", y[i]);
    return rss;
}
