spam_template = '''
From: Matt Zepf (abcdefg@spam.com)
To: {}

Are you free???
'''

invite_template = '''
Dear {},

We invite You to the next CHIPS seminar!
'''

def send_spam_email(email='my-email@uni-jena.de'):
    spam = spam_template.format(email)
    print(spam)

def send_invitation(name):
    invite = invite_template.format(name)
    print(invite)