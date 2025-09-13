
import uuid


class Role:
    id: str
    name: str
    user_id: str

    def __init__(self, name: str, user_id: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.user_id = user_id