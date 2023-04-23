from log import LogPrintMixin, LogFileMixin, LogMessageMixin
from log_abstract import AbstractLog, AbstractLogFileMixin

#l = LogPrintMixin()
#l.log_error('Exception from PRINT mixin')

l = LogFileMixin()
#l.log('Test')
l.log_error('Exception from FILE mixin')
l.log_success('OK')


###### Error exemple #####
# l = LogMessageMixin()
#l.log('Test')
# l.log_error('Exception from FILE mixin')

a = AbstractLogFileMixin()
