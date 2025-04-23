# UrusaiYatu-Library
うるさいやつのライブラリです。非同期処理です。

インストール方法
```
pip install git+https://github.com/mochagod123/UrusaiYatu-Library.git
```

サンプルコード
```
from urusaiyatu import urusaiyatu as main
import asyncio

async def run():
    user = await main.User().fetch()
    print(user)
    item = await main.Item().fetch()
    print(item)
    recipe = await main.Recipe().fetch()
    print(recipe)
    Gathering = await main.Gathering().fetch()
    print(Gathering)
    Fish = await main.Fish().fetch()
    print(Fish)
    Market = await main.Market().fetch()
    print(Market)
    LootTable = await main.LootTable().fetch()
    print(LootTable)

async def cache_save():
    cac = main.Cache()
    cache_item = await cac.save_item()
    print(f"Item: {cache_item}")
    cache_recipe = await cac.save_recipe()
    print(f"Recipe: {cache_recipe}")
    row = cac.row()
    print(row)

# asyncio.run(run())
asyncio.run(cache_save())
```
