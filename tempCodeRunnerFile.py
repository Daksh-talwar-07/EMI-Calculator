from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    emi = None
    error = None

    if request.method == "POST":
        loan = request.form.get("loan")
        rate = request.form.get("rate")
        time = request.form.get("years")

        # 1️⃣ Check empty fields
        if not loan or not rate or not time:
            error = "Please fill all fields"

        else:
            try:
                loan = float(loan)
                rate = float(rate)
                time = float(time)

                # 2️⃣ Check zero or negative values
                if loan <= 0 or rate <= 0 or time <= 0:
                    error = "All values must be greater than 0"

                else:
                    # 3️⃣ EMI calculation
                    r = rate / (12 * 100)
                    n = time * 12

                    emi = (loan * r * math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)
                    emi = format(emi, ",.2f")


            except ValueError:
                error = "Invalid input"

    return render_template("index.html", emi=emi, error=error)


if __name__ == "__main__":
    app.run(debug=True)
