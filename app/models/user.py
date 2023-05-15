from app.extensions import db

class User(db.Model):
    id = db.Column(db.String(150), primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.Text)

    def __repr__(self):
        return f'<User "{self.name}">'