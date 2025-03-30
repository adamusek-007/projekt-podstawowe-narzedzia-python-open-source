"""This is the main class of this programm"""

from flask import Flask
from flask import render_template_string
from flask import render_template
from flask import request
import threading
from project.console_configurator import ConsoleConfigurator

# Choose from user that either he want to supply programm by console or by the web


class EmailAddressExporter:
    """This class is exporting email addresses from the mailbox"""

    def __init__(
        self,
        imap_server_address="",
        imap_email_username="",
        imap_email_password="",
        imap_port=993,
        output_csv_filename="",
    ):
        self.imap_server_address = imap_server_address
        self.imap_email_username = imap_email_username
        self.imap_email_password = imap_email_password
        self.imap_port = imap_port
        self.output_csv_filename = output_csv_filename

    def display_config(self):
        """Displays the collected configuration."""
        print("\nConfiguration:")
        print(f"IMAP Server Address: {self.imap_server_address}")
        print(f"Email Username: {self.imap_email_username}")
        print(f"IMAP Port: {self.imap_port}")
        print(f"Output CSV Filename: {self.output_csv_filename}")


app = Flask(__name__)
exporter = EmailAddressExporter()


@app.route("/", methods=["GET", "POST"])
def configure():
    global exporter
    if request.method == "POST":
        exporter = EmailAddressExporter(
            request.form["imap_server_address"],
            request.form["imap_email_username"],
            request.form["imap_email_password"],
            int(request.form["imap_port"]),
            request.form["output_csv_filename"],
        )
        return "Configuration saved! You can close this page."
    return render_template("configuration-site.html")
    # return render_template_string()


def run_flask():
    app.run(host="0.0.0.0", port=5000, debug=False)


if __name__ == "__main__":
    choice = (
        input(
            "Wybierz jak chciałbyś obsługiwać aplikację: \n konsola (1) \n przegladarka (2)"
        )
        .strip()
        .lower()
    )
    if choice == "1":
        configurator = ConsoleConfigurator()
        config = configurator.create_config()
    elif choice == "2":
        print("Starting web interface on http://localhost:5000...")
        threading.Thread(target=run_flask, daemon=True).start()
        input("Press Enter to stop the web server...")
    else:
        print("Proszę wybierz z dostępnych opcji. (1 lub 2)")
