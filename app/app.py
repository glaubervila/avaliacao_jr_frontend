from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_restless
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db/avaliacao.db'
db = SQLAlchemy(app)


class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    owner = db.Column(db.String(80), nullable=True)
    date = db.Column(db.DateTime(), nullable=True)

    def __repr__(self):
        return '<Catalog %r>' % self.name


class CatalogObjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    ra = db.Column(db.Float, nullable=False)
    dec = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    wikipedia = db.Column(db.Text, nullable=True)

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

    cat1 = Catalog(name='Galaxies', owner='Glauber Costa', date=datetime.now())
    cat2 = Catalog(name='List of nebulae', owner='Cristiano Singulani', date=datetime.strptime('2019-05-04 20:45:23', '%Y-%m-%d %H:%M:%S'))

    db.session.add(cat1)
    db.session.add(cat2)

    obj1 = CatalogObjects(name='Andromeda Galaxy', ra=10.6706957, dec=41.2454558, catalog=cat1, description='The Andromeda Galaxy (/ænˈdrɒmɪdə/), also known as Messier 31, M31, or NGC 224, is a spiral galaxy approximately 780 kiloparsecs (2.5 million light-years) from Earth, and the nearest major galaxy to the Milky Way', wikipedia='https://en.wikipedia.org/wiki/Andromeda_Galaxy')
    obj2 = CatalogObjects(name='M 87', ra=187.7042000, dec=12.3909806, catalog=cat1, description='Messier 87 (also known as Virgo A or NGC 4486, generally abbreviated to M87) is a supergiant elliptical galaxy in the constellation Virgo.', wikipedia='https://en.wikipedia.org/wiki/Messier_87')
    obj3 = CatalogObjects(name='M 101', ra=210.8024292, dec=54.3487500, catalog=cat1, description='The Pinwheel Galaxy (also known as Messier 101, M101 or NGC 5457) is a face-on spiral galaxy distanced 21 million light-years (six megaparsecs)[3] away from Earth in the constellation Ursa Major.', wikipedia='https://en.wikipedia.org/wiki/Pinwheel_Galaxy')
    obj4 = CatalogObjects(name='NGC 1300', ra=49.9210222, dec=-19.4111504, catalog=cat1, description='NGC 1300 is a barred spiral galaxy located about 61 million light-years away in the constellation Eridanus.', wikipedia='https://en.wikipedia.org/wiki/NGC_1300')
    obj5 = CatalogObjects(name='NGC 891', ra=35.6371125, dec=-42.3483194, catalog=cat1, description='NGC 891 (also known as Caldwell 23 or Silver Sliver Galaxy) is an edge-on unbarred spiral galaxy about 30 million light-years away in the constellation Andromeda.', wikipedia='https://en.wikipedia.org/wiki/NGC_891')
    obj6 = CatalogObjects(name='M 104', ra=189.9976327, dec=-11.6230542, catalog=cat1, description='The Sombrero Galaxy (also known as Messier Object 104, M104 or NGC 4594) is a lenticular galaxy[4] in the constellation Virgo', wikipedia='https://en.wikipedia.org/wiki/Sombrero_Galaxy')
    
    db.session.add(obj1)
    db.session.add(obj2)
    db.session.add(obj3)
    db.session.add(obj4)
    db.session.add(obj5)
    db.session.add(obj6)
 
    obj7 = CatalogObjects(name='Tarantula Nebula', ra=84.6500000, dec=-69.0863888, catalog=cat2, description='The Tarantula Nebula (also known as 30 Doradus) is an H II region in the Large Magellanic Cloud (LMC).', wikipedia='https://en.wikipedia.org/wiki/Tarantula_Nebula')
    obj8 = CatalogObjects(name='Eagle Nebula', ra=274.7000000, dec= -13.8066666, catalog=cat2, description='The Eagle Nebula is a young open cluster of stars in the constellation Serpens', wikipedia='https://en.wikipedia.org/wiki/Eagle_Nebula')
    obj9 = CatalogObjects(name='Veil Nebula', ra=73.3198569, dec=-7.6627167, catalog=cat2, description='The Veil Nebula is a cloud of heated and ionized gas and dust in the constellation Cygnus.', wikipedia='https://en.wikipedia.org/wiki/Veil_Nebula')

    db.session.add(obj7)
    db.session.add(obj8)
    db.session.add(obj9)


    db.session.commit()

except Exception as e:
    print(e)
    pass


# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
catalog_api = manager.create_api(
    Catalog, 
    collection_name='catalog',
    methods=['GET', 'POST', 'DELETE', 'PUT', 'PATCH'],
    exclude_columns=['catalog_objects'],
    allow_patch_many=False,
    )

catalog_objects_api = manager.create_api(
    CatalogObjects, 
    methods=['GET'],
    exclude_columns=['catalog'])


@app.route('/')
def hello_world():
    return 'Bem vindo ao teste para Dev jr e Boa Sorte!'