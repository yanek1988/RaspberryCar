import obd

class Command:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


class Connection:
    def __init__(self, source = None):
        self._source = source
        self._connection = obd.OBD(self._source)

    def call(self, command):
        c = obd.commands[command.name()]
        print(self._connection.query(c).value)


def get_supported_commands():
    """
    TO see all the commands execute pprint(dir(obd.commands))
    """
    return ['ABSOLUTE_LOAD',
            'AIR_STATUS',
            'DISTANCE_W_MIL',
            'ENGINE_LOAD',
            'FUEL_LEVEL',
            'FUEL_PRESSURE',
            'FUEL_RATE',
            'FUEL_STATUS',
            'LONG_FUEL_TRIM_1',
            'LONG_FUEL_TRIM_2',
            'LONG_O2_TRIM_B1',
            'LONG_O2_TRIM_B2',
            'OIL_TEMP',
            'RPM',
            'SHORT_FUEL_TRIM_1',
            'SHORT_FUEL_TRIM_2',
            'SPEED']


if __name__ == "__main__":
    connection = Connection()
    for name in get_supported_commands():
        command = Command(name)
        connection.call(command)
