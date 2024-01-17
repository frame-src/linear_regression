#include "utils.h"

float square(float n)
{
    return n * n;
}

float mean(float *n, int len)
{
    float sum = 0;
    for(int i = 0; i < len; i ++){
        sum += n[i];
    }
    return (sum / len);
}

float line_equation(float m, float q, float x)
{
    return ( m * x + q);
}

