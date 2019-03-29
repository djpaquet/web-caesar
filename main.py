from flask import Flask, request

ap = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!doctype html>
    <html>
        <head>
            <link href="styles.css" type="text/css" rel="stylesheet">
            </head>
        <body>
            <form action= method="post">
                <label></label>
                <input type="text" name="rot" />
                <input type="textarea" name="text" />
                </form>
            </body>
    </html>
    """
@app.route("/")
def index():
    return form

