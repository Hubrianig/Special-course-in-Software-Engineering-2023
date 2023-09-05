# Function to count occurrences of a word in a string
def count_word_occurrences(text, word):
    word = word.lower()  # Convert to lowercase for case-insensitive matching
    words = text.lower().split()
    return words.count(word)

# Read the content from file_to_read.txt
with open("file_to_read.txt", "r") as file:
    content = file.read()

# Count the occurrences of the word "terrible"
terrible_count = count_word_occurrences(content, "terrible")
print(f"Total occurrences of 'terrible': {terrible_count}")

# Split the content into words for replacement
words = content.split()
replaced_words = []
for i, word in enumerate(words):
    if word.lower() == "terrible":
        if i % 2 == 0:
            replaced_words.append("pathetic")
        else:
            replaced_words.append("marvellous")
    else:
        replaced_words.append(word)

# Join the modified words back into a string
modified_text = " ".join(replaced_words)

# Write the modified text to result.txt
with open("result.txt", "w") as result_file:
    result_file.write(modified_text)

print("Replacement complete. Modified text saved to result.txt")
