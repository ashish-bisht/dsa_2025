import heapq


def top_k_frequent_words(words, k):
    word_dict = {}

    for word in words:
        if not word in word_dict:
            word_dict[word] = 1

        word_dict[word]+=1
    heap = []
    for key,value in word_dict.items():
        heapq.heappush(heap,(-value,key))

    result = [heapq.heappop(heap)[1] for _ in range(k)]
    return result

print(top_k_frequent_words(["i","love","leetcode","i","love","coding"], k = 2))

    
