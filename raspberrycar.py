import obd

class Command:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


class Connection:
    def __init__(self, source = None):
        self._source = source
        self._connection = obd.OBD(self._source, fast=False)
        if not self._connection.is_connected():
            raise Exception('Unable to connect to OBD')

    def call(self, command):
        c = obd.commands[command.name()]
        return self._connection.query(c).value


def get_supported_commands(mode):
    """TO see all the commands execute pprint(dir(obd.commands))"""
    if mode == "basic":
        return ['ENGINE_LOAD',
                'FUEL_LEVEL',
                'RPM',
                'SPEED']
    elif mode == "adv":
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

    return ['ABSOLUTE_LOAD',
            'ACCELERATOR_POS_D',
            'ACCELERATOR_POS_E',
            'ACCELERATOR_POS_F',
            'AIR_STATUS',
            'AMBIANT_AIR_TEMP',
            'AUX_INPUT_STATUS',
            'BAROMETRIC_PRESSURE',
            'CATALYST_TEMP_B1S1',
            'CATALYST_TEMP_B1S2',
            'CATALYST_TEMP_B2S1',
            'CATALYST_TEMP_B2S2',
            'COOLANT_TEMP',
            'DISTANCE_W_MIL',
            'EGR_ERROR',
            'ELM_VERSION',
            'ELM_VOLTAGE',
            'EMISSION_REQ',
            'ENGINE_LOAD',
            'ETHANOL_PERCENT',
            'EVAP_VAPOR_PRESSURE',
            'EVAP_VAPOR_PRESSURE_ABS',
            'EVAP_VAPOR_PRESSURE_ALT',
            'FUEL_LEVEL',
            'FUEL_PRESSURE',
            'FUEL_RAIL_PRESSURE_ABS',
            'FUEL_RAIL_PRESSURE_DIRECT',
            'FUEL_RAIL_PRESSURE_VAC',
            'FUEL_RATE',
            'FUEL_STATUS',
            'FUEL_TYPE',
            'INTAKE_PRESSURE',
            'INTAKE_TEMP',
            'LONG_FUEL_TRIM_1',
            'LONG_FUEL_TRIM_2',
            'LONG_O2_TRIM_B1',
            'LONG_O2_TRIM_B2',
            'MAF',
            'MAX_MAF',
            'MAX_VALUES',
            'OBD_COMPLIANCE',
            'OIL_TEMP',
            'PIDS_A',
            'PIDS_B',
            'PIDS_C',
            'RELATIVE_ACCEL_POS',
            'RELATIVE_THROTTLE_POS',
            'RPM',
            'RUN_TIME',
            'RUN_TIME_MIL',
            'SHORT_FUEL_TRIM_1',
            'SHORT_FUEL_TRIM_2',
            'SHORT_O2_TRIM_B1',
            'SHORT_O2_TRIM_B2',
            'SPEED',
            'STATUS',
            'STATUS_DRIVE_CYCLE',
            'THROTTLE_ACTUATOR',
            'THROTTLE_POS',
            'THROTTLE_POS_B',
            'THROTTLE_POS_C']
