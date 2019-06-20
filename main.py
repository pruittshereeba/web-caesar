from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{{
                background-color: #eeee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="rot">Rotate by:</label>
            <input type="number" name="rot" value="" />
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    form_rot = int(request.form['rot'])
    form_text = request.form['text']
    encrypted = rotate_string(form_text, form_rot)
    return form.format(encrypted)


app.run()