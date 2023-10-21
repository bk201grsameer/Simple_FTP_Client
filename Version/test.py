from ftplib import FTP


class FTPCONFIG:
    def __init__(self) -> None:
        self.host = "192.168.50.149"
        self.user = input("[+] Enter User:> ")
        self.password = input("[+] Enter Password:> ")
        self.remote_directory = "/"  # Replace with the actual remote directory

    def display(self):
        print(f"[+] User:{self.user} Password:{self.password} Host:{self.host} ")


def list_files_with_type(ftp, remote_directory):
    try:
        # Use the LIST command to get directory listing
        files = ftp.nlst(remote_directory)
        print("[+] List of files in the remote directory:")
        for filename in files:
            # Check if the entry is a file or directory using the LIST data
            entry_type = "File"
            if filename.endswith("/"):
                entry_type = "Directory"
            print(f"{filename} ({entry_type})")
    except Exception as ex:
        print(f"[-] Something went wrong: {str(ex)}")


def main():
    try:
        ftpconfig = FTPCONFIG()
        try:
            print("[+] LOGGING INTO THE FTP server")
            with FTP(ftpconfig.host) as ftp:
                ftp.login(user=ftpconfig.user, passwd=ftpconfig.password)
                print(f"[+] FTP LOGIN TEST: {ftp.getwelcome()}")
                list_files_with_type(ftp, ftpconfig.remote_directory)
                ftp.quit()
        except Exception as ex:
            print(f"[-] Something went wrong: {str(ex)}")
    except KeyboardInterrupt:
        print("\n[-] OPERATION CANCELLED ")


if __name__ == "__main__":
    main()
