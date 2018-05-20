from twilio.rest import Client
import ClassScan

phone = ClassScan.get_config()


class client:
    """
    Wrapper for Twilio.Client
    Usage: sms.message, call.message
    """
    def __init__(self):
        self.number = phone.get('PHONE', 'NUMBER')
        self.sid = phone.get('PHONE', 'SID')
        self.token = phone.get('PHONE', 'TOKEN')
        self.client = Client(self.sid, self.token)

    def message(self, address, message):
        return False


class sms(client):
    def __init__(self):
        super().__init__()

    def message(self, address, message):
        self.client.messages.create(body=message, from_=self.number, to=address)
        return True


class call(client):
    def __init__(self):
        super().__init__()

    def message(self, address, message):
        self.client.calls.create(body=message, from_=self.number, to=address)
        return True