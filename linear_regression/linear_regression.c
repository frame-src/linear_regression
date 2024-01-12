#include "linear_regression.h"

float learning_rate(){
    return (1);
}

float estimated_value(float a, float b, float x){
    float y = a + b * x;
    return (y);
}

estimate_tetha_zero(int n){
    return( learning_rate() * (1 / n) ) * (  -1  * gradient());
}

// estimate(dpn) = theta[0] + (theta[1] ∗ dpn)
void *linear_regression(int *dpn, int *indpn, int buffer_len){
    float theta[2];
    float gamma = learning_rate();
    
    for(int i = 0; i < buffer_len; i++){
        theta[0] = learning_rate * (()/ buffer_len)
    }

    theta[0] = gamma +

    return (void *) value
}

