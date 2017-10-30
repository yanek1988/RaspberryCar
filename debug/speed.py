import obd

print("This script should return current speed")

obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD()
cmd = obd.commands.SPEED
response = connection.query(cmd)

print(response.value) # returns unit-bearing values thanks to Pint
if response.value != None:
    print(response.value.to("mph")) # user-friendly unit conversions
