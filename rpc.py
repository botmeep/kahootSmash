from pypresence import Presence

CLIENT_ID = 929826161956098139

class RPC:
    def __init__(self):
        self.rpc = Presence(CLIENT_ID)
    def start(self):
        self.rpc.connect()
        self.rpc.update(state="Currently Idle",
        large_image="kahooticon",
        details="Flooding Kahoots with Bots",
        large_text="Spams Kahoots with bot users",
        buttons=[{"label":"Download Kahoot Smasher", "url":"https://github.com/botmeep/kahootSmash/"}])
    def updatePin(self, pin):
        self.pin = pin
        self.rpc.update(details=f'Flooding Kahoot: {pin}',
        large_image="kahooticon",
        state="Flooding Kahoots with Bots",
        large_text="Spams Kahoots with bot users",
        buttons=[{"label":"Download Kahoot Smasher", "url":"https://github.com/botmeep/kahootSmash/"}],
        instance=True)
    def updateBotCount(self, botCount):
        self.rpc.update(details=f'Flooding Kahoot: {self.pin}',
        large_image="kahooticon",
        state=f'Flooding Kahoots with {botCount} Bots',
        large_text="Spams Kahoots with bot users",
        buttons=[{"label":"Download Kahoot Smasher", "url":"https://github.com/botmeep/kahootSmash/"}],
        instance=True)
    def clear(self):
        self.rpc.update(state="Currently Idle",
        large_image="kahooticon",
        details="Flooding Kahoots with Bots",
        large_text="Spams Kahoots with bot users",
        buttons=[{"label":"Download Kahoot Smasher", "url":"https://github.com/botmeep/kahootSmash/"}])