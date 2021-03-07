import sys
sys.path.append('../')
from tushare_lib.tushare_utils import get_tushare_handle


def main():
    ts_api = get_tushare_handle()
    currency_df = ts_api.cn_m()
    currency_df.to_csv('currency_data.csv')


if __name__ == '__main__':
    main()
