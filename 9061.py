import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                # Удаляем пунктуацию из строки
                translator = str.maketrans('', '', string.punctuation.replace('-', '') + ' -')
                content = content.translate(translator)
                words = content.split()
                all_words[file_name] = words
        return all_words
    
    def find(self, word):
        positions = {}
        all_words = self.get_all_words()
        target_word = word.lower()
        for name, words in all_words.items():
            if target_word in words:
                positions[name] = words.index(target_word) + 1  # Индексация с 1
        return positions
    
    def count(self, word):
        counts = {}
        all_words = self.get_all_words()
        target_word = word.lower()
        for name, words in all_words.items():
            counts[name] = words.count(target_word)
        return counts
