import sys

def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    # Check if text is provided as command line argument
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <text>")
        sys.exit(1)

    # Extract text from command line argument
    text = ' '.join(sys.argv[1:])

    # Count words
    word_count = count_words(text)

    # Display the word count
    print("Word count:", word_count)
