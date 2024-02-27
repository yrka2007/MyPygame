from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def first():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route("/index")
def index():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def reklama():
    lines = ["Человечество вырастает из детства.",
             "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.",
             "И начнем с Марса!",
             "Присоединяйся!"]
    return "<h2>" + '<br>'.join(lines) + '</h2>'

@app.route('/image_mars')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/Mars.jpg')}" 
                        alt="здесь должен быть марс но он потерялся">
                    <div class="alert alert-primary" role="alert">
                      Вот она какая красная планета
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run('127.0.0.1', 8080, debug=True)
