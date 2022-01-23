from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine('mysql+pymysql://root:#Flyingraijin123@localhost/movie_ratings')
print(engine)
conn = engine.connect()
result = conn.execute(text("SELECT * FROM Movies"))
print(result)
