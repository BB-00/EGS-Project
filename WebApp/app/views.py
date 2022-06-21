from app import app
import requests
import json
import random

from flask import Flask, session, render_template, request, redirect, url_for, flash


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        prod_name = request.form["prod_name"]
        i=0
        for item in session['cart_item']:
            if item['prod_name'] == prod_name:
                session['cart_item'].pop(i)
                session['checkout_cost'] = session['checkout_cost']-float(item['prod_price']) 
                session.modified = True
                return redirect(url_for("index"))
            i=i+1
    else:
        return render_template("index.html")

@app.route("/shop", methods=["POST","GET"])
def shop():
    if request.method == "POST" and 'add_to_cart' in request.form:

        prod_name = request.form["prod_name"]
        prod_price = request.form["prod_price"]
        prod_img = request.form["prod_img"]
        prod_amount = request.form["prod_amount"]
        session["cart_item"].append({"prod_name":prod_name, "prod_price":prod_price, "prod_img":prod_img, "prod_amount":prod_amount})
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

    if request.method == "POST" and 'checkout' in request.form:

        try:

            r = requests.get('http://127.0.0.1:9023/MysteryShirt/Stock/1/products')
            r.raise_for_status()
            
            product_count=r.json().count("product_ID")

            lista=r.json().split("product_ID")
            prod_id=lista[product_count].split()[1][:-1]
            amount=0

            for item in session['cart_item']:
                # print(item['prod_amount'])
                amount=amount-int(item['prod_amount'])

            params = {  'buy_price': 0, 
                        'material': 0, 
                        'name': 'string', 
                        "product_ID": int(prod_id),
                        "product_type": 0,
                        "provider": 0,
                        "quantity": amount,
                        "reference": 0,
                        "size": 0
                    }

            r_p = requests.post('http://127.0.0.1:9023/MysteryShirt/Stock/1/products', json=params)
            r_p.raise_for_status()

            session.pop("cart_item", None)

            return redirect('http://127.0.0.1:9021/payments', code=307)
        except:
            # flash("")
            return redirect(url_for("checkout")) 
    
    elif request.method == "POST" and 'rm_from_cart' in request.form:
        prod_name = request.form["prod_name"]
        i=0
        for item in session['cart_item']:
            if item['prod_name'] == prod_name:
                session['cart_item'].pop(i)
                session['checkout_cost'] = session['checkout_cost']-float(item['prod_price']) 
                session.modified = True
                return redirect(url_for("checkout"))
            i=i+1

    elif request.method == "POST" and 'rm_cart' in request.form:
        prod_name = request.form["prod_name"]
        i=0
        for item in session['cart_item']:
            if item['prod_name'] == prod_name:
                session['cart_item'].pop(i)
                session['checkout_cost'] = session['checkout_cost']-float(item['prod_price']) 
                session.modified = True
                return redirect(url_for("checkout"))
            i=i+1
    else:
        return render_template("checkout.html")


@app.route("/team", methods=["POST","GET"])
def team():
    if request.method == "POST":
        prod_name = request.form["prod_name"]
        i=0
        for item in session['cart_item']:
            if item['prod_name'] == prod_name:
                session['cart_item'].pop(i)
                session['checkout_cost'] = session['checkout_cost']-float(item['prod_price']) 
                session.modified = True
                return redirect(url_for("team"))
            i=i+1
    else:
        return render_template("team.html")

@app.route("/register_page", methods=["POST","GET"])
def register_page():
    if request.method == "POST":
        # print(session['user'])

        try:

            # print("p",request.form['username'].replace(" ",""),"p")
            # print("p",request.form['email'],"p")
            # print("p",request.form['password'],"p")

            params = {  "username": request.form['username'], 
                        "email": request.form['email'], 
                        "password": request.form['password']
                    }


            r = requests.post('http://127.0.0.1:9020/register', json=params)
            r.raise_for_status()

            session.permanet = True

            user = request.form["username"]
            session["user"] = user
            session["cart_item"] = []
            session["checkout_cost"] = 0

            url = 'http://127.0.0.1:9021/wallets/?_username='+session['user']
            print(url)
            r = requests.post(url)

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

@app.route("/payment_successfull", methods=["POST","GET"])
def payment_successfull():

    return render_template("payment_successfull.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("cart_item", None)
    session.pop("token",None)
    flash("Logging out!")
    return redirect(url_for("login_page"))

@app.route("/orders")
def orders():

    url = 'http://127.0.0.1:9021/wallets/?_username='+session['user']

    return redirect(url)

@app.route("/checkout_info")
def checkout_info():
    
    return session
