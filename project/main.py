"""This is the main class of this programm"""

from flask import Flask
from flask import render_template_string
from flask import render_template
from flask import request
import threading
from console_configurator import ConsoleConfigurator
from configuration_way import ConfigurationWay
from email_address_exporter import EmailAddressExporter

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def configure():
    """Display configuration site, and on POST colletcts data"""
    if request.method == "POST":
        config = Config(
            imap_server_address=request.form["imap_server_address"],
            imap_email_username=request.form["imap_email_username"],
            imap_email_password=request.form["imap_email_password"],
            imap_port=int(request.form["imap_port"]),
            output_csv_filename=request.form["output_csv_filename"],
        )
        # Tutaj możesz dodać kod do przetwarzania obiektu config,
        # np. zapisać go do pliku lub użyć w dalszej części aplikacji.
        return "Konfiguracja zapisana! Możesz zamknąć tę stronę."
    return render_template("configuration-site.html")


def run_flask():
    """Runs flask configurator"""
    app.run(host="0.0.0.0", port=5000, debug=False)


if __name__ == "__main__":
    config_way = ConfigurationWay()
    config_way.get_configuration_method()
    if config_way.choice == "1":
        console_configurator = ConsoleConfigurator()
        config = console_configurator.create_config()
    elif config_way.choice == "2":
        print("Starting web interface on http://localhost:5000...")
        threading.Thread(target=run_flask, daemon=True).start()
        input("Press Enter to stop the web server...")
