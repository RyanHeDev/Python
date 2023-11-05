
# Print is your friend

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# use = instead of ==
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"Your total words: {total_words}")
