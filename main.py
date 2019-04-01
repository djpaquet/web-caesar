from flask import Flask, request
from caesar import rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
        form {{
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }}

        textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
        </style>
    </head>
    <body>
        <form action="/" method='post'>
            <label for="rot">Rotate by:
                <input type='text' name='rot' id="rot" value='0' /></label>
            <textarea name='text'>{0}</textarea>
            <input type='submit' value='Encrypt Baby!'>
        </form>
            
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')


@app.route("/", methods=['POST'])

def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    mess = ''
    for letter in text:
        letter = rotate_character(letter,rot)
        mess += letter
    return form.format(mess)



app.run()