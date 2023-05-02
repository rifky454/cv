from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def halamanCV():
    return render_template("Fibonacci_Rifky.htlm")

if __name__=="__main__":
    app.run()