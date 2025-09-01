#Title: Interactive Probability Calculator
# Description: This script allows a user to choose an experiment (die roll or card draw)
# and define an event to calculate its probability.

import re # Using regex for cleaner input parsing

def calculate_probability(event_outcomes, sample_space):
    """Calculates and returns the probability of an event."""
    event_count = len(event_outcomes)
    total_count = len(sample_space)
    
    if total_count == 0:
        return 0.0, 0, 0
        
    probability = event_count / total_count
    return probability, event_count, total_count

def handle_dice_experiment():
    """Handles the logic for the die-rolling experiment."""
    print("\n--- Rolling a Single Six-Sided Die ---")
    sample_space_dice = {1, 2, 3, 4, 5, 6}
    print(f"The sample space (all possible outcomes) is: {sorted(list(sample_space_dice))}")
    
    while True:
        try:
            # Get user input for the event outcomes
            user_input_str = input("\nEnter the outcomes for your event, separated by commas (e.g., 2, 4, 6): ")
            
            # Use regex to find all numbers in the string
            outcomes_str = re.findall(r'\d+', user_input_str)
            
            # Convert string numbers to integers
            user_event_outcomes = {int(num) for num in outcomes_str}
            
            # Validate that the user's outcomes are actually in the sample space
            if not user_event_outcomes.issubset(sample_space_dice):
                print("Error: One or more of your chosen outcomes are not valid for a six-sided die (1-6). Please try again.")
                continue
            
            # Calculate probability
            prob, event_n, total_n = calculate_probability(user_event_outcomes, sample_space_dice)
            
            # Display results
            print("\n--- Result ---")
            print(f"Your defined event is: {sorted(list(user_event_outcomes))}")
            print(f"Number of outcomes in your event: {event_n}")
            print(f"Total outcomes in sample space: {total_n}")
            print(f"The probability of your event is: {event_n}/{total_n} = {prob:.2%}") # Display as percentage
            break # Exit the loop after successful calculation
            
        except (ValueError, TypeError):
            print("Invalid input. Please enter numbers separated by commas.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def handle_cards_experiment():
    """Handles the logic for the card-drawing experiment."""
    print("\n--- Drawing a Single Card from a Standard 52-Card Deck ---")
    
    # Create the sample space for a deck of cards
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    sample_space_cards = {f"{rank} of {suit}" for rank in ranks for suit in suits}
    
    # Present user with choices
    print("Choose the type of event you want to calculate the probability for:")
    print("  1. Drawing a specific suit (e.g., all Hearts)")
    print("  2. Drawing a specific rank (e.g., all Kings)")
    print("  3. Drawing any face card (Jack, Queen, or King)")
    
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        user_event_outcomes = set()
        event_description = ""

        if choice == '1':
            suit_choice = input("Enter the suit (Hearts, Diamonds, Clubs, or Spades): ").strip().title()
            if suit_choice in suits:
                user_event_outcomes = {card for card in sample_space_cards if suit_choice in card}
                event_description = f"drawing any card of the suit '{suit_choice}'"
                break
            else:
                print("Invalid suit. Please enter one of the four suits.")
        
        elif choice == '2':
            rank_choice = input("Enter the rank (e.g., 7, King, Ace): ").strip().title()
            if rank_choice in ranks:
                user_event_outcomes = {card for card in sample_space_cards if card.startswith(rank_choice)}
                event_description = f"drawing a card with the rank '{rank_choice}'"
                break
            else:
                print("Invalid rank. Please check your spelling and try again.")

        elif choice == '3':
            face_cards = {'Jack', 'Queen', 'King'}
            user_event_outcomes = {card for card in sample_space_cards if card.split()[0] in face_cards}
            event_description = "drawing any face card (Jack, Queen, or King)"
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Calculate and display results for the card experiment
    prob, event_n, total_n = calculate_probability(user_event_outcomes, sample_space_cards)
    print("\n--- Result ---")
    print(f"The event is: {event_description}.")
    # print(f"Outcomes in this event: {sorted(list(user_event_outcomes))}") # Optional: uncomment to see all cards
    print(f"Number of outcomes in this event: {event_n}")
    print(f"Total outcomes in sample space (a full deck): {total_n}")
    print(f"The probability of this event is: {event_n}/{total_n} = {prob:.2%}")


def main():
    """Main function to run the interactive program."""
    print("Welcome to the Interactive Probability Calculator!")
    while True:
        print("\nWhich experiment would you like to run?")
        print("  1. Roll a Die")
        print("  2. Draw a Card")
        print("  3. Quit")
        
        user_choice = input("Please enter your choice (1, 2, or 3): ")
        
        if user_choice == '1':
            handle_dice_experiment()
        elif user_choice == '2':
            handle_cards_experiment()
        elif user_choice == '3':
            print("Thank you for using the probability calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main program
if __name__ == "__main__":
    main()
