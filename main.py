from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        secret = request.cookies.get("secret_number")
        res = make_response(render_template("index.html"))

        if not secret:
            secret_new = random.randint(1, 30)
            res.set_cookie("secret_number", str(secret_new))

        return res

    elif request.method == "POST":
        guess = int(request.form.get("guess"))
        secret = int(request.cookies.get("secret_number"))
        print(guess)

        if guess == secret:
            msg = "You've guessed it - congratulations! It's number {0}".format(str(secret))
            res = make_response(render_template("success.html", message=msg))
            res.set_cookie("secret_number", str(random.randint(1, 30)))
            return res
        elif guess > secret:
            msg = "Your guess is not correct... try something smaller."
            return render_template("wrong.html", message=msg)
        elif guess < secret:
            msg = "Your guess is not correct... try something bigger."
            return render_template("wrong.html", message=msg)





if __name__ == '__main__':
    app.run()
