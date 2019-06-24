#!/usr/bin/env python3.7
# coding: utf-8

import sys
from webhook import Webhook, MessageBuilder
import subprocess

def main():
    args = sys.argv
    if len(args) <= 1: return

    slack = Webhook()

    results = subprocess.run(
            args[1:],
            capture_output=True,
            )
    returncode = results.returncode
    output = results.stdout

    messageBuilder = MessageBuilder()
    messageBuilder.setText(' '.join(results.args) + ' : ' + str(results.returncode))

    # stdout
    if (results.stdout != b''):
        text = results.stdout.decode()
        text = text.split('\n')[:-1]
        if (len(text) > 10): text = ['...'] + text[-10:]
        text = '\n'.join(text)
        messageBuilder.addAttachments(
                title = 'stdout',
                color = 'good',
                text = text,
                failback = 'stdout')

    # stderr
    if (results.stderr != b''):
        messageBuilder.addAttachments(
                title = 'stderr',
                color = 'danger',
                text = results.stderr.decode(),
                failback = 'stderr')

    slack.post(messageBuilder.getMessage())


if __name__ == '__main__':
    main()

