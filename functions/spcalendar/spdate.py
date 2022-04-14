class SPDate:

    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
        # TODO: Implement isoweekday logic
        self.isoweekday = None

    def __str__(self) -> str:
        return f"{self.day}-{self.month}-{self.year}"

    def __del__(self):
        pass
