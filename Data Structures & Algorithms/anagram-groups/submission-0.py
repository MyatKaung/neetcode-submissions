class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a dictionary to group anagrams
        groups ={}
        #loop through each word in the input list
        for word in strs:
            #create a list of 26 zeros for letters a to z
            count =[0]*26
            for char in word:
                index= ord(char)-ord('a')
                count[index]+=1

            signature = tuple(count)
            if signature not in groups:
                groups[signature]=[]
            groups[signature].append(word)
        
        return list(groups.values())




            
        