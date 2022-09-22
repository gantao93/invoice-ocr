# #!/usr/bin python3
# # -*- coding:UTF-8 -*-
# # Author: nigo
# import sys, fitz, os, datetime
#
# def pyMuPDF_fitz(pdf_path, image_path):
#     pdfDoc = fitz.open(pdf_path)
#     base_name = os.path.basename(pdf_path)
#     pdf_name = os.path.splitext(base_name)[0]
#     if pdfDoc.pageCount == 1:
#         flag = True
#     else:
#         flag = False
#     for pg in range(pdfDoc.pageCount):
#         page = pdfDoc[pg]
#         rotate = int(0)
#         # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
#         # 此处若是不做设置，默认图片大小为：792X612, dpi=96
#         zoom_x = 2 #(1.33333333-->1056x816)   (2-->1584x1224)
#         zoom_y = 2
#         mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
#         pix = page.getPixmap(matrix=mat, alpha=False)
#         if not os.path.exists(image_path):#判断存放图片的文件夹是否存在
#             os.makedirs(image_path) # 若图片文件夹不存在就创建
#         if flag:
#             image_name = pdf_name + '.png'
#         else:
#             image_name = pdf_name + '_%s.png' % pg
#         image_path = os.path.join(image_path,image_name)
#         pix.writePNG(image_path)#将图片写入指定的文件夹内
#
# if __name__ == "__main__":
#     pdfPath = './TJB/餐饮94.pdf'
#     imagePath = './img'
#     pyMuPDF_fitz(pdfPath, imagePath)
