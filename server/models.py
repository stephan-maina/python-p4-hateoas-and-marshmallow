from app import db

class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=True)

    def __init__(self, title, body):
        self.title = title
        self.body = body
