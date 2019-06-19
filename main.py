from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "Hello World"

app.run()

<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                background-color: #eeee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <form method='POST'>
        <label>Rotate by:</label>
        <input type="text" name="rot" value="0" />
        <textarea name="text">{0}</textarea>
        input type="submit" value="Submit Query" />
    </form>

    </body>
</html>
""""
@app.rout("/")
def index():
    return form.format('')