def is_palindrome(sentence):
    # Remove punctuation and spaces from the sentence
    cleaned_sentence = ''.join(char for char in sentence if char.isalnum()).lower()
    
    # Check if the cleaned sentence is equal to its reverse
    return cleaned_sentence == cleaned_sentence[::-1]

# Test the function
sentence = "A man, a plan, a canal, Panama!"
if is_palindrome(sentence):
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")
