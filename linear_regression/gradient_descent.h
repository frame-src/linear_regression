#ifndef GRADIENT_DESCENT_H
#define GRADIENT_DESCENT_H

/*
    pass
*/

#include "rss.h"
#include "stdlib.h"

int price[13] = {3650,3800,4400,4450,5250,5350,5800,5990,5999,6200,6390,6390,6600};
int km[13] = {240000, 139800,150500, 185530, 176000, 114800,166800,89000, 144500,84000,82029,63060,7400};
int len = 13;


void *gradient_descent();
float learning_rate();



#endif