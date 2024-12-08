import spam
import spam.email

def print_spam():
    print('Sending spam...')
    print('-'*40)
    spam.email.send_spam_email()
    print('-'*40)

if __name__ == '__main__':
    print_spam()