import random
import time

def spin_reels():
    symbols = ['🍒', '🍋', '🔔', '💎', '7️⃣']
    # random.choices allows us to set weights (7s and Diamonds are rarer)
    return random.choices(symbols, weights=[10, 8, 5, 2, 1], k=3)

def play_slot_machine():
    balance = 100
    print("--- Welcome to the Python Slots! ---")
    print(f"Starting Balance: ${balance}")

    while balance > 0:
        bet = input(f"\nCurrent Balance: ${balance} | Enter bet amount (or 'q' to quit): ")

        if bet.lower() == 'q':
            break
        
        if not bet.isdigit() or int(bet) > balance or int(bet) <= 0:
            print("Invalid bet. Please enter a valid amount.")
            continue

        bet = int(bet)
        balance -= bet
        
        print("\nSpinning...")
        time.sleep(1) # Adds a bit of suspense
        
        reels = spin_reels()
        print(f" | {' | '.join(reels)} | ")
        
        # Win Logic
        if reels[0] == reels[1] == reels[2]:
            multipliers = {'🍒': 5, '🍋': 10, '🔔': 20, '💎': 50, '7️⃣': 100}
            winnings = bet * multipliers[reels[0]]
            balance += winnings
            print(f"🎉 JACKPOT! You won ${winnings}!")

        elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
            winnings = bet * 2
            balance += winnings
            print(f"✨ Small Win! Two matched. You won ${winnings}.")
        else:
            print("❌ No match this time.")

    print(f"\nGame Over. You're leaving with ${balance}. Thanks for playing!")

if __name__ == "__main__":
    play_slot_machine()