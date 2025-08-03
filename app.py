from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-login', methods=['POST'])
def test_login():
    username = request.form['username']
    return f"✅ Test login başarılı: {username} (şifre kaydedilmedi)"

if __name__ == '__main__':
    app.run(debug=True)
