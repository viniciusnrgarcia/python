# Herança
# Abstração
from pathlib import Path


LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:

    # protected method
    def _log(self, log):
        raise NotImplementedError('Implemente o método log')

    # método concretos herdado
    def log_error(self, log):
        return self._log(f'Error: {log}')

    def log_success(self, log):
        return self._log(f'Success: {log}')


# https://www.pythontutorial.net/python-oop/python-mixin/
# A mixin is a class that provides method implementations for reuse by multiple related child classes. However, the inheritance is not implying an is-a relationship.
# A mixin doesn’t define a new type. Therefore, it is not intended for direction instantiation.

class LogFileMixin(Log):
    def _log(self, log):
        print(f'LOG: {log} ({self.__class__.__name__})')
        with open(LOG_FILE, 'a') as log_file:
            log_file.write(log)
            log_file.write('\n')



class LogPrintMixin(Log):
    def _log(self, log):
        print(f'{log} ({self.__class__.__name__})')


class LogMessageMixin(Log):
    ...


if __name__ == '__main__':
    l = LogFileMixin()
    l.log('Iniciando log')
