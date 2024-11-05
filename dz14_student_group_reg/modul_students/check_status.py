class CheckCapacityError(Exception):
    """Checking capacity of  the group <`10"""
    def __init__(self, message="Group capacity are 10 students"):
        self.message = message
        super().__init__(self.message)