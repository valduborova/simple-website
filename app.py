from flask import Flask, render_template, request, redirect
import models
from database import SessionLocal

app = Flask(__name__)

db = SessionLocal()


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    res = db.query(models.Record).order_by(models.Record.date.desc()).all()
    return render_template('posts.html', res=res)


@app.route('/posts/<int:id>')
def article(id):
    res = db.query(models.Record).get(id)
    return render_template('article.html', rec=res)


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def update_article(id):
    article = db.query(models.Record).get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.commit()
            db.close()
            return redirect('/posts')
        except:
            return 'При редактировании статьи произошла ошибка'
    else:
        return render_template('update_article.html', article=article)

@app.route('/posts/<int:id>/delete')
def article_delete(id):
    res = db.query(models.Record).get(id)
    if res:
        try:
            db.delete(res)
            db.commit()
            return redirect('/posts')
        except:
            return 'При удалении статьи произошла ошибка'
    else:
        return 'Такой записи не существует'


@app.route('/create_article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = models.Record(title=title, intro=intro, text=text)
        try:
            db.add(article)
            db.commit()
            db.close()
            return redirect('/posts')
        except:
            return 'При добавлении статьи произошла ошибка'
    else:
        return render_template('create_article.html')


if __name__ == "__main__":
    app.run(debug=True)  # debug=True позволяет увидеть ошибки на странице
