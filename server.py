from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)
print(random_number)

@app.route("/")
def home():
    return "\
        <h1>Guess a number between 0 and 9<h1>\
        <img src='https://media0.giphy.com/media/JdFEeta1hLNnO/giphy.gif?cid=ecf05e47ryme7m5710s8q1yidwabiuz8kukd24z2sv180v4e&rid=giphy.gif&ct=g' width=500px />"

@app.route("/<int:number>")
def guessed_number(number):
    if number > random_number:
        return "\
            <h1>Too high, guess again!<h1>\
            <img src='https://media1.giphy.com/media/RXAfuEDpseYBG/giphy.gif?cid=ecf05e47xqa612lvonpbhyf4neabigqd4jmdx0sq8adborfz&rid=giphy.gif&ct=g' width=500px />"
    if number < random_number:
        return "\
            <h1>Too low, guess again!<h1>\
            <img src='https://media3.giphy.com/media/4QD4OjqqE5M8U/giphy.gif?cid=ecf05e47f6m4uj4fyj9ww7tn54dyts9tqvxs4i3ovdw5iob3&rid=giphy.gif&ct=g' width=500px />"
    else:
        return "\
            <h1>That's right! Good job!<h1>\
            <img src='https://media1.giphy.com/media/xUjSOWCndCdECCyOEY/giphy.gif?cid=ecf05e47m511a3zx8xjj4v6hrnj5catvqejuapi9oczv4mja&rid=giphy.gif&ct=g' width=500px />"

if (__name__) == '__main__':
    app.run()
