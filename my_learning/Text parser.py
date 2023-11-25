text = input("Enter some text: ").lower()
letters = []
for _ in range(3):
    letter = input("Enter a different letter each time: ").lower()
    letters.append(letter)

print("\nLETTER REPETITIONS:")
for l in letters:
    letter_repetition = text.count(l)
    print(f"We have found the letter {l} repeated {letter_repetition} times")

print("\nNUMBER OF WORDS:")
words = text.split()
print(f"We have found {len(words)} words in your text")

first_letter = text[0]
last_letter = text[-1]
print(f"The initial letter is {first_letter}, the final letter is {last_letter}\n")

print("INVERTED TEXT:")
reversed_words = list(reversed(words))
inverted_text = " ".join(reversed_words)
print(f"If we order your text backwards it will say: {inverted_text}")

print("\nLOOKING FOR THE WORD 'PYTHON':")
is_python = "python" in text
word_found_status = "was" if is_python else "was not"
print(f"The word 'python' {word_found_status} found in the text")
