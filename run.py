from flask import Flask, render_template, request
from collections import OrderedDict
import records

app = Flask(__name__)

@app.route('/')
def hello():
    db = records.Database('sqlite:///mydb.db')
    res = db.query('select distinct country from release_date order by country')
    res2 = db.query('select distinct year from release_date order by year desc')
    
    res3 = OrderedDict([('None','None'),('Jan','Jan'),('Feb','Feb'),('Mar','Mar'),('Apr','Apr'),('May','May'),('June','June'),('July','July'),('Aug','Aug'),('Sep','Sep'),('Oct','Oct'),('Nov','Nov'),('Dec','Dec')])
    return render_template('index.html', countries=res,years=res2,months=res3 )

@app.route('/processform')
def procform():
    countryx = request.args.get("country")
    yearx = request.args.get("year")
    monthx = request.args.get("month")
    res3 = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'June':6,'July':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    db = records.Database('sqlite:///mydb.db')
    if monthx == "None" and yearx == "None":
        res = db.query('select * from release_date where country = :country', country = countryx)
    elif monthx == "None":
        res = db.query('select * from release_date where country = :country and year = :year', country = countryx, year =yearx)
    elif yearx == "None":
        res = db.query('select * from release_date where country = :country and month = :month', country = countryx, month = res3[monthx])
    else:
        res = db.query('select * from release_date where country = :country and year = :year and month = :month', country = countryx, year =yearx, month = res3[monthx])

    return render_template('result.html', movress=res)

@app.route('/rendermovie')
def getMovieInfo():
    moviex = request.args.get("movie")
    #x = len(moviex)
    db = records.Database('postgresql://schuna05:@knuth.luther.edu/movies')
    res = db.query('select * from moviecast where title = :movie order by n', movie = moviex)


    return render_template('movie.html',actors = res)



if __name__ == '__main__':
    app.run(debug=True)
