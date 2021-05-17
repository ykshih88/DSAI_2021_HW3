import pandas as pd
import time
import os
# You should not modify this part.
def config():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--consumption", default="./data/consumption.csv", help="input the consumption data path")
    parser.add_argument("--generation", default="./data/generation.csv", help="input the generation data path")
    parser.add_argument("--bidresult", default="./data/bidresult.csv", help="input the bids result path")
    parser.add_argument("--output", default="output.csv", help="output the bids path")

    return parser.parse_args()


def output(path, data):
    import pandas as pd

    df = pd.DataFrame(data, columns=["time", "action", "target_price", "target_volume"])
    df.to_csv(path, index=False)

    return

def transpose_time(date,plus_time):
    pre_d = time.strptime(date,'%Y-%m-%d %X')#按照格式轉換為9元組
    pre_d = time.mktime(pre_d)#轉換為時間戳
    next_d = pre_d + plus_time
    next_d = time.localtime(next_d)#將時間轉換為struct_time
    next_d = time.strftime("%Y-%m-%d %X",next_d)#轉換為字串
    return next_d
def next_day(date):
    date = transpose_time(date,86400)
    return date
def next_hour(date):
    date = transpose_time(date,3600)
    return date
if __name__ == "__main__":
    args = config()
    
    data_dir = ''
    cons_name = 'consumption.csv'
    gene_name = 'generation.csv'
    bid_name = 'bidresult.csv'
    cons_path = args.consumption
    gene_path = args.generation
    bid_path = args.bidresult
    cons_df = pd.read_csv(cons_path)
    gene_df = pd.read_csv(gene_path)
    bid_df = pd.read_csv(bid_path)
    
    data = []
    data_last_date = cons_df['time'].tolist()[-24]#-24 because last date time is 23:00:00
    tomorrow_date = next_day(data_last_date)
    for i in range(24):
        if(i>=10 and i<=15):
            data.append([tomorrow_date, "buy", 2.3, 1])
            data.append([tomorrow_date, "buy", 2.1, 0.5])
        if(i>=0 and i<=10):
            data.append([tomorrow_date, "sell", 2.666, 5])
            data.append([tomorrow_date, "sell", 2.588, 5])
        tomorrow_date = next_hour(tomorrow_date)
    output(args.output, data)
