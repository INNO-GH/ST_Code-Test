int romanToInt(char * s){
// We should watch Roman left to right
// If next number is smaller than previous, It's not instances
// But when reverse situation, We should recognize it as instances
// I will use switch function because I get char data for choosing number
    int sum=0, i=0;
    while(i <= (strlen(s)-1)){ // I can easily get string's length by function 'strlen'
        switch(s[i]){
            case 'M':
                sum=sum+1000;
                i=i+1;
                break;
            case 'D':
                sum=sum+500;
                i=i+1;
                break;
            case 'C': // Exceptional Case
                if(s[i+1]=='D'){
                    sum=sum+400;
                    i=i+2; // i must jump already completed number    
                }
                else if(s[i+1]=='M'){
                    sum=sum+900;
                    i=i+2;
                }     
                else{
                    sum=sum+100;
                    i=i+1;
                }
                break;
            case 'L':
                sum=sum+50;
                i=i+1;
                break;
            case 'X':
                if(s[i+1]=='L'){
                    sum=sum+40;
                    i=i+2;
                }    
                else if(s[i+1]=='C'){
                    sum=sum+90;
                    i=i+2;
                }
                else{
                    sum=sum+10;
                    i=i+1;
                }
                break;
            case 'V': 
                sum=sum+5;
                i=i+1;
                break;
            case 'I':
                if(s[i+1]=='V'){
                    sum=sum+4;
                    i=i+2;
                }    
                else if(s[i+1]=='X'){
                    sum=sum+9;
                    i=i+2;
                }
                else{
                    sum=sum+1;
                    i=i+1;
                }
                break;           
        }        
    }
    return sum;
}
