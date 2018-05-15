from flask import Flask, render_template, request
import records

app = Flask(__name__)

@app.route('/')
def hello():
    db = records.Database('postgresql://schuna05:@knuth.luther.edu/movies')
    res = db.query('select distinct country from release_date order by country')
    res2 = db.query('select distinct year from release_date order by year')
    #res3 = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'June':6,'July':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    res3 = {'Jan':'Jan','Feb':'Feb','Mar':'Mar','Apr':'Apr','May':'May','June':'June','July':'July','Aug':'Aug','Sep':'Sep','Oct':'Oct','Nov':'Nov','Dec':'Dec'}
    return render_template('index.html', countries=res,years=res2,months=res3 )

@app.route('/processform')
def procform():
    countryx = request.args.get("country")
    yearx = request.args.get("year")
    monthx = request.args.get("month")
    db = records.Database('postgresql://schuna05:@knuth.luther.edu/movies')
    res = db.query('select * from release_date where country = :country and year = :year limit 10', country = countryx, year =yearx)

    return render_template('result.html', movress=res)



if __name__ == '__main__':
    app.run(debug=True)
