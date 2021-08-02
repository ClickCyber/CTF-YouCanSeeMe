from flask import *
import json

msg = "You Hacked Me good Job !"
app = Flask(__name__, template_folder='./view')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        if len(request.form["text"]) > 100:
            raise "log username/paswword"
        with open(f'./contact/{request.form["email"]}', 'w+') as f:
            f.write(f'{request.form["text"]}\n')
            return render_template('index.html', contact=True, save_contact=True)
    return render_template('index.html', contact=True)


@app.route('/login', methods=["GET", "POST"])
def login():
    error = ''
    DB = json.load(open('accounts.json', 'r'))
    if request.method == "POST":
        if DB["username"] == request.form["username"] and DB["password"] == request.form["password"]:
            return render_template('admin.html', login=True, flags=msg)
        elif len(request.form["password"]) > 20 | len(request.form["username"]) > 20:
            raise "long username/paswword"
        else:
            raise "Wrong username/paswword"

    return render_template('admin.html', login=False)


if __name__ == "__main__":
    app.run(port=80, debug=True)