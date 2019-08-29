"""Notify Pack."""
import requests

LINE_TOKEN = ''


def set_line_token(token):
    """Set line token."""
    global LINE_TOKEN
    LINE_TOKEN = token


def notify_line(message):
    """Notify line of message."""
    if LINE_TOKEN:
        line_notify_api = 'https://notify-api.line.me/api/notify'
        payload = {'message': message}
        headers = {'Authorization': 'Bearer ' + LINE_TOKEN}
        requests.post(line_notify_api, data=payload, headers=headers)
