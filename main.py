from flask import Flask, request, render_template, jsonify
import os
import json

app = Flask(__name__)

# Store the latest webhook payload
latest_payload = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the JSON payload from the webhook
        payload = request.get_json()

        # Update the latest payload
        global latest_payload
        latest_payload = payload

        # You can process the payload here if needed

        return jsonify({'status': 'success'}), 200

    # For GET requests, render the HTML template with the payload
    return render_template('index.html', payload=json.dumps(latest_payload, indent=4))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
