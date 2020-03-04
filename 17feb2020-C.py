import threading

#IS-A RELATIONAHSIP ----> PRINTINGTASK IS-A THREAD

class PrintingTask(threading.Thread):
    def run(self):
        for i in range(1,11):
            print(">>Printing {} Copy #{}".format("LearningPython.PDF",i))


def main():

    print("APP STARTED--->")
    task = PrintingTask
    news