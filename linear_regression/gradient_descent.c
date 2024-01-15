
#include "gradient_descent.h"

float learning_rate()
{
    return (1);
}


void *gradient_descent()
{
    float min = 1;
    float prmtrs[2] = {1,0};

    while( min != 0 || min > 0.009) {
        float *tmp = calculate_derivative_rss(price, km, len, prmtrs);
        prmtrs[0] = tmp[0];
        prmtrs[1] = tmp[1];
        min = calculate_rss(price, km, len, prmtrs);
    }
}