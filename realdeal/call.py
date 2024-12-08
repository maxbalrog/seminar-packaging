import sys
sys.path.append('.')

from spam.email import send_invitation
from send_spam import print_spam
import collections

print_spam()

print('Sending invitation')
send_invitation('Maksim')

print(dir(collections))