# import csv
import datetime

import models
from database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

test = models.Record(id=2, title='Test title2', intro='This is a very interesting intro2. Second sentence.',
       text='This is main text. 12345 is a number2.', date=datetime.datetime.utcnow())

db.add(test)
db.commit()
db.close()
