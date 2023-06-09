from flask import Flask, render_template, jsonify

app= Flask (__name__)

JOBS=[
  {
  'id':1,
  'title':'Data Scietist',
  'location':'New Delhi, India',
  'salary':'Rs 10,00,000'
  },
  {
  'id':2,
  'title':'Data Analyst',
  'location':'Bengurule, India',
  'salary':'Rs 12,00,000'
  },
  {
  'id':3,
  'title':'Data Base expert',
  'location':'USA',
  'salary':'$ 110,000'
  },
  {
  'id':4,
  'title':'Data Scietist Manager',
  'location':'New Delhi, India'
  }
]

@app.route ("/")
def hello_world ():
  return render_template ( "home.html", jobs=JOBS, company_name="Jovian")

@app.route ("/jobsapi")
def jobs_api ():
  return jsonify (JOBS)

if __name__ == "__main__" :
  app.run(host="0.0.0.0", debug=True)
