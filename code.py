import sys
import re

def read_text(file_path):
    """Read the content of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the text file.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(file_path, "r") as text_file:
            return text_file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)

def get_sentences(text):
    """Split the text into sentences.

    Args:
        text (str): The input text.

    Returns:
        list: A list of sentences.
    """
    sentences = re.split(r'\. ', text)
    return sentences

def get_words(text):
    """Extract words from the text, removing non-alphanumeric characters.

    Args:
        text (str): The input text.

    Returns:
        list: A list of cleaned words.
    """
    words = []
    sentences = get_sentences(text)
    for sentence in sentences:
        sentence_words = sentence.split()
        for word in sentence_words:
            clean_words = re.sub(r"[^\w\s]", "", word)
            words.append(clean_words)
    return words

def key_for_order_sentences(sentence):
    """Key function for ordering sentences based on word length."""
    words = get_words(sentence)
    return len(words)

def order_sentences(text):
    """Order sentences by their word length and print the top and bottom sentences."""
    sentences_to_order = get_sentences(text)
    
    # Sort the sentences in reverse order based on their length in words
    sentences_to_order.sort(key=key_for_order_sentences, reverse=True)
    
    # Create a list with the "ordinal numbers"
    ordinal = ["longest", "second longest", "third longest", "fourth longest", "fifth longest", "sixth longest","shortest"]
    
    # Initialize a variable to keep track of the loops
    i = 0
    
    # Iterate through each sentence from the ordered sentences
    for sentence in sentences_to_order:
        words = get_words(sentence)
        
        # Nested if loop
        if i <= 6:  # condition to print the sentences in order
            # Print the ordinal number and the number of words in the sentence
            print("The", ordinal[i], "sentence has", len(words), "words")
            print()
            i += 1  # Increase by one the index of ordinal to change for each iteration of the for loop
        else:
            break  # If i > 6, break and exit

def get_longest_words(text, N):
    """Get the N longest unique words from the text.

    Args:
        text (str): The input text.
        N (int): The number of longest words to retrieve.

    Returns:
        list: A list of the N longest unique words.
    """
    words = get_words(text)

    # Convert all words to lowercase to avoid considering them as separate words
    words_lower = [word.lower() for word in words]

    # Convert the list into a set to eliminate duplicates
    sorted_words_set = set(words_lower)
    # Convert the set to a list to be able to sort it
    sorted_words_list = list(sorted_words_set)
    # Sort the list based on length
    sorted_words = sorted(sorted_words_list, key=len, reverse=True)
    # Get the N longest words
    five_longest = sorted_words[:N]
    
    # Sort the longest N words alphabetically
    unique_words_alphabetically = sorted(five_longest)
    return unique_words_alphabetically

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    my_text = read_text(input_file_path)
    
    # Count the number of sentences from my file using the function
    sentences = get_sentences(my_text)
    # Print the number of sentences
    print("This text contains", len(sentences), "sentences")
    print()  # Aesthetics whitespace

    # Get the list of words from my file using the function
    words = get_words(my_text)
    # Print the number of words
    print("This text contains", len(words), "words")  # Print number of words
    print()  # Aesthetics whitespace

    # Get the first 5 longest words from my file
    longest_sorted = get_longest_words(my_text, 5)
    longest_sorted_string = ", ".join(longest_sorted)
    
    # Print the words
    print("The 5 longest words in the text are", longest_sorted_string)

    # Get the ordered sentences from my text using the function 
    order_sentences(my_text)

if __name__ == "__main__":
    main()
