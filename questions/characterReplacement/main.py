def longest_character_replacement(s, k):
    left = 0
    freq = {}
    max_freq = 0
    max_length = 0
    # track max_freq character
    # check valid window : if  max character + k >=  window_lenth  
    for right in range(len(s)):

        cur_word = s[right]

        freq[cur_word] = freq.get(cur_word,0) + 1

        max_freq = max(max_freq, freq[cur_word])

        if (right -left +1) - max_freq > k:
            left_char = s[left]
            freq[left_char] -=1
            left +=1

        max_length = max(max_length, right-left+1)

    
    return max_length









print(longest_character_replacement(s = "ABAB", k = 2))
print(longest_character_replacement( s = "AABABBA", k = 1))
