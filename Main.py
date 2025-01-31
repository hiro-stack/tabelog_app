from presentation.presentation import Presentation
from apprication.app import Application


class Main:
    def __init__(self):

        self.current_location = {
            "name": "現在地",
            "latitude": 35.64338,
            "longitude": 139.66952,
        }

        self.areas = [
            "三軒茶屋",
            "西太子堂",
        ]

        self.presentation = Presentation()

        self.app = None

    def main(self):
        self.presentation.main()
        self.app = Application(
            self.current_location,
            self.areas,
            self.presentation.menus,
            self.presentation.max_minutes,
            self.presentation.price_max,
            self.presentation.time_is,
            self.presentation.weight,
            self.presentation.votes_result,
            self.presentation.alpha,
        )
        self.app.main()


if __name__ == "__main__":
    main = Main()
    main.main()
