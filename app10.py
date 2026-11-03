from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/n8n-webhook', methods=['POST'])
def n8n_webhook():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400
    print("Received from n8n:", data)
    # Store or process the data
    return jsonify({"status": "received", "data": data})
if __name__ == '__main__':
    app.run(debug=True, port=5000)