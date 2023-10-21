from ftplib import FTP


class FTPCONFIG:
    def __init__(self) -> None:
        self.host = input("[+] Enter Host:> ")
        self.user = input("[+] Enter User:> ")
        self.password = input("[+] Enter Password:> ")
        self.remote_directory = "/Files"

    def display(self):
        print(f"[+] User:{self.user} Password:{self.password} Host:{self.host} ")


def download_all_files(ftp, remote_directory):
    try:
        files = ftp.nlst(remote_directory)
        for filename in files:
            with open(filename, "wb") as fd:
                ftp.retrbinary("RETR " + filename, fd.write, 1024)
            print(f"[+] Downloaded: {filename}")
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


def download_single_file(ftp, path):
    try:
        filename = path.split("/")[-1]
        with open(filename, "wb") as fd:
            ftp.retrbinary("RETR " + path, fd.write, 1024)
        print(f"[+] Downloaded: {filename}")
    except Exception as ex:
        print(f"[-] Something went wrong: {str(ex)}")


def change_directory(ftp, path):
    try:
        ftp.cwd(path)
        print(f"[+] Changed to directory: {path}")
    except Exception as ex:
        print(f"[-] Something went wrong: {str(ex)}")


def get_current_directory(ftp):
    try:
        current_directory = ftp.pwd()
        print(f"[+] Current working directory: {current_directory}")
    except Exception as ex:
        print(f"[-] Something went wrong: {str(ex)}")


def upload_file(ftp, remote_directory, local_filepath):
    try:
        with open(local_filepath, "rb") as fd:
            filename = local_filepath.split("\\")[-1]
            remote_path = remote_directory + "/" + filename
            ftp.storbinary("STOR " + remote_path, fd, 1024)
        print(f"[+] Uploaded: {filename} to {remote_directory}")
    except Exception as ex:
        print(f"[-] Something went wrong: {str(ex)}")


def delete_file(ftp, path):
    try:
        ftp.delete(path)
        print(f"[+] Deleted: {path}")
    except Exception as ex:
        print(f"[-] Something went wrong: {str(ex)}")


def main():
    try:
        ftpconfig = FTPCONFIG()
        try:
            print("[+] LOGGING INTO THE FTPserver")
            with FTP(
                ftpconfig.host
            ) as ftp:  # ftp -> is our handle to ftp server for understanding i.e with this ftp we can have control over our ftp
                ftp.login(user=ftpconfig.user, passwd=ftpconfig.password)
                print(f"[+] FTP LOGIN TEST : {ftp.getwelcome()}")
                """ open file stream """
                # download_single_file(ftp, "/", "winfile.txt")
                while True:
                    command = input(f"[+] ftp{ftpconfig.host}:> ")
                    if command.strip() == "quit":
                        print("[+] SESSION CLOSED ")
                        break
                    if command[0:2] == "ls":
                        path = command[3:]
                        list_all_files(ftp, path)
                        continue
                    if command[0:8] == "download":
                        path = command[9:]
                        download_single_file(ftp, path)
                        continue
                    if command.strip().lower() == "pwd":
                        get_current_directory(ftp)
                        continue
                    if command[0:2] == "cd":
                        path = command[3:]
                        change_directory(ftp, path)
                        continue
                    if command[0:6] == "upload":
                        cmd = command[7:].split(" ")
                        filepath = cmd[0]
                        remotepath = cmd[1]
                        upload_file(ftp, remotepath, filepath)
                        continue
                    if command[0:6] == "delete":
                        path = command[7:]
                        delete_file(ftp, path)
                        continue
                ftp.quit()
        except Exception as ex:
            print(f"[-] Something went wrong {str(ex)}")
    except KeyboardInterrupt:
        print("\n[-] OPERATION CANCELLED ")


if __name__ == "__main__":
    main()
