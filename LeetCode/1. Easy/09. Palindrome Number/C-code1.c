bool isPalindrome(int x){
// 1. If x<0 -> Not Palidrome, x=0 -> Palidrome
    if(x<0) return false;
    if(x==0) return true;
// 2. Check number of Digit (Be careful about overflow)
    long long int a=10, b=1;
    while(!((a>x)&&(x>=b))){
        a=a*10;
        b=b*10;
    }
// 3. Check Symmetry by using %
    b=10;
    while(a>=b){
        if(((x%a-x%(a/10))/(a/10))!=((x%b-x%(b/10))/(b/10))) return false;
        a=a/10;
        b=b*10;
    }
    return true;
}

/* Extracting digit that I wanted = (x%a-x%(a/10))/(a/10) */ 
