import pytest
from text_analyzer import count_sentences, count_words, analyze_file

@pytest.fixture
def temp_text_file(tmp_path):
    file_path = tmp_path / "test_data.txt"
    content = "Привіт! Це тест: один, два, три. Ось ще слова; і кінець..."
    file_path.write_text(content, encoding='utf-8')
    return file_path

@pytest.mark.parametrize("text, expected_words", [
    ("Одне слово", 2),
    ("Слова, розділені: комою; та пробілом", 6),
    ("Текст... з різними! знаками?", 4),
    ("", 0)
])
def test_count_words(text, expected_words):
    assert count_words(text) == expected_words

@pytest.mark.parametrize("text, expected_sentences", [
    ("Перше. Друге! Третє?", 3),
    ("Текст із трикрапкою... І ще одне речення.", 2),
    ("Без кінцевих знаків", 1),
    ("", 0)
])
def test_count_sentences(text, expected_sentences):
    assert count_sentences(text) == expected_sentences

def test_analyze_file(temp_text_file):
    words, sentences = analyze_file(temp_text_file)
    assert words == 11
    assert sentences == 3