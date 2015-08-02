"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()
#throw a unicode error as follows:
# UnicodeEncodeError: 'ascii' codec can't encode 
# character u'\xeb' in position 28: ordinal not in range(128)
# Because the table has the word "Citroën"

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded<1950)).all()
#throw the same unicode error as line 32.

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name.isnot('Chevrolet')).all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    """
    Return model info based on given year.

    Takes in a year, and prints out each model's name, brand_name, 
    and brand headquarters for each car model from that year"""

    
    model_info = db.session.query(Model.name, 
                                Model.brand_name, 
                                Model.brand.headquarters).filter(Model.year == year)

    for name, brand_name, headquarters in model_info:
        print name, brand_name, headquarters


def get_brands_summary():
	"""
	Generates each brand's name and a list of the brand's models.

	Take nothing as input and prints each brand name, 
	and all of that brand’s models. Feel free to format with newlines (\n) 
	and/or tabs (\t) to create helpful and readable output."""


    brand_info = db.session.query(Brand.name, Brand.models.name)
    for brand_name, model_names in brand_info:
        print brand_name
        for model_name in model_names:
            print "\t*", model_name 

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
	"""Returns a list of Brand objects with names that contains mystr"""

	return db.session.query(Brand).filter(Brand.name.like(%mystr%)).all()



def get_models_between(start_year, end_year):
	"""Returns a list of Model objects which year is between the given range."""

	return Model.query.filter(Model.year > start_year, Model.year <  end_year).all()


# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# A query object

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#An associatio table enables a many to many relationship by setting itself 
# as a one-many relationshp with other tables
