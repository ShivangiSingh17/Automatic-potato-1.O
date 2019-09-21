import base64
from email.mime.text import MIMEText
#from google-api-python-client import discovery
import googleapiclient
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client import file
import httplib2
import os
from googleapiclient.discovery import build



def create_message(sender, to, subject, message_text):
  
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string())}


SCOPES = "https://mail.google.com/"
CLIENT_SECRET_FILE = 'Ruby project-cdf10a6d136d.json'
APPLICATION_NAME = 'Ruby project'
def get_creds():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, 'Desktop/mail')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                             'credentials.json')
 
    store = oauth2client.file.Storage(credential_path)
    #credentials = ""
    try:
        credentials = store.get()
        return credentials
    except:
        print('Working with flow-based credentials instantiation')
    


def send_message(service, user_id, message):

    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    #print 'Message Id: %s' % message['id']
    return message



if __name__  == '__main__':
    creds = get_creds()
    #http = creds.authorize(httplib2.Http())
    service = build('gmail', 'v1', credentials=creds)
    message = create_message("me","example@gmail.com","test header","test mail",)
    send_message(service,"me",message)