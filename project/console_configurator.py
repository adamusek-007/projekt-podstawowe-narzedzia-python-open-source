"""Konfigurator parametrów połączenia z wykorzystaniem konsoli oraz zawierający funkcję Config z wprowadzonymi danymi."""

from config import Config


class ConsoleConfigurator:
    """Konfigurator parametrów połączenia z konsoli"""

    def __init__(self):
        self.imap_server_address = input("Wprowadź adres serwera IMAP: ")
        self.imap_email_username = input("Wprowadź nazwę logowania do serwera: ")
        self.imap_email_password = input("Wprowadź hasło: ")
        self.imap_port = int(input("Wprowadź port serwera (domyślny 993): ") or 993)
        self.output_csv_filename = input("Wprowadź nazwę pliku wyjściowego CSV: ")

    def create_config(self):
        """Funkcja tworząca klasę Config z wprowadzonymi danymi"""
        return Config(
            self.imap_server_address,
            self.imap_email_username,
            self.imap_email_password,
            self.imap_port,
            self.output_csv_filename,
        )
