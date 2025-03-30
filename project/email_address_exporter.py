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
