
#include "gradient_descent.h"

int price[13] = {3650,3800,4400,4450,5250,5350,5800,5990,5999,6200,6390,6390,6600};
int km[13] = {240000, 139800,150500, 185530, 176000, 114800,166800,89000, 144500,84000,82029,63060,7400};
int len = 13;

float learning_rate()
{
    return (1);
}

/*
    ax + b;
*/
gradient_descent()
{
    float min;
    float prmtrs[2] = {1,0};

    while( min != 0 | min > 0.009){
        &prmtrs = calculate_derivative_rss(price, km, 13, prmtrs);
        min = calculate_rss;
    }
}