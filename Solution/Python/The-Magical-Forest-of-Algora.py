print('Welcome to the Magical Forest of Algora!')


import itertools
import random
# Define the dance moves
dance_words = ['Twirl', 'Leap', 'Spin']

# Generate all possible combinations of the dance words
dance_combinations = [''.join(p) for p in itertools.product(dance_words, repeat=2)]
print(dance_combinations)

# Define the effects for each dance move
dance_moves = [
    'Fireflies light up the forest.',
    'Gentle rain starts falling.',
    'A rainbow appears in the sky.',
    'The wind starts to blow.',
    'The sun shines brightly.',
    'The moon appears in the sky.',
    'Stars twinkle in the night sky.',
    'A gentle snowfall begins.',
    'A mist rolls in from the forest.',
]

dance_moves = dict(zip(dance_combinations, dance_moves))
print(dance_moves)

# Define the dance sequences for each creature
lox_moves = ['Twirl', 'Leap', 'Spin', 'Twirl', 'Leap']
drako_moves = ['Spin', 'Twirl', 'Leap', 'Leap', 'Spin']

# Initialize the state of the forest
forest_state = 'Normal'

# Perform the dance sequences
# Define the number of sequences
num_sequences = 5

# Perform the dance sequences
for i in range(num_sequences):
    # Get the current dance move
    dance_move = random.choice(lox_moves) + random.choice(drako_moves)
    
    # Get the effect of the dance move
    effect = dance_moves.get(dance_move, 'Nothing happens.')

    
    # Update the state of the forest based on the effect
    if effect == 'Fireflies light up the forest.':
        forest_state = 'Magical with fireflies'
    elif effect == 'Gentle rain starts falling.':
        forest_state = 'Magical with rain'
    elif effect == 'A rainbow appears in the sky.':
        forest_state = 'Magical with rainbow'
    elif effect == 'The wind starts to blow.':
        forest_state = 'Magical with wind'
    elif effect == 'The sun shines brightly.':
        forest_state = 'Magical with sun'
    elif effect == 'The moon appears in the sky.':
        forest_state = 'Magical with moon'
    elif effect == 'Stars twinkle in the night sky.':
        forest_state = 'Magical with stars'
    elif effect == 'A gentle snowfall begins.':
        forest_state = 'Magical with snowfall'
    elif effect == 'A mist rolls in from the forest.':
        forest_state = 'Magical with mist'
    else:
        forest_state = 'Normal'
    
    # Display the state of the forest
    print(f'Sequence {i+1}: {forest_state}')