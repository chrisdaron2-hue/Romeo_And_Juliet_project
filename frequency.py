from romeo_and_juliet import PLAY


def get_words(text):
    return text.split()


def words_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def top_n_words(freq, n):
    # Sort items by frequency (value), descending
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Print top n words with their frequency
    for word, count in sorted_words[:n]:
        print(word, count)

def main():
    words = get_words(PLAY)
    counted_words = words_frequency(words)
    top_n_words(counted_words, n=50)


if __name__ == '__main__':
    main()


