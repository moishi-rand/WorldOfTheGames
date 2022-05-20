from flask import Flask

# Return string as html format for display score
def score_server():
    player_score = 0
    str_for_html = ""

    try:
        score_file = score_file = open("../Utills/my_text.txt", "r")
        player_score = score_file.read()
        str_for_html = f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is: <div id="score">{player_score}</div></h1>
                </body>
            </html>
        """
        score_file.close()
    except:
        error = exec()
        str_for_html = f""""
                    <html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1><div id="score" style="color:red">{error}</div></h1>
                        </body>
                    </html>
                """

    return str_for_html

#Run service of display main score
app = Flask(__name__)

# accessed via <HOST>:<PORT>/
@app.route("/")
def welcome():
    return score_server(), 200 # status code

app.run(host='127.0.0.1', debug=True, port=5000)

