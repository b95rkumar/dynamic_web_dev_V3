import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONN_STR']
#print("db_connection_string", db_connection_string)
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
  print ("Inside this")
  with engine.connect() as conn:
    result = conn.execute (text(f"select * from jobs where id = :val"), {"val":id})
    result_dicts = result.mappings().all()
    if len(result_dicts) == 0 :
      return None
    else:
      #print ("result_dics", result_dicts[0]._mapping)
      return dict(result_dicts[0])      

def add_form_to_db (job_id, data): 
  with engine.connect() as conn:
    query = text(f"insert into job_applications (job_id, full_name,email_id, linkedin_url, resume_url, work_experience, education) values (:job_id, :full_name,:email_id, :linkedin_url, :resume_url, :work_experience, :education)")
    conn.execute (query, {"job_id":job_id, "full_name": data['full_name'],"email_id":data['email_id'],"linkedin_url":data['linkedin_url'],"resume_url":data['resume_url'],"work_experience":data['work_experience'],"education":data['education']})
    

 
 