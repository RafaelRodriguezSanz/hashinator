from flask import Flask, request, render_template, jsonify
import hashlib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hash_result = None
    hash_type = "sha256"
    if request.method == "POST":
        password = request.form.get("password")
        hash_type = request.form.get("hash_type")
        if password:
            m = getattr(hashlib, hash_type)()
            m.update(password.encode())
            hash_result = m.hexdigest()
    return render_template("index.html", hash_result=hash_result, hash_type=hash_type)


@app.route('/health')
def health():
    return jsonify(status="OK"), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
