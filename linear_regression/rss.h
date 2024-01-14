#ifndef RSS_H
#define RSS_H

/*
    RESIDUAL SQUARED SUM;
    is a type of loss function, 
    evaluate the difference beetween 
    the awaited value and the measured one;
    S = ( R - E )^2
*/

float estimate_slope(int x, int y, float a, float b);
float estimate_intercept(int x, int y, float a, float b);
float *calculate_derivative_rss(int *x, int *y, int len, float * values);

#endif