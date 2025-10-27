__version__='0.1.3'
__author__=['Ioannis Tsakmakis']
__date_created__='2025-08-20'
__last_updated__='2025-09-09'

from pydantic import BaseModel, condecimal, validator
from decimal import Decimal
from typing import Annotated, List
from datetime import datetime
from databases_companion.enum_variables import BeachTypes, DWDIconVars

class BeachAmenities(BaseModel):
    sunbeds: bool = False
    showers: bool = False
    toilets: bool = False
    parking: bool = False
    accessibility: bool = False
    food: bool = False
    watersports: bool = False
    lifeguard: bool = False

class WaveDataArgs(BaseModel):
    beach_longitude: Annotated[Decimal, condecimal(max_digits=10, decimal_places=6)]
    beach_latitude: Annotated[Decimal, condecimal(max_digits=10, decimal_places=6)]
    start_date: datetime
    end_date: datetime
    process_waves: bool
    beach_type: BeachTypes
    depth: float
    slope: float

    @validator("start_date", "end_date", pre=True)
    def parse_dates(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Dates must be in format YYYY-MM-DD")
        return value 
    
class CurrentTempChlorophyllDataArgs(BaseModel):
    longitude: Annotated[Decimal, condecimal(max_digits=10, decimal_places=6)]
    latitude: Annotated[Decimal, condecimal(max_digits=10, decimal_places=6)]
    start_date: datetime
    end_date: datetime

    @validator("start_date", "end_date", pre=True)
    def parse_dates(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Dates must be in format YYYY-MM-DD")
        return value
    
class DWDIconDataArgs(BaseModel):
    latitude: Annotated[Decimal, condecimal(max_digits=10, decimal_places=6)]
    longitude: Annotated[Decimal, condecimal(max_digits=10, decimal_places=6)]
    start_date: datetime
    end_date: datetime
    variables: List[DWDIconVars]
    model: str = "icon_seamless"
    timezone: str = "auto"

    @validator("start_date", "end_date", pre=True)
    def parse_dates(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Dates must be in format YYYY-MM-DD")
        return value
