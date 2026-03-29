import requests
import re
from collections import Counter

def get_text(url):
    response = requests.get(url.strip(), timeout=10)
    response.raise_for_status()
    return response.text

def count_word_frequencies_optimized(url, words_to_count):
    text = get_text(url)  # загружает текст единожды
    
    words = re.findall(r'[a-zA-Z]+', text.lower())  # regex для извлечения слов
    
    counter = Counter(words)
    
    frequencies = {
        word: counter.get(word.lower(), 0)
        for word in words_to_count
    }
    return frequencies

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    with open(words_file, 'r', encoding='utf-8') as file:
        words_to_count = [line.strip() for line in file if line.strip()]

    frequencies = count_word_frequencies_optimized(url, words_to_count)  # Единственный запрос
    

    print(frequencies)

if __name__ == "__main__":
    main()