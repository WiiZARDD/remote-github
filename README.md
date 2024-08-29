
# GitHub Workflow Bot

This Python bot automates the management of GitHub workflows, repositories, and notifications, integrating seamlessly with Slack for real-time updates. It can trigger workflows, monitor their status, create issues, merge pull requests, and send notifications via Slack.

## Features

- **Trigger Workflows**: Start specific GitHub Actions workflows with a simple command.
- **Monitor Workflow Status**: Check the status of running workflows and receive notifications on their progress or completion.
- **Create Issues**: Automate issue creation in your GitHub repositories.
- **Merge Pull Requests**: Automatically merge pull requests when they meet certain conditions.
- **Slack Notifications**: Receive real-time updates on workflow events directly in your Slack channel.
- **Webhooks**: Handles GitHub webhooks for real-time event processing.

## Configuration

Update the `config.py` file with your GitHub token, repository details, and Slack token:

```python
# config.py

GITHUB_TOKEN = 'your_github_token'
REPO_NAME = 'your_username/your_repo'
WORKFLOW_ID = 'your_workflow_id'
SLACK_TOKEN = 'your_slack_bot_token'
SLACK_CHANNEL = '#general'
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone
   cd (dir)
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**:
   ```bash
   python app.py
   ```

4. **Start the scheduler**:
   ```bash
   python scheduler.py
   ```

## Deployment

### Heroku

1. **Create a Heroku app**:
   ```bash
   heroku create app
   ```

2. **Push the code to Heroku**:
   ```bash
   git add .
   git commit -m "Deploying to Heroku"
   git push heroku master
   ```

### AWS EC2

1. **Launch an EC2 Instance** and SSH into it.

2. **Install Python and dependencies**:
   ```bash
   sudo yum install python3
   pip3 install PyGithub requests Flask APScheduler slack-sdk
   ```

3. **Transfer the script and run**:
   ```bash
   python3 app.py
   ```

## Usage

- **Trigger a Workflow**: The bot automatically triggers workflows based on the configuration.
- **Monitor Workflow**: The bot checks workflow statuses every 10 minutes by default.
- **Webhooks**: The Flask app listens for GitHub webhook events.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

Created by WiiZARDD. Credit to WiiZARDD for developing and maintaining this bot.
