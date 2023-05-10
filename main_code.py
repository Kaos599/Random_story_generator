# Define the story template with blanks for the words to fill in
story = """
It was a {adjective1} morning. I woke up at 8:30 am and checked my {noun1}. I had a {adjective2} message from my {noun2}. It said: "Hey, don't forget to attend the {noun3} class today. It's very {adjective3} and you might learn something {adjective4}."

I quickly got ready and grabbed my {noun4}. I ran to the {noun5} and hopped on the {noun6}. I reached the {noun7} just in time for the class. The teacher was {verb1} on the board. He looked at me and said: "Welcome, {name1}. I hope you are ready for a {adjective5} lesson today. We are going to learn about {noun8}s and how they work."

I sat down and opened my {noun9}. I was feeling {emotion1} and {emotion2}. I wondered what the class would be like. I hoped it would be {adjective6} and not {adjective7}.
"""

# Define a list of words to ask for
words = ["adjective1", "noun1", "adjective2", "noun2", "noun3", "adjective3", "adjective4", "noun4", "noun5", "noun6", "noun7", "verb1", "name1", "adjective5", "noun8", "noun9", "emotion1", "emotion2", "adjective6", "adjective7"]

# Start the game
print("Welcome to random story generator game!")
print("Please enter some words to fill in the blanks of the story.")

# Get the inputs from the user using a dictionary comprehension
inputs = {word: input(f"Enter a {word}: ") for word in words}

# Print a message
print("Here is your crazy random story:")

# Fill in the blanks with the inputs using str.format
print(story.format(**inputs))
print(inputs)
