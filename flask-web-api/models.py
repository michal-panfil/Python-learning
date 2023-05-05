class Book:
    def __init__(self, id, avaliable, title, timestamp):
        self.id = id
        self.avaliable = avaliable
        self.title = title
        self.timestamp = timestamp

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'avaliable': self.avaliable,
            'title': self.title,
            'timestamp': self.timestamp
        }