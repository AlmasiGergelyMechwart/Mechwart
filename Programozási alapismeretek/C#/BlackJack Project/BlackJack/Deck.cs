namespace BlackJack
{
    public class Deck
    {
        //string[] deck = new string[52];
        List<string> deck = new ();
        string faceCards = "JQKA";
        string suits = "HDCS";

        Random rnd = new Random();

        public Deck()
        {
            for (int i = 0; i < 52; i++)
            {
                if (i % 13 <= 8)
                {
                    deck.Add(((i % 13) + 2).ToString() + suits[(int)(4 / (52 / (float)i))]);
                }
                else
                {
                    deck.Add(faceCards[(i % 13) - 9].ToString() + suits[(int)(4 / (52 / (float)i))].ToString());
                }
            }
        }

        public void Print()
        {
            for (int i = 0; i < deck.Count; i++)
            {
                if (deck[i].Length < 3)
                {
                    Console.Write(" ");
                }

                Console.Write(deck[i] + " ");

                if (i % 13 == 12)
                {
                    Console.WriteLine();
                }
            }
        }

        public void Shuffle()
        {
            for (int i = 0; i < deck.Count; i++)
            {
                int rand = rnd.Next(i, deck.Count);
                string temp = deck[i];
                deck[i] = deck[rand];
                deck[rand] = temp;
            }
        }

        public class Player
        {
            Deck deck;
            public Player(Deck d) { deck = d; }

            List<string> hand = new ();

            public void Draw()
            {
                hand.Add(deck.deck[0]);
                deck.deck.RemoveAt(0);
            }

            public void Print()
            {
                for (int i = 0; i < hand.Count; i++)
                {
                    Console.Write(hand[i] + " ");
                }
                Console.WriteLine();
            }
        }
    }

}