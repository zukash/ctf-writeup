import os
import sqlite3
import subprocess

from flask import Flask, request, render_template

app = Flask(__name__)


@app.get("/")
def index():
    sequence = request.args.get("sequence", None)
    print(sequence)
    if sequence is None:
        return render_template("index.html")

    script_file = os.path.basename(sequence + ".dc")
    print(script_file)
    if " " in script_file or "flag" in script_file:
        return ":("

    print(script_file)
    print(type(script_file))
    print(script_file.encode())
    print("-e!ls\40#.dc".encode())
    print(script_file == "-e!ls\40#.dc")
    proc = subprocess.run(
        ["dc", script_file],
        capture_output=True,
        text=True,
        timeout=100,
    )
    output = proc.stdout
    print(f"{proc.stderr=}")

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
