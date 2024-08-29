from flask import Flask, request, jsonify
from bot import send_slack_notification
from config import SLACK_CHANNEL

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if 'workflow_run' in data and data.get('action') == 'completed':
        conclusion = data['workflow_run']['conclusion']
        workflow_name = data['workflow_run']['name']
        notification = f"Workflow '{workflow_name}' completed with status: {conclusion}"
        send_slack_notification(SLACK_CHANNEL, notification)
    return jsonify({'message': 'Received'}), 200

if __name__ == "__main__":
    app.run(port=5000)
