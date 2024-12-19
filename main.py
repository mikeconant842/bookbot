def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

    print(f"Frankenstein contains {getWordCount(file_contents)}")

def getWordCount(sample_text):
    words = sample_text.split()
    return len(words)

main()