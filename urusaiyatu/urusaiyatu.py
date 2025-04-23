import aiohttp
import json

baseurl = "http://oracle.node.shishen575.com:2000"
cache = {}

class Item():
    def __init__(self):
        pass

    async def fetch(self, itemid: str = None):
        try:
            cac = cache.get("Item", None)
            if not cac:
                async with aiohttp.ClientSession() as session:
                    if not itemid:
                        async with session.get(f"{baseurl}/item") as response:
                            return await response.json()
                    async with session.get(f"{baseurl}/item/{itemid}") as response:
                        return await response.json()
            else:
                return cac
        except:
            return None
        
class Recipe():
    def __init__(self):
        pass

    async def fetch(self, recipe: int = None, itemname: str = None):
        try:
            async with aiohttp.ClientSession() as session:
                if not recipe and not itemname:
                    async with session.get(f"{baseurl}/recipe") as response:
                        return await response.json()
                if not recipe:
                    async with session.get(f"{baseurl}/recipe/{itemname}?t=r") as response:
                        return await response.json()
                if not itemname:
                    async with session.get(f"{baseurl}/recipe/{recipe}") as response:
                        return await response.json()
                return None
        except:
            return None
        
class Gathering():
    def __init__(self):
        pass

    async def fetch(self, id: str = None):
        try:
            async with aiohttp.ClientSession() as session:
                if not id:
                    async with session.get(f"{baseurl}/gathering") as response:
                        return await response.json()
                else:
                    async with session.get(f"{baseurl}/gathering/{id}") as response:
                        return await response.json()
                return None
        except:
            return None
        
class Fish():
    def __init__(self):
        pass

    async def fetch(self, id: str = None):
        try:
            async with aiohttp.ClientSession() as session:
                if not id:
                    async with session.get(f"{baseurl}/place/fishing") as response:
                        return await response.json()
                else:
                    async with session.get(f"{baseurl}/place/fishing/{id}") as response:
                        return await response.json()
                return None
        except:
            return None
        
class User():
    def __init__(self):
        pass

    async def fetch(self, id: int = None):
        try:
            async with aiohttp.ClientSession() as session:
                if not id:
                    async with session.get(f"{baseurl}/user") as response:
                        return await response.json()
                else:
                    async with session.get(f"{baseurl}/user/{id}") as response:
                        return await response.json()
                return None
        except:
            return None
        
class Market():
    def __init__(self):
        pass

    async def fetch(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{baseurl}/market") as response:
                    return await response.json()
            return None
        except:
            return None
        
class LootTable():
    def __init__(self):
        pass

    async def fetch(self, id: str = None):
        try:
            async with aiohttp.ClientSession() as session:
                if not id:
                    async with session.get(f"{baseurl}/loot") as response:
                        return await response.json()
                else:
                    async with session.get(f"{baseurl}/loot/{id}") as response:
                        return await response.json()
            return None
        except:
            return None
        
class Cache():
    def __init__(self):
        pass

    async def save_item(self):
        try:
            cache["Item"] = await Item().fetch()
            return True
        except:
            return False
        
    async def save_recipe(self):
        try:
            cache["Recipe"] = await Recipe().fetch()
            return True
        except:
            return False
        
    def row(self):
        return cache