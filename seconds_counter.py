import time

secondi = 0


def count():
    global secondi
    while True:
        print(">>>>>>>>>>>>>>>>>>>>> {}".format(secondi))
        # Sleep for a minute
        time.sleep(1)
        # Increment the minute total
        secondi += 1
        # Bring up the dialog box here
        return secondi
