class ConfigurationWay:

    def __init__(self):
        self.choice = None

    def get_configuration_method(self):
        """Gets configuration method from user"""
        while self.choice not in ("1", "2"):
            self.choice = input(
                "Wybierz, jak chciałbyś obsługiwać aplikację:\n"
                "1: Konsola\n"
                "2: Przeglądarka\n"
                "Twój wybór: "
            ).strip()
            if self.choice not in ("1", "2"):
                print("Proszę wybrać jedną z dostępnych opcji: 1 lub 2.")
