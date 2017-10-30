import obd
from datetime import datetime
from time import sleep

class Command:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


class Connection:
    def __init__(self, source = None):
        self._source = source
        self._connection = obd.OBD(self._source, fast=False)
        if self._connection.is_connected() != True:
            raise Exception('Unable to connect to OBD')

    def call(self, command):
        c = obd.commands[command.name()]
        print(command.name(), self._connection.query(c).value)


def get_supported_commands():
    """
    TO see all the commands execute pprint(dir(obd.commands))
    """
    return ['ENGINE_LOAD',
            'FUEL_LEVEL',
            'RPM',
            'SPEED']


if __name__ == "__main__":
    obd.logger.setLevel(obd.logging.DEBUG)
    connection = Connection()
    while True:
        for name in get_supported_commands():
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            command = Command(name)
            connection.call(command)
        sleep(1)
