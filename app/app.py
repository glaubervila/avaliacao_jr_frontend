from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db/avaliacao.db'
db = SQLAlchemy(app)

# db.create_all()


class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Catalog %r>' % self.name


class CatalogObjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    ra = db.Column(db.Integer, nullable=False)
    dec = db.Column(db.Integer, nullable=False)

    catalog_id = db.Column(db.Integer, db.ForeignKey(
        'catalog.id'))
    catalog = db.relationship(
        'Catalog', backref=db.backref('catalog_objects', lazy=True))

    def __repr__(self):
        return '<CatalogObjects %r>' % self.name


db.create_all()


# Adding some Rows
try:
    db.session.query(CatalogObjects).delete()
    db.session.query(Catalog).delete()

    cat1 = Catalog(name='Teste 1')
    cat2 = Catalog(name='Teste 2')

    db.session.add(cat1)
    db.session.add(cat2)

    obj1 = CatalogObjects(name='Object 1', ra=10, dec=20, catalog=cat1)
    obj2 = CatalogObjects(name='Object 2', ra=10, dec=20, catalog=cat1)
    obj3 = CatalogObjects(name='Object 3', ra=10, dec=20, catalog=cat1)

    db.session.add(obj1)
    db.session.add(obj2)
    db.session.add(obj3)

    obj4 = CatalogObjects(name='Object 4', ra=10, dec=20, catalog=cat2)
    obj5 = CatalogObjects(name='Object 5', ra=10, dec=20, catalog=cat2)
    obj6 = CatalogObjects(name='Object 6', ra=10, dec=20, catalog=cat2)

    db.session.add(obj4)
    db.session.add(obj5)
    db.session.add(obj6)

    db.session.commit()

except Exception as e:
    print(e)
    pass


@app.route('/')
def hello_world():
    return 'Hello, World!'
