from ftplib import FTP


class FTPCONFIG:
    def __init__(self) -> None:
        self.host = "192.168.50.149"
        self.user = input("[+] Enter User:> ")
        self.password = input("[+] Enter Password:> ")
        self.remote_directory = "/Files"

    def display(self):
        print(f"[+] User:{self.user} Password:{self.password} Host:{self.host} ")


def download_all_files(ftp, remote_directory):
    try:
        files = ftp.nlst(remote_directory)
        for filename in files:
            print(filename)
    except Exception as ex:
        print(f"[-] Something went wrong {str(ex)}")


def list_all_files(ftp, remote_directory):
    try:
        files = ftp.nlst(remote_directory)
        print("[+] List of files in the remote directory:")
        for filename in files:
            print(filename)
    except Exception as ex:
        print(f"[-] Something went wrong: {str(ex)}")


def main():
    try:
        ftpconfig = FTPCONFIG()
        try:
            print("[+] LOGGING INTO THE FTPserver")
            with FTP(ftpconfig.host) as ftp:
                ftp.login(user=ftpconfig.user, passwd=ftpconfig.password)
                print(f"[+] FTP LOGIN TEST : {ftp.getwelcome()}")
                download_all_files(ftp, ftpconfig.remote_directory)
                """ open file stream """
                with open("test.txt", "wb") as fd:
                    # Add a space after "RETR"
                    ftp.retrbinary("RETR " + "winfile.txt", fd.write, 1024)
                ftp.quit()
        except Exception as ex:
            print(f"[-] Something went wrong {str(ex)}")
    except KeyboardInterrupt:
        print("\n[-] OPERATION CANCELLED ")


if __name__ == "__main__":
    main()
