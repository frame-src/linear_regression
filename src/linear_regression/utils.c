#include "utils.h"
#include <stdbool.h>

float square(float n)
{
    return n * n;
}

float mean(int *n, int len)
{
    int sum = 0;
    for(int i = 0; i < len; i ++){
        sum += n[i];
    }
    return (sum / len);
}

void *safe_malloc(int size)
{
    void *mem = malloc(size);
    if (!mem)
        exit(1);
    return mem;
}

float line_equation(float m, float q, int x)
{
    // printf("line equation: %f %f %i \n", m, q, x);
    return ( m * x + q);
}

