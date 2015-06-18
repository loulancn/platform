from syncloud.app import logger


class Reader:

    def __init__(self, proc_cpuinfo='/proc/cpuinfo'):
        self.proc_cpuinfo = proc_cpuinfo
        self.logger = logger.get_logger('Reader')
        
    def read(self):
        self.logger.info('reading {}'.format(self.proc_cpuinfo))
        with open(self.proc_cpuinfo, 'r') as f:
            contents = f.read()
            # self.logger.debug('contents: {}'.format(contents))
            return contents