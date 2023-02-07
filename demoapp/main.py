from flask import *

# Python Flaskの初期化
app = Flask(__name__)

# Phrudeプロファイラの読み込み
# from python_profiler import FlaskProfiler

# Phrudeプロファイラの設定
# FlaskProfiler(
#     app,
#     app_name="Python Flask DemoApp",
#     key="1e8a950f-745a-4cc5-a776-95dfa7c062f3",
#     endpoint="http://backend:8080/api",
# )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ssti", methods=["POST"])
def demo_ssti():
    return render_template_string("<p>Hello " + request.form["name"] + ".</p>")


@app.route("/stealer", methods=["GET"])
def demo_stealer():
    from stealer_package.fake import fake

    fake()
    return "Stealer demo is executed"


@app.route("/malware", methods=["GET"])
def demo_malware():
    from malware_package.fake import fake

    fake()
    return "Malware demo is executed"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
