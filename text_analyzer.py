import re

def count_sentences(text: str) -> int:
    if not text.strip():
        return 0
    sentences = re.split(r'\.\.\.|[.!?]', text)
    return len([s for s in sentences if s.strip()])