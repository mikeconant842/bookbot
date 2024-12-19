def main():
    filename = "books/frankenstein.txt"
    with open(filename) as f:
       text = f.read()

    word_count = getWordCount(text)
    char_counts = getCharacterCount(text)
     
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document\n")
    sorted_char_counts = dict(sorted(char_counts.items(), key=lambda x: x[1], reverse=True))
    for char in sorted_char_counts:
        print(f"The '{char}' character was found {sorted_char_counts[char]} times")
    print("--- End report ---")

def getWordCount(text):
    words = text.split()
    return len(words)

def getCharacterCount(text):
    char_counts = dict()
    lower_text = text.lower()
    for c in lower_text:
        if c.isalpha():
            if c in char_counts:
                char_counts[c] += 1
            else:
                char_counts[c] = 1
    return char_counts


main()