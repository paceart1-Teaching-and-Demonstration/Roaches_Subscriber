
class Subscriber:
    def __init__(self):
        pass
    
    def get_notification(self, **kwargs):
        print("Notification Received.")
        print(f"kwargs: {kwargs}")


class Notifier:
    def __init__(self):
        self.subscribers = []
        
    def notify(self):
        for subscriber in self.subscribers:
            subscriber.get_notification()
    
    def subscribe(self, subscriber):
        # TODO : Needs type check
        self.subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)


if __name__ == "__main__":
    sub = Subscriber()
    notif = Notifier()

    notif.subscribe(sub)
    notif.notify()