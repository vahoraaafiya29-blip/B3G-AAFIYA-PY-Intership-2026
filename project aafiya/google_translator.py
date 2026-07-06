from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

root = Tk()
root.title("Google Translator")
root.geometry("700x500")
root.config(bg="white")

title = Label(
    root,
    text="Google Translator",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="blue"
)
title.pack(pady=10)

frame = Frame(root, bg="white")
frame.pack()

language_dict = {
    "English": "en",
    "Hindi": "hi",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Bengali": "bn",
    "Spanish": "es",
    "French": "fr"
}

languages = list(language_dict.keys())

frame.pack()


input_text = Text(
    root,
    height=8,
    width=70,
    font=("Arial", 12)
)
input_text.pack(pady=10)


src_lang = ttk.Combobox(frame, values=languages, width=20)
src_lang.set("English")
src_lang.grid(row=0, column=0, padx=20)

dest_lang = ttk.Combobox(frame, values=languages, width=20)
dest_lang.set("Hindi")
dest_lang.grid(row=0, column=1, padx=20)

output_text = Text(
    root,
    height=8,
    width=70,
    font=("Arial", 12)
)
output_text.pack(pady=10)

def translate_text():
    try:
        text = input_text.get("1.0", END).strip()

        source = language_dict[src_lang.get()]
        target = language_dict[dest_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, "Error: " + str(e))

translate_btn = Button(
    root,
    text="Translate",
    font=("Arial", 14, "bold"),
    bg="black",
    fg="white",
    width=20,
    command=translate_text
)

translate_btn.pack(pady=15)

root.mainloop()
