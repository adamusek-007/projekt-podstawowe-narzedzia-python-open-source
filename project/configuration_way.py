class OperatingWay:

    def __init__(self):
        self.choice = None
        self.user_choice = None

    def get_operating_way_from_user(self):
        """Gets configuration method from user"""
        while self.user_choice not in ("1", "2"):
            self.user_choice = input(
                "Wybierz, jak chciałbyś obsługiwać aplikację:\n"
                "1: Konsola\n"
                "2: Przeglądarka\n"
                "Twój wybór: "
            ).strip()
            if self.user_choice == "1":
                self.choice = "console"
            if self.user_choice == "2":
                self.choice = "web"
            if self.user_choice not in ("1", "2"):
                print("Proszę wybrać jedną z dostępnych opcji: 1 lub 2.")
