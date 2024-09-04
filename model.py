import random
from collections import defaultdict

class AIModel:
    def __init__(self):
        self.word_pairs = defaultdict(list)

    def train(self, texts):
        for text in texts:
            words = text.split()
            for i in range(len(words) - 1):
                self.word_pairs[words[i]].append(words[i + 1])

    def generate_response(self, input_text, max_length=20):
        words = input_text.split()
        if not words:
            return "I don't understand. Can you please rephrase?"

        current_word = random.choice(words)
        response = [current_word]

        for _ in range(max_length - 1):
            if current_word in self.word_pairs:
                next_word = random.choice(self.word_pairs[current_word])
                response.append(next_word)
                current_word = next_word
            else:
                break

        return ' '.join(response)
