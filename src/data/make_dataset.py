# -*- coding: utf-8 -*-
import pandas as pd


def main():
    _pdjson()


def _pdjson():
    json_path = "crawler/output.json"
    csv_save_path = "../data/processed"
    with open(json_path, encoding="utf-8") as f_input:
        dfjson = pd.read_json(f_input)
    dfjson.to_csv(f"{csv_save_path}/news_content.csv", index=False)


if __name__ == '__main__':
    main()
