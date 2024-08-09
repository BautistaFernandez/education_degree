text = input("Type a text: ")

# Letter counter
def count_letters(text):
    letters = sum(1 for char in text if char.isalpha())
    return letters

# Word counter
def count_words(text):
    words = text.split()
    return len(words)

# Sentence counter
def count_sentences(text):
    sentences = sum(1 for char in text if char in ['.', '?', '!'])
    return sentences

def main():
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # L and S formula for Coleman-Liau index
    L = (letters / words) * 100.0
    S = (sentences / words) * 100.0

    # Coleman-Liau index
    X = (0.0588 * L) - (0.296 * S) - 15.8
    index = round(X)

    # Check index to print
    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

main()
