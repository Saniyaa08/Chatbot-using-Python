# Chatbot Using Python and Tkinter

## Overview

This is a simple chatbot application built using Python and the Tkinter library. The chatbot is designed to respond to user input based on predefined intents. It uses a neural network model to classify user input into different intents and then selects a response based on the predicted intent.

### Features

- User-friendly graphical interface.
- Responses based on predefined intents.
- Easy customization by editing the intents JSON file.

## Getting Started

To run this chatbot application, follow these steps:

1. Clone or download this repository to your local machine.

2. Install the required dependencies by running the following command:

   ```bash
   pip install tkinter numpy nltk tensorflow
   ```

3. Run the chatbot application:

   ```bash
   python chatbot.py
   ```

4. A graphical user interface (GUI) window will appear with a chat history, an input field, and a "Send" button.

5. Type a message in the input field and press the "Send" button to interact with the chatbot.

## Code Structure

- `chatbot.py`: The main Python script that implements the chatbot logic and GUI using Tkinter.
- `intents.json`: Contains predefined intents and responses for the chatbot.
- `words.pkl` and `classes.pkl`: Pickled files containing preprocessed data for the chatbot.
- `chatbot_saniya.s1`: Pre-trained neural network model for intent classification.

## Customization

You can customize the chatbot's behavior by modifying the `intents.json` file. Define your own intents and responses to make the chatbot more interactive and tailored to your needs.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Commit your changes with descriptive commit messages.
5. Push your branch to your fork.
6. Create a pull request to the main repository's `master` branch.

## Author

This chatbot was created by Saniya for educational purposes.

## Acknowledgments

- Special thanks to the creators of the Keras library for providing a framework for building and training neural networks.
- Thanks to the nltk library for natural language processing capabilities.

If you have any questions or feedback, please feel free to reach out to the author.

Happy Chatting!
```
