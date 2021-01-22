class Entry():
    def __init__(self, id, concept, entry, date, mood_id):
        self.id = id
        self.concpet = concept
        self.entry = entry
        self.date = date
        self.mood_id = mood_id
        self.mood = None