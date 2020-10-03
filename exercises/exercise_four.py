from datetime import datetime


class Promo:
    def __init__(self, name: str, date: datetime):
        self.name = name
        self.date = date
        self.expired = self.calculate_is_expired()

    def calculate_is_expired(self):
        if datetime.today() < self.date:
            return True
        else:
            return False


if __name__ == '__main__':
    promo = Promo("jaider", datetime(2020, 12, 12))
    print(promo.expired)
