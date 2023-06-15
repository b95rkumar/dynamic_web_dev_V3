import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://673dfnl202p9z8bp0jc7:pscale_pw_qNAtYDDydtbkdOPWplQm3xtkUzIknen9XYsE1AP1ktT@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4",
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



    


 
 