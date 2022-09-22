#!/usr/bin python3
# -*- coding:UTF-8 -*-
# Author: nigo
from paddleocr import PaddleOCR
import re
from PIL import Image
import pandas as pd

def invoice_ocr(path):
    result = PaddleOCR().ocr(path)
    print('result', result)
    inform = []
    for line in result:
        inform.append(line[1][0])

    String2 = '【' + '】【'.join(inform) + '】'
    print('String2',String2)
    if '发' in String2 or '票' in String2:
        print('yes')
    else:
        print('no')
        im = Image.open(path)
        out = im.transpose(Image.ROTATE_180)
        out.save(path)
        result = PaddleOCR().ocr(path)

        inform = []
        for line in result:
            inform.append(line[1][0])
        String2 = '【' + '】【'.join(inform) + '】'
    # 发票号码
    try:
        number = re.findall('(?<!\d)(\d{8})】',String2)[0]
    except:
        number=''
    invoice2 = re.sub('[a-zA-Z]','',String2)
    print('invoice2', invoice2)
    # 发票代码
    try:
        code = re.findall('(?<!\d)(\d{10,12})】',invoice2)[0]
    except:
        code = '' 
    # 校验码
    try:
        judge = re.findall('校验码[:：](\d+)】',invoice2)[0]
    except:
        judge = ''
    # 发票日期
    try:
        ymd = re.findall('\d{4}年\d{2}月\d{2}日',invoice2)[0]
    except:
        ymd = ''
    # 发票金额
    try:
        amounts = re.findall('￥\s*([0-9]*?\.\d*?)】',invoice2)
        amounts = [float(i) for i in amounts]
        amounts.sort()
        amount = amounts[-2]
        total_price = amounts[-1]
    except:
        amount = ''
        total_price = ''
    # 税率
    try:
        tax = re.findall('【(\d{1,2}%)】',invoice2)[0]
    except:
        tax = ''
    # 购买方
    try:
        purch_name = re.findall('称[:：](.*?)】',invoice2)[0]
    except:
        purch_name = ''
    # 销售方
    try:
        sale_name = re.findall('称[:：](.*?)】',invoice2)[1]
    except:
        sale_name = ''
    try:
        purch_id = re.findall('识别号[:：]([A-Z0-9]+)】',String2)[0]
        sale_id = re.findall('识别号[:：]([A-Z0-9]+)】',String2)[1]
    except:
        purch_id = ''
        sale_id = ''
    # 商品名称
    try:
        product_name = re.findall('税额(.*?)[0-9]',invoice2)[0].replace(" ", "")[2:-2]
        print(product_name)
    except:
        product_name = ''

    info = [[path,code,number,judge,ymd,product_name,amount,tax,total_price,purch_name,purch_id,sale_name,sale_id]]
    df = pd.DataFrame(info,columns=['路径','发票代码','发票号码','校验码','开票日期','货物或应税劳务服务名称','金额(税前)','税率','金额(税后)','购买方名称','购买方纳税人识别号','销售方名称','销售人纳税人识别号'])
    return df
        

if __name__ == "__main__":
    path = 'img/invoice3.png'
    result = invoice_ocr(path)
    print(result)
