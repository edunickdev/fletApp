class Task:
    
    def __init__(self, title: str, start: str, end: str, description: str, category: str, suggestGPT: str ):
        self.title = title
        self.start = start
        self.end = end
        self.description = description
        self.category = category
        self.suggestGPT = suggestGPT
    
    def to_dict(self):
        return {
            'title': self.title,
            'start_date': self.start,
            'end_date': self.end,
            'description': self.description,
            'category': self.category,
            'suggestGPT': self.suggestGPT
        }
