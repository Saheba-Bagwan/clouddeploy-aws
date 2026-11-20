from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CloudDeploy AWS</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 750px;
                margin: 80px auto;
                padding: 20px;
                line-height: 1.7;
                background: #f4f7fb;
                color: #1f2937;
            }

            .card {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 18px rgba(0, 0, 0, 0.08);
            }

            h1 {
                color: #146eb4;
            }

            .status {
                color: #18794e;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>CloudDeploy AWS</h1>

            <p>
                Welcome to our automated DevOps deployment project.
            </p>

            <p class="status">
                Application status: Running
            </p>

            <h3>Technologies</h3>

            <ul>
                <li>Python and Flask</li>
                <li>Docker</li>
                <li>GitHub Actions</li>
                <li>AWS EC2</li>
                <li>Amazon CloudWatch</li>
            </ul>

            <p>
                Our goal is to automate application testing,
                containerization, deployment, and monitoring.
            </p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "CloudDeploy AWS"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
