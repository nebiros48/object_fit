from flask import Flask, render_template

from game_of_life import SingletonMeta, GameOfLife

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    GameOfLife(25,25)
    return render_template('index.html')

@app.route('/live')
def live():  # put application's code here
    game = GameOfLife()
    game.form_new_generation()
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
