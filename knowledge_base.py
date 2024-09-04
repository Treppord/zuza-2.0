import sqlite3

class KnowledgeBase:
    def __init__(self):
        self.conn = sqlite3.connect('knowledge_base.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS knowledge
            (id INTEGER PRIMARY KEY, topic TEXT, information TEXT)
        ''')

    def add_information(self, topic, information):
        self.cursor.execute("INSERT INTO knowledge (topic, information) VALUES (?, ?)", (topic, information))
        self.conn.commit()
    def get_relevant_info(self, processed_input):
        # Use the processed_input directly as search terms
        search_terms = processed_input
        
        self.cursor.execute("SELECT information FROM knowledge WHERE topic LIKE ?", ('%' + search_terms + '%',))
        return self.cursor.fetchall()
    def populate_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                topic, information = line.strip().split(':', 1)
                self.add_information(topic.strip(), information.strip())
