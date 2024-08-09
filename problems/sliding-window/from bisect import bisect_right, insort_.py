from bisect import bisect_right, insort_right


class LogServer:
    def __init__(self, max_logs):
        self.logs = []          # logs[i] = [(timestamp, orderInsertion), logID]
        self.m = max_logs
        self.order = 0
        # Constructor
        pass

    def recordLog(self, logId, timestamp):
        curOrder = self.order
        self.order += 1

        ## binary insort the timestamp, and order_insertion
        insort_right(self.logs, [(timestamp, curOrder), logId], key =  lambda x: (x[0][0], x[0][1]))
        
        ## evict oldest one

        pass

    def getLogs(self):
        pass

    def getLogCount(self):
        pass
    