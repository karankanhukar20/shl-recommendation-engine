from flask import Flask, request
from recommend import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = ""
    if request.method == "POST":
        user_input = request.form["skills"]
        recs = recommend(user_input)
        results = recs.to_html(index=False, classes="table")

    return f"""
    <html>
    <head>
        <title>SHL Recommendation Engine</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(120deg,#4f46e5,#06b6d4);
                color: white;
                text-align: center;
                padding-top: 60px;
            }}
            .box {{
                background: white;
                color: black;
                width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            }}
            input {{
                padding: 10px;
                width: 70%;
                border-radius: 6px;
                border: 1px solid #ccc;
            }}
            button {{
                padding: 10px 18px;
                border: none;
                background: #4f46e5;
                color: white;
                border-radius: 6px;
                cursor: pointer;
                font-weight: bold;
            }}
            button:hover {{
                background: #4338ca;
            }}
            table {{
                margin: auto;
                border-collapse: collapse;
                margin-top: 20px;
                color: black;
                background: white;
            }}
            th, td {{
                padding: 10px 15px;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background: #4f46e5;
                color: white;
            }}
        </style>
    </head>

    <body>
        <div class="box">
            <h2>🎯 SHL Assessment Recommendation Engine</h2>
            <p>Enter skills or job role to get recommended assessments</p>

            <form method="post">
                <input name="skills" placeholder="e.g. data analyst python sql">
                <br><br>
                <button type="submit">Get Recommendations</button>
            </form>

            {results}
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)