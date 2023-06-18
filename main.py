from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_form_to_db
#from sqlalchemy import text

app= Flask (__name__)



@app.route ("/")
def hello_world ():
  JOBS= load_jobs_from_db ()
  return render_template ( "home.html", jobs=JOBS, company_name="Jovian")

@app.route ("/jobs/<id>")
def show_job (id):
  print("id", id)
  job=load_job_from_db(id)
  if not job:
    return "Not Found", 404
  else:  
#    return jsonify(job)
     return render_template ("jobpage.html", job=job, company_name="Jovian")


@app.route ("/jobsapi")
def jobs_api ():
  JOBS= load_jobs_from_db ()
  return jsonify (JOBS)

@app.route ("/jobs/<id>/apply", methods=['post'])
def apply_job (id):
  data = request.form
  job=load_job_from_db(id)
  add_form_to_db (id, data)
  print("after data in apply")
  return render_template ("application_submitted.html", application=data, job=job)

if __name__ == "__main__" :
  app.run(host="0.0.0.0", port=5001, debug=True)
