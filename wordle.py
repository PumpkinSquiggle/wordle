import random, logging

MAX_GUESSES = 6


def pretty_print(hint: list) -> None:
    for letter_obj in hint:
        if letter_obj.get("correct_placement"):
            suffix = "Placement is correct"
        else:
            suffix = "Is in word: " + str(letter_obj.get("in_word"))
        print("Letter: " + letter_obj.get("letter") + " - " + suffix)
    print("")


def word_to_list(word: str) -> list:
    return list(word)


def guess(player_guess: str, answer_word: str) -> list:
    guess_list = word_to_list(player_guess)
    answer_list = word_to_list(answer_word)
    guess_letters = []

    for index, letter in enumerate(guess_list):
        result = {
            'letter': letter,
            'in_word': letter in answer_list,
            'correct_placement': guess_list[index] == answer_list[index]
        }
        guess_letters.append(result)
    return guess_letters


def get_all_words(filename: str) -> list:
    with open(filename) as f:
        lines = f.read().splitlines()
        return lines


def random_answer(all_words: list) -> str:
    x = random.choice(all_words)
    logging.debug(x)
    return x


def main():
    all_words = get_all_words("list-of-five-letter-words.txt")
    answer = random_answer(all_words).strip()
    number_of_guesses = 1

    while number_of_guesses <= MAX_GUESSES:
        player_guess = input("Enter your guess:").strip()

        if player_guess in all_words:
            if player_guess == answer:
                print("Nailed It!!")
                break
            pretty_print(guess(player_guess, answer))
            number_of_guesses += 1

        else:
            print("Not a word! (nice try)")


if __name__ == '__main__':
    main()
