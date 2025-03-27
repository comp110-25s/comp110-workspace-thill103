"""Exercise 2 on Wordle """

WHITE_BOX: str = "\U00002B1c"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

__author__: str = "730649767"


def contains_char(ST: str, SF: str) -> bool:
    """Checking given character presence at indices"""
    assert len(SF) == 1, f"len('{SF}') is not 1"
    for index in range(len(ST)):
        if ST[index] == SF:
            return True

    return False


def emojified(Guessing: str, Secrets: str) -> str:
    """Color codifying results of a guess"""
    assert len(Guessing) == len(Secrets), "Guess must be same length as secret"

    result_emoji = ""

    for i in range(len(Guessing)):
        if Guessing[i] == Secrets[i]:
            result_emoji += GREEN_BOX
        elif contains_char(Secrets, Guessing[i]):
            result_emoji += YELLOW_BOX
        else:
            result_emoji += WHITE_BOX

    return result_emoji


def input_guess(Expected: int) -> str:
    """Prompting for a word of expected length"""
    Guessing = input(f"Enter a {Expected} character word: ")

    while len(Guessing) != Expected:
        Guessing = input(f"That wasn't {Expected} chars! Try again: ")

    return Guessing


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 0
    max_turns = 6
    won = False

    while turns <= max_turns and not won:
        turns += 1
        print(f"=== Turn {turns}/{max_turns} ===")

        Guessing = input_guess(len(secret))
        feedback = emojified(Guessing, secret)
        print(feedback)

        if Guessing == secret:
            won = True
            print(f"You won in {turns}/{max_turns} turns!")

        else:
            if turns == max_turns:
                print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
