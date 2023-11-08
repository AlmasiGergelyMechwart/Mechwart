//https://bicyclecards.com/how-to-play/blackjack
namespace BlackJack
{
    class Program
    {
        static void Main(string[] args)
        {
            Deck deck = new Deck();
            deck.Shuffle();
            deck.Print();

            Deck.Player player = new Deck.Player(deck);
            Deck.Player dealer = new Deck.Player(deck);

            player.Draw();
            dealer.Draw();
            player.Draw();
            //dealer.Draw();

            player.Print();
            dealer.Print();
        }
    }
}