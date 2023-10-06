from flask import Flask, render_template
from article_data import article_list

app = Flask(__name__)

article_list = article_list()

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/articles')
def articles():
   return render_template('articles.html', articles=article_list)

@app.route('/articles/<string:id>/')
def display_article(id):
   return render_template('articles_page.html', id=id, articles=article_list)

if __name__ == '__main__':
   app.run(debug=True)