import Notification


class LightState:
    ON = 1
    OFF = 0


class Light(Notification.Notifier):
    def __init__(self):
        super().__init__()
        self.state = LightState.OFF
        self._light_color = {
            LightState.ON: (200, 200, 200),
            LightState.OFF: (0, 0, 0)
            }
        
    def flip_switch(self):
        if self.state == LightState.OFF:
            self.state = LightState.ON
        else:
            self.state = LightState.OFF
        self.notify()
    
    def notify(self):
        for s in self.subscribers:
            s.get_notification(state=self.state)
    
    def get_light_color(self):
        return self._light_color[self.state]
