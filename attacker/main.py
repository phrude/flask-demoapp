import pprint

from flask import *

app = Flask(__name__)

data = []


@app.route("/", methods=["GET", "POST"])
def show_data():
    if request.method == "GET":
        return pprint.pformat(data)

    else:
        data.append(request.form.to_dict())
        return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
