from abc import ABC, abstractmethod

# Polimorfismo
class Notification(ABC):
    
    def __init__(self, message) -> None:
        self.message = message
    
    @abstractmethod
    def send(self) -> bool: ...
        # print(f'send message {self.message}')


class EmailNotification(Notification):

    def send(self) -> bool:
        print(f'send EMAIL message {self.message}')
        return True


class SMSNotification(Notification):

    def send(self) -> bool:
        print(f'send SMS message {self.message}')
        return True



n = EmailNotification('Testando notificacao')
n.send()


n2 = SMSNotification('Testando notificacao')
n2.send()


def notificate(notification: Notification):
    n = notification.send()
    if n:
        print('Notificacao enviada')
    else:
        print('Notificacao NAO enviada')

notificate(n)
notificate(n2)




