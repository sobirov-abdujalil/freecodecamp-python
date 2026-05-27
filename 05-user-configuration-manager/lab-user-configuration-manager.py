# Certification Project: Build a User Configuration Manager
class UserConfig:
    def __init__(self, username):
        self.username = username
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def delete(self, key):
        return self.settings.pop(key, None)

    def export_config(self):
        return {"username": self.username, "settings": self.settings}
