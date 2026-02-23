from imapclient import IMAPClient
import pyzmail

EMAIL = "kushwahnitii447@gmail.com"
APP_PASSWORD = "rpghwfrffmttcbuh"

def fetch_latest_email():

    with IMAPClient("imap.gmail.com") as client:
        client.login(EMAIL, APP_PASSWORD)
        client.select_folder("INBOX")

        messages = client.search(['UNSEEN'])

        if not messages:
            return None

        latest = messages[-1]
        raw = client.fetch([latest], ['BODY[]', 'FLAGS'])

        msg = pyzmail.PyzMessage.factory(raw[latest][b'BODY[]'])

        subject = msg.get_subject()

        if msg.text_part:
            body = msg.text_part.get_payload().decode(msg.text_part.charset)
        else:
            body = msg.html_part.get_payload().decode(msg.html_part.charset)

        return {
            "subject": subject,
            "body": body
        }