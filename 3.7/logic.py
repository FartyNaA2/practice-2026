def process_text(text):
    if not text:
        return "Текст не введено", 0
    
    upper_text = text.upper()
    length = len(text)
    
    return upper_text, length
