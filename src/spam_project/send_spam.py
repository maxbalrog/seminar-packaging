# !/usr/bin/env python3
import numpy as np

import spam_project.spam
import spam_project.spam.email as spam_email

def print_spam():
    print('Sending spam...')
    print('-'*40)
    spam_email.send_spam_email()
    print('-'*40)
    print(f'printing numpy array for no reason: {np.arange(3)}')

if __name__ == '__main__':
    print_spam()