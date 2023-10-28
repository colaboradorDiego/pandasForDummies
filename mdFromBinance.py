import asyncio
import websockets
import time
import json
import pandas as pd


async def get_avg_price(price1, price2):
    bb = float(price1)
    ba = float(price2)
    if bb and ba:
        return (bb + ba)/2
    return 0


async def parse_binance(resp_dict):
    data = {}
    price1 = resp_dict.get('b')     # best bid price
    price2 = resp_dict.get('a')     # best ask price
    data['market'] = 'BINANCE'
    instrumen = resp_dict.get('s')
    data['instrument'] = '{}-{}'.format(instrumen[:3], instrumen[3:])
    data['avg_price'] = await get_avg_price(price1, price2)
    return data


async def print_result(resp_dict):
    parsed_data = await parse_binance(resp_dict)

    if type(parsed_data) is dict:
        print('{} "{}" {} avg_price: $ {}'.format(
            time.strftime('%H:%M:%S'),
            parsed_data.get('market'),
            parsed_data.get('instrument'),
            parsed_data.get('avg_price')))

    else:
        print(parsed_data)


# series
def mostrar(json_md):
    md = pd.read_json(json_md, typ='index')
    print(md.dtypes)


def mostrar1(json_md, data):
    # print("recibida:", json_md)
    md_dict = json.loads(json_md)
    md_list = list(md_dict.values())

    nuevo = pd.DataFrame([md_list], columns=['OrderBookID',
                                            'Symbol',
                                            'BestBidPrice',
                                            'BestBidQty',
                                            'BestAskPrice',
                                            'BestAskQty'])
    data = pd.concat([data, nuevo])
    print(data)
    return data


async def start_listening_to_binance(url):
    async with websockets.connect(url) as socket:
        data = pd.DataFrame([[0, 0, 0, 0, 0, 0]], columns=['OrderBookID',
                                                         'Symbol',
                                                         'BestBidPrice',
                                                         'BestBidQty',
                                                         'BestAskPrice',
                                                         'BestAskQty'])
        while True:
            response = await socket.recv()
            data = mostrar1(response, data)
            #resp_dict = json.loads(response)
            #await print_result(resp_dict)
            await asyncio.sleep(10)


async def main(url):
    task1 = asyncio.create_task(start_listening_to_binance(url))
    await asyncio.gather(task1)


binance_url = 'wss://stream.binance.com:9443/ws/btcusdt@bookTicker'
print('Listening is started...')
asyncio.run(main(binance_url))

