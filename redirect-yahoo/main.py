from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def redirect_func():
    return redirect('https://www.yahoo.co.jp', code=301) # Yahoo にリダイレクトする

if __name__ == '__main__':
    app.run()

