from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def route1():
    return render_template("index.html")

@app.route("/auth", methods=['POST'])

def route2():
    print request.method
    if request.form["user"] == "tester" and request.form["pass"] == "pass":
        return "login successful"
    return "login unsuccessful. try again"

@app.route("/three")

def route3():
	return "this is the third route"

if __name__ == "__main__":
    app.debug = True
    app.run()
