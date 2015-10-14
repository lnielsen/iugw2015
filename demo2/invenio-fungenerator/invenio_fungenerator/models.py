from invenio_db import db


class MyTable(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255))
