from microchat import client_tornado

def main():
    usrname = "XXXXXXXX"
    passwd = "xxxxxxxxxx"
    client_tornado.start(usrname, passwd)


if __name__ == '__main__':
    main()