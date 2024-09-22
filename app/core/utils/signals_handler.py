import signal

def handler(signum, frame):
    print ("\nCTRL+C Exiting... \nCiao ciao :)")
    exit(0)


def signal_handler():
    signal.signal(signal.SIGINT, handler)