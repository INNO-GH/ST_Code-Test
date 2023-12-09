bool isPalindrome(int x){
// First, Check a definitely false case
    if(x<0 || x!=0 && x%10 ==0 ) return false;
    int check=0;
    while(x>check){
        check = check*10 + x%10; // Check brings last digit one by one (Reversely) 
        x/=10; // then x will give last digit one by one to check
    }
    return (x==check || x==check/10); // Former is case for even digit
				     // later is case for odd digit
}

/* We should know that [%10 brings last digit] + [/10 remove last digit] */ 


