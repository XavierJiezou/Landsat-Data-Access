import json


def limit(fpath: str, max_points: int = 500):
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    points = data['features'][0]['geometry']['coordinates'][0][0]
    step = len(points)//max_points+1
    data['features'][0]['geometry']['coordinates'][0][0] = points[::step]
    with open('json/Qinghai_lit.json', encoding='utf-8', mode='w') as f:
        json.dump(data, f, ensure_ascii=False)


if __name__ == '__main__':
    limit('json/Qinghai_del.json')
