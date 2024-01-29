import win32com.client
import win32com
import re

EMAILADDRESS = "beijiezhang@microsoft.com"
TOKEN_LIMIT = 8000
MAX_EMAILS = 8
MAX_SEARCH_EMAILS = 50


def init():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    accounts= win32com.client.Dispatch("Outlook.Application").Session.Accounts

    return accounts, outlook


def fetch_emails(accounts, outlook):
    """Takes accounts and outlook
    Purpose: Gets emails from outlook
    Returns: list of emails
    """
    emails = []

    for account in accounts:
        if str(account).lower() == EMAILADDRESS.lower():
            folders = outlook.Folders(account.DeliveryStore.DisplayName)
            specific_folder = folders.Folders

            # Loop through all folders            
            for folder in specific_folder:    
                # Restricts the program to only check this folder
                if folder.name == "Inbox":
                    messages = folder.Items
                    messages.Sort("[ReceivedTime]", True)

                    # Loop through all messages
                    count = 1
                    for email in messages:
                        if count > MAX_EMAILS:
                            return emails
                        # For some reason deleted but unread emails are stored in the Inbox on the backend
                        subject = email.Subject
                        if subject and email.body and not email.unread and "Canceled" not in subject:
                            body = email.Body
                            body = body.replace("\r\n", "<br>")
                            re.sub(r'<http\S+', '', body, flags=re.MULTILINE)
                            body = body.strip()
                            
                            content = subject + "<br>=====<br>" + body[:TOKEN_LIMIT]
                            emails.append(content)
                            count += 1

    return emails

def fetch_contents(accounts, outlook):
    """Takes accounts and outlook
    Purpose: Gets emails from outlook
    Returns: dict of email subject -> body
    """
    contents = {}
    count = 0

    for account in accounts:
        if str(account).lower() == EMAILADDRESS.lower():
            folders = outlook.Folders(account.DeliveryStore.DisplayName)
            specific_folder = folders.Folders

            # Loop through all folders            
            for folder in specific_folder:    
                # Restricts the program to only check this folder
                
                messages = folder.Items
                # Loop through all messages
                for email in messages:
                    # For some reason deleted but unread emails are stored in the Inbox on the backend
                    if count > MAX_SEARCH_EMAILS:
                        return contents
                    subject = email.Subject
                    if email and "Canceled" not in subject:
                        body = email.Body
                        body = body.replace("\r\n", "<br>")
                        body = body.replace("\t", "")
                        re.sub(r'<http\S+', '', body, flags=re.MULTILINE)
                        body = body.strip()
                        
                        contents[subject] = body
                        count += 1
                        
    return contents


def get_emails():
    accounts, outlook = init()
    emails = fetch_emails(accounts, outlook)
    return emails

def get_contents():
    accounts, outlook = init()
    contents = fetch_contents(accounts, outlook)
    return contents

if __name__ == "__main__":
    get_emails()
