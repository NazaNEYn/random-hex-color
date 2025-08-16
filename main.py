import random


def generate_random_hex_code():
    """Generates a random 6-digit hexadecimal color code."""

    # List of all possible hexadecimal characters (0-9 and a-f).
    # We use strings for all characters to make joining them easier later.
    hex_characters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    # This list will store the 6 random characters we pick.
    random_hex_list = []

    # Loop 6 times to get 6 random characters for the hex code.
    for _ in range(6):
        # Pick a single random character from our list of possibilities.
        random_char = random.choice(hex_characters)
        # Add the chosen character to our list.
        random_hex_list.append(random_char)

    # Join the characters in the list into a single string.
    # The "" tells Python to put nothing between the characters.
    hex_code = "".join(random_hex_list)

    # Return the full hex code, including the leading "#"
    return f"#{hex_code}"


# To run the code and see the result:
print(generate_random_hex_code())
