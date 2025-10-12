bool judgeCircle(char* moves) {
    int v = 0;
    int h = 0;
    for(char* i = moves; *i != '\0'; i++){
        if (*i == 'U') v++;
        else if (*i =='D') v--;
        else if (*i == 'R') h++;
        else h --;
    }
    return v == 0 && h == 0;
}