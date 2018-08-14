from app import app
from flask import render_template, redirect, url_for, flash, request, Response, send_from_directory
# from app.forms import SubmitProductIdForm
# from app.export import export_csv
from werkzeug.urls import url_parse
import time
import os
from app.forms import SearchDFForm
from app.analysis import Analysis
from app.sentiment_analysis import SentimentAnalysis
from app.wordcloud import WordCloud
from app.index import Index


# Create an index route:
@app.route("/", methods=['GET','POST'])
@app.route("/index", methods=['GET','POST'])
def index():
    place = Index()
    directory = place.data_file
    # search = SearchForm(request.form)
    # if request.method == 'POST':
    return render_template('index.html', directory=directory)

@app.route('/get_city/<city>', methods=['GET', 'POST'])
def get_city(city):
        place = Index()
        place.selectCity(city)
        directory = place.data_file
        print(place.data_file)
        return redirect(url_for('index'))



# @app.route('/results')
# def search_results(search):
#     results = []
#     search_string = search.data['search']
#
#     if search.data['search'] == '':
#         qry = db_session.query(Album)
#         results = qry.all()
#
#     if not results:
#         flash('No results found!')
#         return redirect('/')
#     else:
#         # display results
#         return render_template('results.html', results=results)

@app.route('/analysis', methods=["GET","POST"])
def analysis():
        form = SearchDFForm()
        analysis = Analysis()
        word_cloud = WordCloud()
        if form.validate_on_submit():
            analysis_df = analysis.makeDF(form.input.data)
        else:
            analysis_df = analysis.makeDF()
        return render_template('analysis.html', analysis_df=analysis_df)

@app.route('/sentiment_analysis/<directory>', methods=["GET", "POST"])
def sentiment_analysis(directory):
    form = SearchDFForm()
    sa = SentimentAnalysis(directory)

    if form.validate_on_submit():
        sentiment_df = sa.makeSentDF(form.input.data)
    else:
        sentiment_df = sa.makeSentDF()



    return render_template('sentiment_analysis.html', sentiment_df = sentiment_df, form=form)





# @app.route('/parse')
# def parse():
#     return render_template('parse.html')
