class SavedState:
    """Represents the original state of a row before it was edited"""

    def __init__(self, oid, data=None):
        self.oid = oid
        self.data = data

    def get_oid(self):
        return self.oid

    def get_data(self):
        return self.data

    def __eq__(self, other):
        if isinstance(other, SavedState):
            print(self.oid)
            print(other.oid)
            return self.oid == other.oid
        return False

    def __str__(self):
        return f"oid: ${self.oid}, data: ${self.data}"

    def __repr__(self):
        return f"oid: ${self.oid}, data: ${self.data}"

    def __hash__(self):
        return hash(self.oid)
