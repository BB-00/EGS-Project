from app import app
import requests

from flask import Flask, session, render_template, request, redirect, url_for, flash


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shop", methods=["POST","GET"])
def shop():
    if request.method == "POST" and 'add_to_cart' in request.form:

        prod_name = request.form["prod_name"]
        prod_price = request.form["prod_price"]
        prod_img = request.form["prod_img"]
        session["cart_item"].append({"prod_name":prod_name, "prod_price":prod_price, "prod_img":prod_img})
        session["checkout_cost"] += float(prod_price)
        
        session.modified = True
        return redirect(url_for("shop"))
    elif request.method == "POST" and 'log' in request.form:
        return redirect(url_for("login_page"))
    elif request.method == "POST" and 'rm_from_cart' in request.form:
        prod_name = request.form["prod_name"]
        i=0
        for item in session['cart_item']:
            if item['prod_name'] == prod_name:
                session['cart_item'].pop(i)
                session['checkout_cost'] = session['checkout_cost']-float(item['prod_price']) 
                session.modified = True
                return redirect(url_for("shop"))
            i=i+1
        
    else:
        return render_template("shop.html")

@app.route("/checkout", methods=["POST","GET"])
def checkout():

    if request.method == "POST":

        try:

            r = requests.post('http://127.0.0.1:9021/payments', json={"username":"lalala","amount":145})
            r.raise_for_status()
    
            return redirect('http://127.0.0.1:9021/payments', code=307)
        except:
            # flash("")
            return redirect(url_for("checkout"))        

    else:
        return render_template("checkout.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/register_page", methods=["POST","GET"])
def register_page():
    if request.method == "POST":
        # print(session['user'])

        try:
            r = requests.post('http://127.0.0.1:9020/register', request.form)
            r.raise_for_status()

            session.permanet = True

            user = request.form["username"]
            session["user"] = user
            session["cart_item"] = []
            session["checkout_cost"] = 0

            

            return redirect(url_for("index"))
        except:
            flash("Make sure you are inputing a valid email, username and password!")
            return redirect(url_for("register_page"))        

    else:
        return render_template("register.html")

@app.route("/login_page", methods=["POST","GET"])
def login_page():
    if request.method == "POST":
        # print(session['user'])

        try:
            r = requests.post('http://127.0.0.1:9020/token', request.form)
            r.raise_for_status()
            session.permanet = True
            user = request.form["username"]
            session["user"] = user
            session["cart_item"] = []
            session["checkout_cost"] = 0

            token = r.json()

            session["token"] = token.get('access_token')
            return redirect(url_for("index"))
        except requests.exceptions.HTTPError:
            flash("User or password incorrect!")
            return redirect(url_for("login_page"))        

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("cart_item", None)
    flash("Logging out!")
    return redirect(url_for("login_page"))
