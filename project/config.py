class Config:
    """Class containing configuration of the connection to the server"""

    def __init__(
        self,
        imap_server_address,
        imap_email_username,
        imap_email_password,
        imap_port,
        output_csv_filename,
    ):
        self.imap_server_address = imap_server_address
        self.imap_email_username = imap_email_username
        self.imap_email_password = imap_email_password
        self.imap_port = imap_port
        self.output_csv_filename = output_csv_filename
