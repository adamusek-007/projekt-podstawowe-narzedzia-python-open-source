"""This is the main class of this programm"""

from flask import Flask
from flask import render_template_string
from flask import render_template
from flask import request
import threading
from console_configurator import ConsoleConfigurator
from configuration_way import ConfigurationWay
from email_address_exporter import EmailAddressExporter

# Choose from user that either he want to supply programm by console or by the web

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
    config_way = ConfigurationWay()
    config_way.get_configuration_method()
    if config_way.choice == "1":
        console_configurator = ConsoleConfigurator()
        config = console_configurator.create_config()
    elif config_way.choice == "2":
        print("Starting web interface on http://localhost:5000...")
        threading.Thread(target=run_flask, daemon=True).start()
        input("Press Enter to stop the web server...")
