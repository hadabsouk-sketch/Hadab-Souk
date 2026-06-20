"""Hadab Souk — Flask e-commerce app."""
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from catalog import PRODUCTS, CATEGORIES, get_product, get_category, by_category, related
from translations import TRANSLATIONS
from shopify_service import (
    get_products,
    format_products,
    get_product_by_handle
)

app = Flask(__name__)
app.secret_key = "hadab-souk-change-this-secret-in-production"


@app.context_processor
def inject_globals():
    """Make lang, t, cart count available in every template."""
    lang = session.get("lang", "en")
    t = TRANSLATIONS[lang]
    cart = session.get("cart", {})
    cart_count = sum(cart.values())
    return {
        "lang": lang,
        "t": t,
        "dir": "rtl" if lang == "ar" else "ltr",
        "categories": CATEGORIES,
        "cart_count": cart_count,
        "name_field": "name_ar" if lang == "ar" else "name_en",
        "desc_field": "desc_ar" if lang == "ar" else "desc_en",
        "cat_name_field": "name_ar" if lang == "ar" else "name_en",
    }


@app.route("/set-lang/<lang>")
def set_lang(lang):
    if lang in ("en", "ar"):
        session["lang"] = lang
    return redirect(request.referrer or url_for("index"))


# ---------- Pages ----------
@app.route("/")
def index():
    products = format_products()

    return render_template(
        "index.html",
        featured=products,
        best=products,
        deals=products[:4]
    )


@app.route("/shop")
def shop():
    q = request.args.get("q", "").strip().lower()
    sort = request.args.get("sort", "featured")
    items = format_products()
    if q:
        items = [p for p in items if q in p["name_en"].lower() or q in p["name_ar"] or q in p["brand"].lower()]
    if sort == "low":
        items.sort(key=lambda p: p["price"])
    elif sort == "high":
        items.sort(key=lambda p: -p["price"])
    elif sort == "rating":
        items.sort(key=lambda p: -p["rating"])
    return render_template("shop.html", products=items, q=q, sort=sort)

@app.route("/category/<slug>")
def category(slug):
    cat = get_category(slug)
    if not cat:
        return render_template("404.html"), 404
    items = by_category(slug)
    return render_template("category.html", category=cat, products=items)


@app.route("/product/<slug>")
def product(slug):

    data = get_product_by_handle(slug)

    node = data["data"]["product"]

    p = {
    "id": node["id"],
    "slug": node["handle"],

    "name_en": node["title"],
    "name_ar": node["title"],

    "desc_en": node["description"],
    "desc_ar": node["description"],

    "image": node["featuredImage"]["url"] if node.get("featuredImage") else "",

    "price": float(
        node["priceRange"]["minVariantPrice"]["amount"]
    ),

    "brand": "Hadab Souk",
    "category": "electronics",

    "rating": 5,
    "reviews": 0,
    "old_price": None
}
    return render_template(
        "product.html",
        product=p,
        related=[]
    )
    if not p:
        return render_template("404.html"), 404
    return render_template("product.html", product=p, related=related(p))


# ---------- Cart ----------
@app.route("/cart")
def cart_view():
    cart = session.get("cart", {})
    items = []
    subtotal = 0
    for pid, qty in cart.items():
        p = next((x for x in PRODUCTS if x["id"] == pid), None)
        if p:
            line = p["price"] * qty
            subtotal += line
            items.append({"product": p, "qty": qty, "line": line})
    return render_template("cart.html", items=items, subtotal=subtotal)


@app.route("/cart/add/<pid>", methods=["POST"])
def cart_add(pid):
    qty = int(request.form.get("qty", 1))
    cart = session.get("cart", {})
    cart[pid] = cart.get(pid, 0) + qty
    session["cart"] = cart
    if request.headers.get("X-Requested-With") == "fetch":
        return jsonify({"count": sum(cart.values())})
    return redirect(url_for("cart_view"))


@app.route("/cart/update/<pid>", methods=["POST"])
def cart_update(pid):
    qty = int(request.form.get("qty", 1))
    cart = session.get("cart", {})
    if qty <= 0:
        cart.pop(pid, None)
    else:
        cart[pid] = qty
    session["cart"] = cart
    return redirect(url_for("cart_view"))


@app.route("/cart/remove/<pid>", methods=["POST"])
def cart_remove(pid):
    cart = session.get("cart", {})
    cart.pop(pid, None)
    session["cart"] = cart
    return redirect(url_for("cart_view"))


# ---------- Checkout ----------
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = session.get("cart", {})
    items = []
    subtotal = 0
    for pid, qty in cart.items():
        p = next((x for x in PRODUCTS if x["id"] == pid), None)
        if p:
            subtotal += p["price"] * qty
            items.append({"product": p, "qty": qty})

    discount = 0
    coupon = request.form.get("coupon", "").strip().upper() if request.method == "POST" else ""
    if coupon == "HADAB10":
        discount = subtotal * 0.10
    shipping = 0 if subtotal >= 200 else 25
    total = subtotal - discount + shipping

    if request.method == "POST" and request.form.get("action") == "place":
        session["cart"] = {}
        flash(TRANSLATIONS[session.get("lang", "en")]["order_success"], "success")
        return redirect(url_for("index"))

    return render_template(
        "checkout.html",
        items=items, subtotal=subtotal, shipping=shipping,
        discount=discount, total=total, coupon=coupon,
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks! We'll get back to you soon.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.route("/shopify-test")
def shopify_test():
    return get_products()

@app.route("/shopify-products")
def shopify_products():
    return get_products()
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
