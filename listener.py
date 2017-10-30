import raspberrycar
import obd
from datetime import datetime
from time import sleep

if __name__ == "__main__":
    obd.logger.setLevel(obd.logging.DEBUG)
    connection = raspberrycar.Connection()
    commands = raspberrycar.get_supported_commands()
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for name in commands:
            command = raspberrycar.Command(name)
            connection.call(command)
        sleep(1)
