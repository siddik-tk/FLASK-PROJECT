from flask import Flask,render_template,flash,request,redirect,url_for


app = Flask(__name__)
app.secret_key="nothing"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/search/<name>")
def search(name):
    return f"well come you {name} dump ass"

@app.route("/submit",methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    messages = request.form.get("messages")

    if not name or not messages:
        flash("all fields needs to be filled","error")
    else:
        flash(f"{name}! ,your data is submitted! ","success")

    return redirect(url_for('contact'))



if __name__ == "__main__":
    app.run(debug=True)