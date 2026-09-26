# Mythology Hangman 🕉️

A console-based Hangman game in Python featuring mythology-inspired words. Guess the letters before you run out of attempts!

## Features

- Random word selection from a mythology-themed word list
- Visual letter-by-letter progress display
- Tracks wrong guesses out of a maximum of 6
- Input validation (single alphabet letters only, no repeated guesses)
- Play multiple rounds without restarting the program
- Clean win/loss messages

## Requirements

- Python 3.x (no external libraries needed — uses only the built-in `random` module)

## How to Run

1. Save the script as `hangman.py`.
2. Open a terminal in the same folder.
3. Run:

   ```bash
   python hangman.py
   ```

4. Guess one letter at a time until you reveal the word or run out of guesses.

## Word List

The current word list includes:

- krishna
- garuda
- hanuman
- indra
- trishula

You can add more words by editing the `words` list at the top of the script.

## Example Session

```
===================================
       WELCOME TO HANGMAN GAME
===================================
Guess the mythology-inspired word!
You can make up to 6 incorrect guesses.

A new word has been selected!
The word has 6 letters.

Word: _ _ _ _ _ _
Wrong guesses: 0 / 6
Enter a letter: i
✅ Correct guess!

Word: i _ _ _ _ _
Wrong guesses: 0 / 6
Enter a letter: n
✅ Correct guess!
...
🎉 Congratulations!
You guessed the word: indra

Do you want to play again? (yes/no): no

Thank you for playing Hangman!
Goodbye!
```

## Possible Improvements

- Add ASCII-art hangman drawings for each wrong guess
- Add difficulty levels with longer/shorter words
- Add word categories (gods, weapons, animals, etc.)
- Track and display win/loss statistics across rounds
- Add hints for each word

## License

Free to use and modify for personal or educational purposes.
