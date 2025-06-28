using System;
using System.Security.Cryptography;
using System.Text;

class Solver
{
    static void Main()
    {
        for (int i = 0; i < 30000000; i++)
        {
            string seedInput = i.ToString();
            int seed = GetSeed(seedInput);
            Random rng = new Random(seed);

            int playerScore = 0, jokerScore = 0;

            while (playerScore < 100 && jokerScore < 100)
            {
                int playerRoll = rng.Next(1, 7);
                int jokerRoll = rng.Next(5, 7);

                playerScore += playerRoll;
                jokerScore += jokerRoll;
            }

            if (playerScore > jokerScore)
            {
                Console.WriteLine($"✅ Win found with seed: {seedInput}");
                Console.WriteLine($"Final Scores -> Player: {playerScore}, Joker: {jokerScore}");
                break;
            }
        }
    }

    static int GetSeed(string input)
    {
        var hash = SHA256.HashData(Encoding.UTF8.GetBytes(input));
        return BitConverter.ToInt32(hash, 0);
    }
}

// → 21733947