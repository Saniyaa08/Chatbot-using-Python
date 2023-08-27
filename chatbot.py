import tkinter as tk
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("C:/Users/DELL/OneDrive/Desktop/chatbot using python/chatbot/Include/intents.json").read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

model = load_model("chatbot_saniya.s1")

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []

    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})

    return return_list

def get_response(intents_list, intents_json):
    list_of_intents = intents_json['intents']
    tag = intents_list[0]['intent']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def send_message():
    message = entry.get()
    entry.delete(0, tk.END)
    if message.strip() != "":
        ints = predict_class(message)
        res = get_response(ints, intents)
        text.configure(state=tk.NORMAL)
        text.insert(tk.END, "You: " + message + "\n", "user")
        text.insert(tk.END, "Bot: " + res + "\n", "bot")
        text.insert(tk.END, "\n")
        text.configure(state=tk.DISABLED)

        # Apply different styles to user and bot messages
        text.tag_add("user", "1.0", "1.end")
        text.tag_add("bot", "2.0", "2.end")
        text.tag_config("user", foreground="blue", font=("Arial", 12, "bold"))
        text.tag_config("bot", foreground="red", font=("Arial", 12))

        # Optional: Print the bot's response to the console
        print("Bot: " + res)

# Create the GUI window
window = tk.Tk()
window.title("Chatbot")

# Set the window background color
window.configure(bg="lightgray")

# Create a label for the chat history
label = tk.Label(window, text="Saniya's Chatbot", font=("Arial", 14, "bold"), bg="lightgray", fg="darkblue")
label.grid(row=0, column=0, padx=10, pady=10)

# Configure the chat history text widget
text = tk.Text(window, height=10, width=50, state=tk.DISABLED)
text.tag_configure("user", foreground="blue", font=("Arial", 12, "bold"))
text.tag_configure("bot", foreground="red", font=("Arial", 12))
text.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

# Create a frame for user input
input_frame = tk.Frame(window, bg="lightgray")
input_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Create an entry widget for user input
entry = tk.Entry(input_frame, width=40, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)

# Create a button to send the message
button = tk.Button(input_frame, text="Send", font=("Arial", 12), bg="gray", fg="white", command=send_message)
button.pack(side=tk.LEFT, padx=5)

# Add padding to the window and input frame
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(0, weight=1)

# Start the main GUI loop
window.mainloop()
