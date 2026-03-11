
    text = text_box.get("1.0", tk.END).strip()
    gender = gender_box.get().lower()
    speed = speed_box.get().lower()
    language = language_box.get().lower()

    if text == "":
        return

    lang_dict = {
        'english': 'en',
        'hindi': 'hi',
        'french': 'fr',
        'spanish': 'es',
        'german': 'de',