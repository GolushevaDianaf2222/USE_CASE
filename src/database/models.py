from typing import Optional
from pydantic import BaseModel

class BaseModelModify(BaseModel):
    id: Optional[int]

class Users(BaseModelModify):
    login: str
    password: str
    power_level: Optional[int]

class clint(BaseModelModify):
    name: Optional[str]

class contract(BaseModelModify):
    date: Optional[int]
    contract_number: Optional[str]
    Project_name: Optional[str]
    id_client: Optional[int]
    id_company: Optional[int]

class object(BaseModelModify):
    address: Optional[str]
    id_client: Optional[str]

class Company(BaseModelModify):
    name: Optional[str]
    id_contract: Optional[int]
    id_working_hours: Optional[int]
    id_provider: Optional[int]

class working_hours(BaseModelModify):
    getting_started: Optional[str]
    end_of_work: Optional[str]
    id_company: Optional[int]

class warehouse(BaseModelModify):
    address: Optional[str]
    delivery_date: Optional[str]
    list_of_materials: Optional[str]
    id_company: Optional[int]
    id_provider: Optional[int]

class provider(BaseModelModify):
     name: Optional[str]

class worker(BaseModelModify):
    name: Optional[str]
    type_of_worker: Optional[str]
    id_company: Optional[int]
    id_working_hours: Optional[int]

 class product(BaseModelModify):
     name: Optional[str]
     price_product: Optional[str]
     delivery_date: Optional[str]
     id_provider: Optional[int]

class departments(BaseModelModify):
    departments_name: Optional[str]
    id_warehouse: Optional[str]

class positions(BaseModelModify):
    title_of_the_position: Optional[str]
    id_provider: Optional[int]
    id_workers: Optional[int]
