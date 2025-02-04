__version__='1.0.1'
__author__=['Ioannis Tsakmakis']
__date_created__='2024-09-28'
__last_updated__='2024-10-07'

from enum import Enum

class AccountType(str, Enum):
    commercial = 'commercial'
    academic = 'academic'
    beta = 'beta'
    alpha = 'alpha'

class Status(str, Enum):
    online = 'online'
    offline = 'offline'

class DeviceType(str, Enum):
    sensor = 'sensor'
    meter = 'meter'
    calculated = 'calculated'

class ApplicationType(str, Enum):
    irrigation = 'irrigation'
    fertigation = 'fertigation'
    fertilization = 'fertilization'

class AdviceStatus(str, Enum):
    completed = 'completed'
    in_process = 'in process'
    canceled = 'canceled'

class IconType(str, Enum):
    meteo = 'meteo'
    coastal = 'coastal'
    inland = 'inland'
    soil = 'soil'

