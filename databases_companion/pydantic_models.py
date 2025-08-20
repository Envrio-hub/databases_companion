__version__='0.1.0'
__author__=['Ioannis Tsakmakis']
__date_created__='2025-08-20'
__last_updated__='2025-08-20'

from pydantic import BaseModel

class BeachAmenities(BaseModel):
    sunbeds: bool = False
    showers: bool = False
    toilets: bool = False
    parking: bool = False
    accessibility: bool = False
    food: bool = False
    watersports: bool = False
    lifeguard: bool = False
    blue_flag: bool = False
    