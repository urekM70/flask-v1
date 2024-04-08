class User:
    def __init__(self, id, authenticated=True, active=True, anonymous=False):
        self.id = str(id)
        self.authenticated = authenticated
        self.active = active
        self.anonymous = anonymous