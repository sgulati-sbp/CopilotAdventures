import itertools

# Define the dance moves
dance_words = ['Twirl', 'Leap', 'Spin']

# Generate all possible combinations of the dance words
dance_combinations = [''.join(p) for p in itertools.product(dance_words, repeat=2)]
print(dance_combinations)

# Define the effects for each dance move
dance_effects = [
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

dance_effects = dict(zip(dance_combinations, dance_effects))

print(dance_effects)

# Extend the dance_moves dictionary with the new combinations and their effects
for i, dance_move in enumerate(dance_combinations):
    dance_move[dance_move] = dance_effects[i % len(dance_effects)]