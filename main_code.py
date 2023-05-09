# A simple madlibs generator game in Python

# Define the story template with blanks for the words to fill in
story = """
It was a {} morning. I woke up at 8:30 am and checked my {}. I had a {} message from my {}. It said: "Hey, don't forget to attend the {} class today. It's very {} and you might learn something {}."

I quickly got ready and grabbed my {}. I ran to the {} and hopped on the {}. I reached the {} just in time for the class. The teacher was {} on the board. He looked at me and said: "Welcome, {}. I hope you are ready for a {} lesson today. We are going to learn about {}s and how they work."

I sat down and opened my {}. I was feeling {} and {}. I wondered what the class would be like. I hoped it would be {} and not {}.
"""

# Define a list of words to ask for
words = ["adjective", "noun", "adjective", "noun", "noun", "adjective", "adjective", "noun", "noun", "noun", "noun", "verb", "name", "adjective", "noun", "noun", "emotion", "emotion", "adjective", "adjective"]

# Start the game
print("Welcome to the madlibs generator game!")
print("Please enter some words to fill in the blanks of the story.")

# Get the inputs from the user using a list comprehension
inputs = [input(f"Enter a {word}: ") for word in words]

# Print a message
print("Here is your crazy random story:")

# Fill in the blanks with the inputs using str.format
print(story.format(*inputs))
