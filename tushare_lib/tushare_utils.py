import os
import tushare as ts

tushare_key = 'key.txt'


def get_tushare_key():
    current_path = os.path.dirname(os.path.realpath(__file__))
    key_path = '{}/{}'.format(current_path, tushare_key)
    if not os.path.exists(key_path):
        return ''
    fid = open(key_path)
    key = fid.readline()
    fid.close()
    return key


def get_tushare_handle():
    return ts.pro_api(get_tushare_key())


if __name__ == '__main__':
    print(get_tushare_key())
