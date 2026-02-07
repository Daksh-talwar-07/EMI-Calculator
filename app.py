from flask import Flask, render_template, request
import math

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    emi=None
    error=None
    currency=request.form.get("currency")
    currency_map={
        "INR":"₹",
        "USD":"$",
        "EUR":"€",
        "GBP": "£",
        "JPY": "¥"
    }

    if request.method == "POST":
        loan=float(request.form.get("loan"))
        rate=float(request.form.get("rate"))
        time=float(request.form.get("years"))

        if not loan or not rate or not time:
            error = "Please fill all fields"

        else:
            try:
                loan=float(loan)
                rate=float(rate)
                time=float(time)

                if loan<=0 or rate<=0 or time<=0:
                    error = "All values must be greater than 0"

                else:
                    r=rate/(12*100)
                    n=time*12

                    symbol = currency_map.get(currency, "₹")

                    emi = (loan * r * (1 + r) ** n) / ((1 + r) ** n - 1)
                    emi = f"{symbol}{emi:,.2f}"



            except ValueError:
                error="Invalid input"

    return render_template("index.html", emi=emi,error=error)


if __name__ == "__main__":
    app.run(debug=True)
