#include <stdio.h>

struct stock{
    float value;
    int stock_num;
    char stock_tag[3]; // 3 character tag used as shorthand in any player-facing ui
};

int main(){

    // defining a stock called iron
    struct stock iron;
    iron.value = 12.0f; // with a value of 12
    iron.stock_num = 12567; // and with 12567 of them 'existing'

    return 0;

    // I'm going to quickly prototype this in python just so I have a base to
    // work from.
}
