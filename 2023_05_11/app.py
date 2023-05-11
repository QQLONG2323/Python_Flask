from flask import Flask, render_template, request
import datasource


app = Flask(__name__)
@app.route("/")
def index():
    stock_data = datasource.get_stock_data(stockid=2330)
    return render_template("index.jinja.html", data=stock_data)


@app.route("/features/")
def features():

    return render_template("features.jinja.html")

@app.route("/pricing/")
def pricing():
    
    return render_template("pricing.jinja.html")

@app.route("/about/")
def about():
    return render_template("about.jinja.html")

@app.route('/form/', methods=['GET', 'POST'])
def form():
    rows = datasource.get_stockid()
    if request.method == 'POST':
        stock_name = request.form['stock_name']
        print(stock_name)
        year =  request.form['year']
        return render_template("form.jinja.html",rows=rows,stock_name=stock_name,year=year)
    
    return render_template("form.jinja.html",rows=rows)