from spam_project.spam.email import send_invitation
from spam_project.send_spam import print_spam
import spam_project.spam.collections as spam_collections

if __name__ == '__main__':
    print_spam()

    print('Sending invitation')
    send_invitation('Maksim')

    print(dir(spam_collections))