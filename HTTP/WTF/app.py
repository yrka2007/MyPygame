from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def start(title):
    return render_template('index.html', title=title)


@app.route('/traning/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        tren = 'Инжинерные тренажёры'
        pic = 'ShemaIS.jpg'
    else:
        tren = 'Научные тренажёры'
        pic = 'ShemaNS.jpg'
    pic_out = url_for('static', filename=f'img/{pic}')
    return render_template("prof.html", title=prof, title2=tren, pic=pic_out)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
