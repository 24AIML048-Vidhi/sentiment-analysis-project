import re

def clean_text(text):
    
    # remove numbers and symbols
    text = re.sub(r"[^a-zA-Z]", " ", str(text))
    
    # convert to lowercase
    text = text.lower()
    
    # remove extra spaces
    text = text.strip()
    
    return text