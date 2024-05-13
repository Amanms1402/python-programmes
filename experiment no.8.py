from collections import Counter

file_path = input("Enter the path to the text file: ")
top_n = int(input("Enter the number of most frequent words to find: "))

try:
    with open(file_path, 'r') as file:
        text = file.read().lower()
        word_count = Counter(text.split())
        top_words = word_count.most_common(top_n)
        print(f"\nTop {top_n} most frequent words in the text:")
        for word, frequency in top_words:
            print(f"{word}: {frequency}")
except FileNotFoundError:
    print("File not found.")
