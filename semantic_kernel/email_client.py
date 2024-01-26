import win32com.client
import win32com
import re

EMAILADDRESS = "beijiezhang@microsoft.com"
TOKEN_LIMIT = 8000
MAX_EMAILS = 8


def init():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    accounts= win32com.client.Dispatch("Outlook.Application").Session.Accounts

    return accounts, outlook


def get_contents(accounts, outlook):
    """Takes accounts and outlook
    Purpose: Gets emails from outlook
    Returns: dict of email subject -> body
    """
    emails = []

    for account in accounts:
        if str(account).lower() == EMAILADDRESS.lower():
            # print("Checking email account: {}".format(account))
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
                        if email.unread and "Canceled" not in subject:
                            body = email.Body
                            body = body.replace("\r\n", "<br>")
                            re.sub(r'<http\S+', '', body, flags=re.MULTILINE)
                            body = body.strip()
                            
                            content = subject + "<br>=====<br>" + body[:TOKEN_LIMIT]
                            emails.append(content)
                            count += 1

    # print("Finished checking emails")
    return emails


def get_emails():
    accounts, outlook = init()
    emails = get_contents(accounts, outlook)
    # print(len(emails))
    return emails

if __name__ == "__main__":
    get_emails()
