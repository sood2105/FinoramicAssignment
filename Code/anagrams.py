class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        anagram_words=dict()
        n=len(A)
        for i in range(n):
            original_word=A[i]
            sorted_word="".join(sorted(list(original_word)))
            if sorted_word in anagram_words:
                anagram_words[sorted_word].append(i+1)
            else:
                anagram_words[sorted_word]=[i+1]
        ans=[]
        for i in anagram_words:
            ans.append(anagram_words[i])
        return ans
            