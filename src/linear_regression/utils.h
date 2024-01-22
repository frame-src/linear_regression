#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>
#include <stdlib.h>

float square(float a);
float line_equation(float m, float q, float x);
float mean(int *n, int len);
void *safe_malloc(int size);

#endif