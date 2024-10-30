def get_frequency(words):
    unique_words = set(words)
    counts = {word: 0 for word in unique_words}
    for i in unique_words:
        for j in words:
            if i == j:
                counts[i] += 1
    return counts

if __name__ == '__main__':
    words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
    print(get_frequency(words))