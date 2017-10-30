import raspberrycar
import obd
from datetime import datetime
from time import sleep
import sys, getopt


def get_options(argv):
    options = {"verbose": False,
               "mode": "basic"}
    try:
        opts, args = getopt.getopt(argv, "hvm:", ["help", "verbose", "mode="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-v", "--verbose"):
            options['verbose'] = True
        elif opt in ("-m", "--mode"):
            if arg not in ['basic', 'adv', 'all']:
                print_help()
                sys.exit(2)
            options['mode'] = arg

    return options


def print_help():
    print('listener.py -v --mode <mode>')
    print('Options:')
    print('-h           This Help')
    print('-v           Verbose')
    print('-m --mode	Mode of commands: basic|adv|all')


def add_entry(entry):
    """Just printing for now. Maybe file in the future"""
    print(";".join(str(i) for i in entry))


if __name__ == "__main__":
    options = get_options(sys.argv[1:])
    if options['verbose']:
        obd.logger.setLevel(obd.logging.DEBUG)

    connection = raspberrycar.Connection()
    commands = raspberrycar.get_supported_commands(options['mode'])
    add_entry(commands)

    while True:
        entry = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        for name in commands:
            command = raspberrycar.Command(name)
            entry.append(connection.call(command))
        add_entry(entry)
        sleep(1)
