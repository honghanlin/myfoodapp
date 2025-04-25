from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/detail/<int:food_id>')
def detail(food_id):
    return render_template('detail.html', food_id=food_id)

if __name__ == '__main__':
    app.run(debug=True)