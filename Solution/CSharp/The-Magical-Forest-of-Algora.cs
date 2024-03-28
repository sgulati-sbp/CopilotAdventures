using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        Console.WriteLine("Welcome to the Magical Forest of Algora!");

        // Define the dance moves
        var danceWords = new List<string> { "Twirl", "Leap", "Spin" };

        // Generate all possible combinations of the dance words
        var danceCombinations = new List<string>();
        foreach (var word1 in danceWords)
        {
            foreach (var word2 in danceWords)
            {
                danceCombinations.Add(word1 + word2);
            }
        }
        Console.WriteLine(string.Join(", ", danceCombinations));

        // Define the effects for each dance move
        var danceEffects = new List<string>
        {
            "Fireflies light up the forest.",
            "Gentle rain starts falling.",
            "A rainbow appears in the sky.",
            "The wind starts to blow.",
            "The sun shines brightly.",
            "The moon appears in the sky.",
            "Stars twinkle in the night sky.",
            "A gentle snowfall begins.",
            "A mist rolls in from the forest."
        };

        // Create a dictionary of dance moves and their effects
        var danceMoves = danceCombinations.Zip(danceEffects, (k, v) => new { k, v })
                                          .ToDictionary(x => x.k, x => x.v);

        // Define the dance sequences for each creature
        var loxMoves = new List<string> { "Twirl", "Leap", "Spin", "Twirl", "Leap" };
        var drakoMoves = new List<string> { "Spin", "Twirl", "Leap", "Leap", "Spin" };

        // Initialize the state of the forest
        var forestState = "Normal";

        // Define the number of sequences
        var numSequences = 5;

        // Perform the dance sequences
        var random = new Random();
        for (int i = 0; i < numSequences; i++)
        {
            // Get the current dance move
            var danceMove = loxMoves[random.Next(loxMoves.Count)] + drakoMoves[random.Next(drakoMoves.Count)];

            // Get the effect of the dance move
            var effect = danceMoves.ContainsKey(danceMove) ? danceMoves[danceMove] : "Nothing happens.";

            // Update the state of the forest based on the effect
            switch (effect)
            {
                case "Fireflies light up the forest.":
                    forestState = "Magical with fireflies";
                    break;
                case "Gentle rain starts falling.":
                    forestState = "Magical with rain";
                    break;
                case "A rainbow appears in the sky.":
                    forestState = "Magical with rainbow";
                    break;
                case "The wind starts to blow.":
                    forestState = "Magical with wind";
                    break;
                case "The sun shines brightly.":
                    forestState = "Magical with sun";
                    break;
                case "The moon appears in the sky.":
                    forestState = "Magical with moon";
                    break;
                case "Stars twinkle in the night sky.":
                    forestState = "Magical with stars";
                    break;
                case "A gentle snowfall begins.":
                    forestState = "Magical with snowfall";
                    break;
                case "A mist rolls in from the forest.":
                    forestState = "Magical with mist";
                    break;
                default:
                    forestState = "Normal";
                    break;
            }

            // Display the state of the forest
            Console.WriteLine($"Sequence {i + 1}: {forestState}");
        }
    }
}