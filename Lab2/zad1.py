
STOP_WORDS = {"i", "a", "the", "of", "in", "on", "and", "to", "is", "it", "for", "with", "as", "by", "that", "at"}


def analyze_tekstu(text):
    paragraphs = text.strip().split("\n")
    sentences = re.split(r'[.!?]', text)
    words = re.findall(r'\b\w+\b', text.lower())
    
    num_paragraphs = len(paragraphs)
    num_sentences = len(sentences) - sentences.count('')
    num_words = len(words)
    
    filtered_words = [word for word in words if word not in STOP_WORDS]
    most_common_words = Counter(filtered_words).most_common(5)
    
    transformed_words = []
    for word in re.findall(r'\b\w+\b', text):
        if word.lower().startswith('a'):
            transformed_words.append(word[::-1])
        else:
            transformed_words.append(word)
    transformed_text = ' '.join(transformed_words)
    
    print("Liczba akapitów:", num_paragraphs)
    print("Liczba zdań:", num_sentences)
    print("Liczba słów:", num_words)
    print("Najczęstsze słowa:", most_common_words)
    print("Tekst po transformacji:", transformed_text)

text = """
This is an example text. An apple a day keeps the doctor away.
A paragraph about apples and their advantages. Amazing apples are abundant and healthy.
"""

analyze_text(text)
