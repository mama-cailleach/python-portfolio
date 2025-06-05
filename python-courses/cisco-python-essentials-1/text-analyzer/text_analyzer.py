import string

def get_text():
    print("Enter the text to analyze (end with a blank line):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return " ".join(lines)

def count_words(text):
    words = text.split()
    return len(words), words

def count_characters(text):
    return len(text)

def count_sentences(text):
    sentences = [s for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    return len(sentences)

def most_common_word(words):
    freq = {}
    for w in words:
        # Remove punctuation and lowercase the word
        word = w.strip(string.punctuation).lower()
        if word:
            freq[word] = freq.get(word, 0) + 1
    if not freq:
        return None, 0
    max_count = max(freq.values())
    most_common = [word for word, count in freq.items() if count == max_count]
    return most_common, max_count

def unique_words(words):
    s = set(w.strip(string.punctuation).lower() for w in words if w)
    return len(s)

def main():
    text = get_text()
    word_count, words = count_words(text)
    char_count = count_characters(text)
    sentence_count = count_sentences(text)
    unique_word_count = unique_words(words)
    most_common, freq = most_common_word(words)

    print("\nText Analysis Results:")
    print(f"Characters: {char_count}")
    print(f"Words: {word_count}")
    print(f"Unique words: {unique_word_count}")
    print(f"Sentences: {sentence_count}")
    if most_common:
        print(f"Most common word(s): {', '.join(most_common)} (appeared {freq} times)")
    else:
        print("No words found.")

if __name__ == "__main__":
    main()
