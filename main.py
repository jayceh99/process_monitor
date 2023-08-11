import psutil
import os
import re
class monitor:
    def __init__(self,process_name) -> None:
        self.process_name = process_name
    def find_pids(self):
        all_pids = psutil.pids()
        for pid in all_pids:
            try:
                if self.process_name in str(psutil.Process(pid).cmdline()):
                    self.process_pid = pid
                    self.process = psutil.Process(pid)
                    print(self.process)
            except:
                pass
    def memory_useage(self):
        mem = str (self.process.memory_full_info())
        #pattern = re.compile(r'(?<=uss=)\d+\.*')
        pattern = re.compile(r'(?<=uss=)\d+')
        print(mem)
        memory_use =  pattern.findall(mem)
        print(memory_use)
    def cpu_useage (self):
        self.cpu = self.process.cpu_percent(interval=int(1)) 
        print(self.cpu)

    def connections (self):   
        connection_tmp = str(self.process.connections())
        established = connection_tmp.count('ESTABLISHED')
        close_wait = connection_tmp.count('CLOSE_WAIT')
        print(established , close_wait)


def main():
    print(os.environ['NUMBER_OF_PROCESSORS'])
    monitor_q = monitor('Taskmgr')
    monitor_q.find_pids()
   # monitor_q.connections()
   # monitor_q.cpu_useage()
    monitor_q.memory_useage()

if __name__ == '__main__':
    main()