from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
dataset = pd.read_csv("data/sample_dataset.csv")

@app.route("/", methods=["GET"])
def home():
    return "Welcome to SocialSpark! Use the /chat endpoint to talk to the bot."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    if not user_input.strip():
        return jsonify({"response": "Please say something so I can help!"})

    if "hello" in user_input.lower():
        return jsonify({"response": "Hi! I'm SocialSpark. Ready to practice a conversation?"})
    elif "tip" in user_input.lower():
        return jsonify({"response": "Tip: Start conversations with open-ended questions."})
    elif "speech" in user_input.lower():
        return jsonify({"response": "Public speaking tip: Take a deep breath and slow down your pace."})
    else:
        # Pull a random dataset entry
        example = dataset.sample().iloc[0]
        return jsonify({"response": f"Try this ({example['situation']}): {example['response']}"} )

if __name__ == "__main__":
    app.run(debug=True)
