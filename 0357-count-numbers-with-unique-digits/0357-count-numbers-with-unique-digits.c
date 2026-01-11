int countNumbersWithUniqueDigits(int n) {
    
    unsigned int ans = 0;
    if (n==0) return 1;

    switch (n){

        case 8:
            ans = ans + 9*9*8*7*6*5*4*3;
        case 7:
            ans = ans + 9*9*8*7*6*5*4;
        case 6:
            ans = ans + 9*9*8*7*6*5;
        case 5:
            ans = ans + 9*9*8*7*6;
        case 4:
            ans = ans + 9*9*8*7;
        case 3:
            ans = ans + 9*9*8;
        case 2:
            ans = ans + 9*9;
        case 1:
            ans = ans + 10;
        case 0:
            ans = ans + 0;
    }
    return ans;

}