from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def redirect_func():
    return redirect('https://www.google.com', code=301) # Google にリダイレクトする

if __name__ == '__main__':
    app.run()

