import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONN_STR']
print("db_connection_string", db_connection_string)
engine = create_engine(db_connection_string,
                       connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
            }
    }
                      )

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = []
    for row in result.all():
      result_dicts.append (row._mapping)
    return result_dicts


def load_job_from_db (id):
  with engine.connect as conn:
    result = conn.execute (text("select * from jobs where id=:val"), val=id)
    result_dicts = result.all
    if len(result_dicts) == 0 :
      return None
    else:
      return result_dicts[0]._mapping
      



 
 