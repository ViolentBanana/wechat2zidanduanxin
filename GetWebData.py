# coding= utf-8
import urllib.request
import json


# 格式化json输出
def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)


def query_data():
    baseUrl = f"http://d.guduodata.com/m/v3/billboard/list?" \
              "type=DAILY&" \
              "category=NETWORK_DRAMA&" \
              "date=2022-01-27&" \
              "attach=playCount&" \
              "orderTitle=gdi&" \
              "platformId=0"

    print(baseUrl)
    resu = urllib.request.urlopen(baseUrl)

    dat = json.loads(resu.read())
    js = get_pretty_print(dat)

    return js


data = query_data()

print(data)
