import requests
from typing import List, Literal

class Mosyle:
    def __init__(self, email: str, password: str, access_token: str) -> None:
        self.__s = requests.Session()
        self.__access_token = access_token
        
        bearer_token = self.get_bearer_token(email, password)
                
        self.__s.headers.update({'Content-Type': 'application/json',
                          'Authorization': f'Bearer {bearer_token}'})
        


    # -- Methods for retrieving data --
    # Gets bearer token from https://managerapi.mosyle.com/v2/login
    def get_bearer_token(self, email: str, password: str) -> str:
        data = {
            'accessToken': self.__access_token,
            'email': email,
            'password': password
        }
        resp = self.__s.post('https://managerapi.mosyle.com/v2/login', data)
        return resp.headers['Authorization'].split(' ')[-1]
        
    # Returns devices from https://managerapi.mosyle.com/v2/listdevices
    def list_devices(self, os: Literal['ios', 'mac', 'tvos'], tags: List[str] = [], osversions: List[str] = [], serial_numbers: List[str] = [], page: int = 0, specific_columns: List[str] = []) -> dict:
        data = {
            'accessToken': self.__access_token,
            'options': {
                'os': os,
                **{key: value for key, value in {
                    'tags': tags,
                    'osversions': osversions,
                    'serial_numbers': serial_numbers,
                    'page': page,
                    'specific_columns': specific_columns
                }.items() if value}
            }
        }
                
        resp = self.__s.post('https://managerapi.mosyle.com/v2/listdevices', json=data)
        
        return resp.json()
    
    # Returns users from https://managerapi.mosyle.com/v2/listusers
    def list_users(self, page: int = 0, specific_columns: List[str] = [], types: List[str] = []) -> dict:
        data = {
            'accessToken': self.__access_token,
            'options': {
                **{key: value for key, value in {
                    'page': page,
                    'specific_columns': specific_columns,
                    'types': types
                }.items() if value}
            }
        }
                
        resp = self.__s.post('https://managerapi.mosyle.com/v2/listusers', json=data)
        
        return resp.json()

    # Returns groups from https://managerapi.mosyle.com/v2/devicegroups
    def list_device_groups(self, os: Literal['ios', 'mac', 'tvos'], page: int = 0) -> dict:
        data = {
            'accessToken': self.__access_token,
            'options': {
                'os': os,
                'page': page
            }
        }
                
        resp = self.__s.post('https://managerapi.mosyle.com/v2/devicegroups', json=data)
        
        return resp.json()

    # Returns devices in a group from https://managerapi.mosyle.com/v2/listdevicesbygroup
    def list_devices_by_group(self, iddevicegroup: str) -> dict:
        data = {
            'accessToken': self.__access_token,
            'options': {
                'iddevicegroup': iddevicegroup
            }
        }
                
        resp = self.__s.post('https://managerapi.mosyle.com/v2/listdevicesbygroup', json=data)
        
        return resp.json()

    # Returns all accounts form https://managerapi.mosyle.com/v2/accounts
    def list_accounts(self) -> dict:
        data = {
            'accessToken': self.__access_token,
        }
                
        resp = self.__s.post('https://managerapi.mosyle.com/v2/accounts', json=data)
        
        return resp.json()

    # -- Methods for updating data --
    # Updates a device using https://managerapi.mosyle.com/v2/devices
    def update_device(self, serial_number: str, asset_tag: str = None, tags: str = None, name: str = None, lock: str = None) -> dict:
        data = {
            'accessToken': self.__access_token,
            'elements': {
                'serialnumber': serial_number,
                **{key: value for key, value in {
                    'asset_tag': asset_tag,
                    'tags': tags,
                    'name': name,
                    'lock': lock
                }.items() if value}
            }
        }
                
        resp = self.__s.post('https://managerapi.mosyle.com/v2/devices', json=data)
        
        return resp.json()
    
    # Bulk commands will be implemented later
    
    