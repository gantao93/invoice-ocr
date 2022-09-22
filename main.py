#!/usr/bin python3
# -*- coding:UTF-8 -*-
# Author: nigo
import ocr
# from pdf2img import pyMuPDF_fitz
import os
import pandas as pd

def get_file_path(dictory):
    paths = os.listdir(dictory)
    paths = [os.path.join(dictory,path) for path in paths]
    return paths

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('expand_frame_repr', False)
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    pdf_dictory = './pdf'
    img_dictory = './img'
    paths = get_file_path(pdf_dictory)
    # for path in paths:
    #     pyMuPDF_fitz(path,img_dictory)
    print('pdf转png完成')
    paths = get_file_path(img_dictory)
    df_list = []
    for path in paths:
        df_list.append(ocr.invoice_ocr(path))
    df = pd.concat(df_list)
    print(df)
    df.to_excel('output.xlsx',index=False)
