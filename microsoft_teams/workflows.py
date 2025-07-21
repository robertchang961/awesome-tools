"""Provide functionality to send adaptive cards to Microsoft Teams channels.

Load environment variables, construct the Teams card payload, and send it to the specified channel.
"""

import json
import os
import sys

import dotenv
import requests


def send_card(
        url: str,
        body: list[dict] | None = None,
        msteams: dict | None = None,
        actions: list[dict] | None = None,
    ) -> bool:
    """Send adaptive card to certain Microsoft Teams Channel."""
    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "version": "1.5",
                    "body": body,
                    "msteams": msteams,
                    "actions": actions,
                },
            },
        ],
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    try:
        response.raise_for_status()
        print("Successfully sent card to channel.")
        return True
    except Exception:
        print("Unable to send card to channel!")
        return False

def main() -> None:
    """Load environment variables, construct the Teams card payload, and send it to the specified channel."""
    if not dotenv.load_dotenv():
            print("Could not find the .env file, or it is empty!")
            sys.exit(1)

    url = os.getenv("URL")
    email = os.getenv("EMAIL")
    username = os.getenv("USERNAME")

    if not url:
        print("The URL could not be found in the .env file!")
        sys.exit(1)

    body = [
        {
            "type": "TextBlock",
            "text": "這週分享的是 <at>share</at>",
        },
    ]

    msteams = {
        "width": "Full",
        "entities": [
            {
                "type": "mention",
                "text": "<at>share</at>",
                "mentioned": {
                    "id": f"{email}",
                    "name": f"{username}",
                },
            },
        ],
    }

    actions = [
        {
            "type": "Action.OpenUrl",
            "title": "Google 官網",
            "url": "https://www.google.com/",
        },
    ]

    send_card(url, body, msteams, actions)


if __name__ == "__main__":
    main()
