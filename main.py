from nlp_processor import NLPProcessor
from model import AIModel
from knowledge_base import KnowledgeBase
from user_interface import UserInterface

class PersonalAI:
    def __init__(self):
        self.nlp = NLPProcessor()
        self.model = AIModel()
        self.kb = KnowledgeBase()
        self.ui = UserInterface()

    def train(self, filename):
        with open(filename, 'r') as f:
            texts = f.readlines()
        processed_texts = [self.nlp.process(text) for text in texts]
        self.model.train(processed_texts)

    def process_input(self, user_input):
        processed_input = self.nlp.process(user_input)
        context = self.kb.get_relevant_info(processed_input)
        response = self.model.generate_response(processed_input)
        return response

    def run(self):
        self.train('training_data.txt')  # You'll need to create this file with training data
        while True:
            user_input = self.ui.get_input()
            if user_input.lower() == 'exit':
                break
            response = self.process_input(user_input)
            self.ui.display_output(response)

if __name__ == "__main__":
    ai = PersonalAI()
    ai.run()
