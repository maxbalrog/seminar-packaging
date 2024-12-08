spam_template = '''
From: Matt Zepf (abcdefg@spam.com)
To: {}

Are you free???
'''

def send_spam_email(email='my-email@uni-jena.de'):
    spam = spam_template.format(email)
    print(spam)