# Title: Basic Probability Notation Demonstration
# Description: This script explains and shows basic probability concepts
# using a simple die-rolling experiment.

# --- 1. Define the Experiment and Sample Space ---

# An "outcome" is a single possible result of an experiment.
# The "sample space" (often denoted as S) is the set of all possible outcomes.

# Our experiment is rolling a single, fair six-sided die.
# The set of all possible outcomes (the sample space) is {1, 2, 3, 4, 5, 6}.
sample_space = {1, 2, 3, 4, 5, 6}
total_outcomes_count = len(sample_space)


# --- 2. Define Events ---

# An "event" is a specific set of one or more outcomes from the sample space that we are interested in.
# It is a subset of the sample space.

# Event A: The outcome is an even number.
event_a_outcomes = {2, 4, 6}
event_a_count = len(event_a_outcomes)

# Event B: The outcome is a number greater than 4.
event_b_outcomes = {5, 6}
event_b_count = len(event_b_outcomes)

# Event C: The outcome is exactly 3.
# This is an example of an event with a single outcome.
event_c_outcomes = {3}
event_c_count = len(event_c_outcomes)


# --- 3. Calculate Probability Value ---

# The "probability value" of an event is a number between 0 and 1 (inclusive)
# that represents the likelihood of that event occurring.
#
# The formula for the probability of an event (E) is:
# P(E) = (Number of outcomes in the event) / (Total number of outcomes in the sample space)

def calculate_probability(event_outcome_count, total_sample_count):
    """
    Calculates the probability of an event.
    Args:
        event_outcome_count (int): The number of favorable outcomes for the event.
        total_sample_count (int): The total number of outcomes in the sample space.
    Returns:
        float: The probability value, or 0 if the sample space is empty.
    """
    if total_sample_count == 0:
        return 0
    return event_outcome_count / total_sample_count

# Calculate the probability for each of our defined events.
probability_a = calculate_probability(event_a_count, total_outcomes_count)
probability_b = calculate_probability(event_b_count, total_outcomes_count)
probability_c = calculate_probability(event_c_count, total_outcomes_count)


# --- 4. Display the Results ---

print("--- Basic Probability Demonstration ---")
print(f"Experiment: Rolling a single six-sided die.")
print(f"Sample Space (all possible outcomes): {sorted(list(sample_space))}")
print(f"Total number of outcomes: {total_outcomes_count}\n")

print("--- Events and Their Probabilities ---\n")

# Display Event A
print(f"Event A: Rolling an even number.")
print(f"Outcomes for Event A: {sorted(list(event_a_outcomes))}")
# The notation P(A) means "the probability of event A".
print(f"The probability value, P(A), is: {event_a_count}/{total_outcomes_count} = {probability_a:.2f}\n")

# Display Event B
print(f"Event B: Rolling a number greater than 4.")
print(f"Outcomes for Event B: {sorted(list(event_b_outcomes))}")
print(f"The probability value, P(B), is: {event_b_count}/{total_outcomes_count} = {probability_b:.2f}\n")

# Display Event C
print(f"Event C: Rolling a 3.")
print(f"Outcomes for Event C: {sorted(list(event_c_outcomes))}")
print(f"The probability value, P(C), is: {event_c_count}/{total_outcomes_count} = {probability_c:.2f}\n")


