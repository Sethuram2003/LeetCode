class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        n=len(words)
        if n==1:
            return True
        word_dict={}
        for word in words:
            sub=len(word)
            for ch in range(sub):
                if word[ch] not in word_dict.keys():

                    word_dict[word[ch]]=1
                else:
                    word_dict[word[ch]]=word_dict[word[ch]]+1
        
        
        for val in word_dict.values():
            if val%n!=0:
                return False
        return True

        