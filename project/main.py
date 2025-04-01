"""This is the main class of this programm"""

import threading

from flask import Flask
from flask import render_template
from flask import request
from console_configurator import ConsoleConfigurator
from configuration_way import OperatingWay
from email_address_exporter import EmailAddressExporter
from config import Config

web_gui = Flask(__name__)


@web_gui.route("/", methods=["GET", "POST"])
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
        return "Konfiguracja zapisana! Możesz zamknąć tę stronę."
        exporter_thread = Thread(target=run_email_exporter, args=(config,))
        exporter_thread.start()
    return render_template("configuration-site.html")


def run_flask():
    """Runs flask configurator"""
    web_gui.run(host="0.0.0.0", port=5000, debug=False)


def run_email_exporter(config):
    exporter = EmailAddressExporter(config)


if __name__ == "__main__":
    operating_way = OperatingWay()
    operating_way.get_operating_way_from_user()
    if operating_way.choice == "1":
        console_configurator = ConsoleConfigurator()
        config = console_configurator.create_config()
        ConsoleEmailAddressExporter(config)
    elif operating_way.choice == "2":
        print("Starting web interface on http://localhost:5000...")
        threading.Thread(target=run_flask, daemon=True).start()
        input("Press Enter to stop the web server...")
