char * longestCommonPrefix(char ** strs, int strsSize){
// 1. Pick first char of first word
// 2. Check the others whether they have also same word
// 3. If have -> save and next char & else -> stop
  int i, j; // i is picking in the first string / j is for comparing with the other strings
  char* save = (char*)malloc(sizeof(char)*(strlen(strs[0])+1)); // Use malloc for unknown len
  for(i=0;i<strlen(strs[0]);i++){ // First word's char
    for(j=1;j<strsSize;j++){ // compare it with the other words
      if(strs[0][i]!=strs[j][i]) {
        save[i]='\0'; // !!! Don't forget last '\0' when we return string array !!!
        return save;
      }   
    }
    save[i]=strs[0][i];
  } 
  save[i]='\0'; // !!! Don't forget last '\0' when we return string array !!!
  return save;
}
