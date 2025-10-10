__version__='1.1.4'
__author__=['Ioannis Tsakmakis']
__date_created__='2024-09-28'
__last_updated__='2025-09-09'

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

class AggregationFunction(str, Enum):
    daily_mean = 'daily_mean'
    daily_max = 'daily_max'
    daily_min = 'daily_min'
    daily_median = 'daily_median'
    daily_sum = 'daily_sum'
    hourly_mean = 'hourly_mean'
    hourly_max = 'hourly_max'
    hourly_min = 'hourly_min'
    hourly_median = 'hourly_median'
    hourly_sum = 'hourly_sum'

class TemporalResolution(str, Enum):
    annual = '1 Year'
    monthly = '1 Month'
    daily = '1 Day'
    hourly = '1 Hour'
    half_hour = '30 Minutes'
    quarter_hour = '15 Minutes'

class ConfirmationStatus(str, Enum):
    confirmed = 'confirmed'
    unconfirmed = 'unconfirmed'

class CretePrefectures(str, Enum):
    chania = 'Chania'
    heraklion = 'Heraklion'
    rethymnon = 'Rethymnon'
    lasithi = 'Lasithi'

class BeachTypes(str, Enum):
    open = 'open'
    breakwater = 'breakwater'

class DWDIconVars (str, Enum):
    air_temp = "temperature_2m"
    rh = "relative_humidity_2m"
    precipitation = "precipitation"
    weather_code = "weather_code"
    ws = "wind_speed_10m"
    wd = "wind_direction_10m"
    wind_gust = "wind_gusts_10m"

class MeasurementCategory(str, Enum):
    sensor='sensor'
    meter='meter'
    calculated='calculated'

class SurfaceType(str, Enum):
    grass='grass'
    bare_soil='bare_soil'
    concrete='concrete'
    asphalt='asphalt'
    crop='crop'
    water='water'
    other='other'

class StationType(str, Enum):
    agro_meteorological='agro_meteorological'
    atmospheric_quality='atmospheric_quality'
    coastal='coastal'
    inland_water='inland_water'
    soil='soil'