from github import Github
import requests
from slack_sdk import WebClient
from config import GITHUB_TOKEN, REPO_NAME, WORKFLOW_ID, SLACK_TOKEN, SLACK_CHANNEL

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)
client = WebClient(token=SLACK_TOKEN)

def trigger_workflow():
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    url = f"https://api.github.com/repos/{REPO_NAME}/actions/workflows/{WORKFLOW_ID}/dispatches"
    payload = {"ref": "main"}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 204:
        send_slack_notification(SLACK_CHANNEL, "Workflow triggered successfully!")
    else:
        print(f"Failed to trigger workflow: {response.status_code}")
        print(response.json())

def monitor_workflow():
    workflows = repo.get_workflows()
    for workflow in workflows:
        if workflow.id == WORKFLOW_ID:
            runs = workflow.get_runs()
            latest_run = runs[0] if runs.totalCount > 0 else None
            if latest_run:
                status = f"Latest run status: {latest_run.status}, Conclusion: {latest_run.conclusion}"
                send_slack_notification(SLACK_CHANNEL, status)
            break

def create_issue(title, body=None, labels=None):
    issue = repo.create_issue(title=title, body=body, labels=labels)
    send_slack_notification(SLACK_CHANNEL, f"Issue created: {issue.html_url}")

def merge_pull_request(pr_number, commit_message=None):
    pull = repo.get_pull(pr_number)
    if pull.mergeable_state == 'clean':
        pull.merge(commit_message=commit_message)
        send_slack_notification(SLACK_CHANNEL, f"Pull request #{pr_number} merged successfully!")
    else:
        send_slack_notification(SLACK_CHANNEL, f"Pull request #{pr_number} is not in a mergeable state.")

def send_slack_notification(channel, text):
    response = client.chat_postMessage(channel=channel, text=text)
    assert response["ok"]
