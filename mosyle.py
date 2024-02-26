import requests
from typing import List, Literal

class Mosyle:
    def __init__():
        # fill this in later
        return
    
    # -- Methods for retrieving data --
    # Returns devices from https://managerapi.mosyle.com/v2/listdevices
    def list_devices(os: str, tags: List[str] = [], osversions: List[str] = [], serial_numbers: List[str] = [], page: int = 0, specific_columns: List[str] = []) -> dict:
        return
    
    # Returns users from https://managerapi.mosyle.com/v2/listusers
    def list_users(page: int = 0, specific_columns: List[str] = [], types: List[str] = []) -> dict:
        return

    # Returns groups from https://managerapi.mosyle.com/v2/devicegroups
    def list_groups(os: Literal['ios', 'mac', 'tvos'], page: int = 0):
        return

    # Returns devices in a group from https://managerapi.mosyle.com/v2/listdevicesbygroup
    def list_group_devices(iddevicegroup: str) -> dict:
        return

    # Returns all accounts form https://managerapi.mosyle.com/v2/accounts
    def list_accounts() -> dict:
        return

    # -- Methods for updating data --
    # Updates a device using https://managerapi.mosyle.com/v2/devices
    def update_device(serial_number, asset_tag: str = None, tags: str = None, name: str = None, lock: str = None):
        return
    
    # Bulk commands will be implemented later


