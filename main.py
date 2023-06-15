from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
from sqlalchemy import text

app= Flask (__name__)



@app.route ("/")
def hello_world ():
  JOBS= load_jobs_from_db ()
  return render_template ( "home.html", jobs=JOBS, company_name="Jovian")

@app.route ("/jobsapi")
def jobs_api ():
  return jsonify (JOBS)

if __name__ == "__main__" :
  app.run(host="0.0.0.0", debug=True)
