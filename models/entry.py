class Entry():
    def __init__(self, id, concept, entry, date, moodId):
        self.id = id
        self.concept = concept
        self.entry = entry
        self.date = date
        self.mood_id = moodId
        self.mood = None