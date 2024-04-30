def findMostFrequentWord(str):
    words = str.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    most_frequent_word = max(word_count, key=word_count.get)
    return most_frequent_word