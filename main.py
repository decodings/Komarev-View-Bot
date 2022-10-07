import requests, threading, multiprocessing

class Main:
    def __init__(self):
        self.threads = int(input('Threads (visits/sec) (1 - %s): ' % (multiprocessing.cpu_count() * 100)))
        self.link = input('Link (Click the button on your profile and copy the link from URL): ') # Example: https://camo.githubusercontent.com/f86509497432920fb6b9c21924291553d0f2f7ce810a4d81413535315f0303e2/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d6465636f64696e677326636f6c6f723d303237376666267374796c653d666f722d7468652d6261646765266c6162656c3d566973697473
        self.counter = 0

    def visit(self):
        requests.get(self.link)
        self.counter += 1
        print('Visited: %s' % self.counter)

    def run(self):
        while True:
            tasks = [threading.Thread(target = self.visit) for _ in range(self.threads)]
            for task in tasks: task.start()
            for task in tasks: task.join()

if __name__ == '__main__':
    Main().run()
