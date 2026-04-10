from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
if __name__ == "__main__":
    app.run()
    <p>🎁 Daily bonus applied!</p>
    c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    coins INTEGER,
    last_claim TEXT
)
''')
