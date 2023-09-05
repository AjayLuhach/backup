from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def squarenumber():
    if request.method == "GET":
        # If 'num' is None, the user has requested page the first time
        if request.args.get("num") == None:
            return render_template("squarenum.html")

        elif request.args.get("num") == "":
            return "<html> <h1>Invalid number</h1> </html>"
        else:
            number = request.args.get("num")
            sq = int(number) * int(number)

            return render_template("answer.html", squareofnum=sq, num=number)


if __name__ == "__main__":
    app.run(debug=True)
