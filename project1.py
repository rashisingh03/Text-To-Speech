import tkinter as tk
from tkinter.ttk import Combobox
import pyttsx3
from gtts import gTTS
from playsound import playsound
from deep_translator import GoogleTranslator
import os

# Initialize window
root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("1000x580+200+80")
root.configure(bg="#F7AC40")

# Initialize engine
tts = pyttsx3.init()


def speaknow():

    text = text_box.get("1.0", tk.END).strip()
    gender = gender_box.get().lower()
    speed = speed_box.get().lower()
    language = language_box.get().lower()

    if text == "":
        return

    lang_dict = {
        "english": "en",
        "hindi": "hi",
        "french": "fr",
        "spanish": "es",
        "german": "de",
        "tamil": "ta",
        "bengali": "bn",
        "telugu": "te",
        "marathi": "mr",
        "gujarati": "gu",
        "punjabi": "pa"
    }

    lang_code = lang_dict.get(language, "en")

    try:

        # English speech
        if language == "english":

            voices = tts.getProperty("voices")

            if gender == "male":
                tts.setProperty("voice", voices[0].id)
            else:
                tts.setProperty("voice", voices[1].id)

            if speed == "fast":
                tts.setProperty("rate", 200)
            elif speed == "slow":
                tts.setProperty("rate", 100)
            else:
                tts.setProperty("rate", 150)

            tts.say(text)
            tts.runAndWait()

            translated_label.config(text="")

        else:

            translated_text = GoogleTranslator(source="auto", target=lang_code).translate(text)

            tts_g = gTTS(text=translated_text, lang=lang_code)

            filename = "voice.mp3"
            tts_g.save(filename)

            playsound(filename)
            os.remove(filename)

            translated_label.config(text="Translated: " + translated_text)

    except Exception as e:
        print("Error:", e)


# Upper frame
upper_frame = tk.Frame(root, bg="#14A7DD", width=1200, height=130)
upper_frame.place(x=0, y=0)

# Title
title = tk.Label(
    upper_frame,
    text="Text to Speech Converter",
    font=("Times New Roman", 40, "bold"),
    bg="#14A7DD"
)
title.place(x=300, y=10)

# Text box
text_box = tk.Text(
    root,
    font=("Calibri", 20),
    bg="white",
    wrap=tk.WORD
)
text_box.place(x=50, y=180, width=800, height=100)

# Gender
gender_box = Combobox(
    root,
    values=["Male", "Female"],
    state="readonly"
)
gender_box.place(x=250, y=400)
gender_box.set("Male")

# Speed
speed_box = Combobox(
    root,
    values=["Fast", "Medium", "Slow"],
    state="readonly"
)
speed_box.place(x=420, y=400)
speed_box.set("Medium")

# Language
language_box = Combobox(
    root,
    values=[
        "English",
        "Hindi",
        "French",
        "Spanish",
        "German",
        "Tamil",
        "Bengali",
        "Telugu",
        "Marathi",
        "Gujarati",
        "Punjabi"
    ],
    state="readonly"
)
language_box.place(x=590, y=400)
language_box.set("English")

# Labels
tk.Label(root, text="Select Voice", font=("Times New Roman", 15, "bold"),
         bg="#F7AC40", fg="white").place(x=250, y=370)

tk.Label(root, text="Select Speed", font=("Times New Roman", 15, "bold"),
         bg="#F7AC40", fg="white").place(x=420, y=370)

tk.Label(root, text="Select Language", font=("Times New Roman", 15, "bold"),
         bg="#F7AC40", fg="white").place(x=590, y=370)

# Play button
play_btn = tk.Button(
    root,
    text="Play",
    bg="white",
    font=("Arial", 14, "bold"),
    command=speaknow
)
play_btn.place(x=435, y=450)

# Translation label
translated_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#F7AC40"
)
translated_label.place(x=50, y=300)

root.mainloop()