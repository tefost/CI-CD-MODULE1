import re

def count_sentences(text: str) -> int:
    if not text.strip():
        return 0
    sentences = re.split(r'\.\.\.|[.!?]', text)
    return len([s for s in sentences if s.strip()])

def count_words(text: str) -> int:
    if not text.strip():
        return 0
    text_cleaned = re.sub(r'\.\.\.|[.!?]', ' ', text)
    words = re.split(r'[,\s:;]+', text_cleaned)
    return len([w for w in words if w.strip()])

def analyze_file(filepath: str) -> tuple:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return count_words(content), count_sentences(content)