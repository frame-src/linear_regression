import signal

def handler(signum, frame):
    print ("\n Ciao ciao :)")
    exit(0)


signal.signal(signal.SIGINT, handler)