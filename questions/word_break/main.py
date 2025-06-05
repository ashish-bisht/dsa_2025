s = "leetcode"
wordDict = ["leet","code"]

def word_break(s, wordDict):

    word_dict = set(wordDict)


    memo = {}


    def dp(current_index):
        if current_index == len(s):
            return True
        
        if current_index in memo:
            return memo[current_index]
        
        result = False
        for word in word_dict:
            word_length = len(word)

            if current_index + word_length <= len(s) and word == s[current_index:current_index+word_length]:
                if dp(current_index+word_length):
                    result = True
                    break

        
        memo[current_index] = result

        return result
    
    return dp(0)


print(word_break(s,wordDict))