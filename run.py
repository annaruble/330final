from flask import Flask, render_template, request
import records

app = Flask(__name__)

@app.route('/')
def hello():
    db2 = records.Database('sqlite:///mydb.db')
    res = db.query('select distinct continent from country')

    return render_template('index.html', continents=res)

@app.route('/processform')
def procform():
    continentx = request.args.get("continent")
    db = records.Database('postgresql://schuna05:@knuth.luther.edu/world')
    res = db.query('select * from country where continent = :continent limit 10', continent = continentx)

    return render_template('result.html', countries=res)


if __name__ == '__main__':
    app.run(debug=True)