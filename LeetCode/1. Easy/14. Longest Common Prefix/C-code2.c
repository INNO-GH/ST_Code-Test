char *longestCommonPrefix(char **strs, int strsSize)
{	// Don't make additional str but just use first string only method
	for(int c=0;; ++c)
	{
		if(strs[0][c] == '\0') // the longest common prefix is the first string
			return strs[0]; // Just check the first string!!  
		for(int s=1; s<strsSize; ++s)
		{
			if(strs[s][c] != strs[0][c])
			{
				strs[0][c] = '\0';
				return strs[0];
			}
		}
	}
}
