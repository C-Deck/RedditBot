from threading import Timer

#Class for repeating timer
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self.Timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.is_running = False
        self.kwargs = kwargs

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if self.is_running is False:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False