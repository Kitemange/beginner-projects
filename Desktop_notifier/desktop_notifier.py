#env!/usr/bin/env python3

from plyer import notification

# Regular notification
notification.notify(
    title='Regular Notification',
    message='This is a regular notification.',
    app_name='Astro',
    timeout=10
)
