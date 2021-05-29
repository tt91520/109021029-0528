import sys
from PIL import Image, ImageFilter

def resizeImg(imageName):
    try:
        img = Image.open(imageName)
        print("Current size (width, height): ", img.size)
        newWidth = int(input("new width: "))
        ratio = float(newWidth) / img.size[0]
        newHeight = int(img.size[1] * ratio)
        resizedImg = img.resize((newWidth, newHeight), Image.BILINEAR)
        print("new image size: ", resizedImg.size)
        dotIndex = imageName.index(".")
        newImagName = imageName[:dotIndex] + "_resize" + imageName[dotIndex:]
        resizedImg.save(newImagName)
        print("Resized img is saved as ", newImagName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)

def rotateImg(imageName):
    try:
        img = Image.open(imageName)
        print("旋轉選項: ")
        print("1. 左右翻轉")
        print("2. 上下翻轉")
        print("3. 旋轉90度")
        print("4. 旋轉180度")
        print("5. 旋轉270度")
        print("6. other")
        op1 = input("您要進行的操作: ")
        if op1 == "1":
            newIm = img.transpose(Image.FLIP_LEFT_RIGHT)
            str1 = "_flip_LR"
        elif op1 == "2":
            newIm = img.transpose(Image.FLIP_TOP_BOTTOM)
            str1 = "_flip_TB"
        elif op1 == "3":
            newIm = img.transpose(Image.ROTATE_90)
            str1 = "_flip_90"    
        elif op1 == "4":
            newIm = img.transpose(Image.ROTATE_180)
            str1 = "_flip_180"
        elif op1 == "5":
            newIm = img.transpose(Image.ROTATE_270)
            str1 = "_flip_270"
        elif op1 == "6":
            rotDegree = float(input("Rotate degree: "))
            newIm = img.rotate(rotDegree)
            str1 = "_flip_" + str(rotDegree)
        dotIndex = imageName.index(".")
        newImagName = imageName[:dotIndex] + str1 + imageName[dotIndex:]
        newIm.save(newImagName)
        print("Rotated img is saved as ", newImagName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)       

def genThumbnal(imageName):
    try:
        img = Image.open(imageName)
        print("Current size (width, height): ", img.size)
        newWidth, newHeight = map(int, input("請輸入縮圖尺寸: ").split())
        img.thumbnail((newWidth, newHeight))
        dotIndex = imageName.index(".")
        newImagName = imageName[:dotIndex] + "_thumbnail" + imageName[dotIndex:]
        img.save(newImagName)
        print("Thumbnail imge is saved as ", newImagName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)

def applyFilter(imageName):
    try:
        img = Image.open(imageName)
        print("濾鏡選項: ")
        print("1. 模糊 (BLUR)")
        print("2. 輪廓 (CONTOUR)")
        print("3. 細節增強 (DETAIL)")
        print("4. 邊緣增強 (EDGE_ENHANCE)")
        print("5. 深度邊緣增強 (EDGE_ENHANCE_MORE)")
        print("6. 浮雕效果 (EMBOSS)")
        print("7. 邊緣訊息 (FIND_EDGES)")
        print("8. 平滑效果 (SMOOTH)")
        print("9. 深度平滑效果 (SMOOTH_MORE)")
        print("A. 銳利化效果 (SHARPEN)")
        op1 = input("選擇要套用的濾鏡: ")
        if op1 == "1":
            newImg = img.filter(ImageFilter.BLUR)
            str1 = "_BLUR"
        elif op1 == "2":
            newImg = img.filter(ImageFilter.CONTOUR)
            str1 = "_CONTOUR"
        elif op1 == "3":
            newImg = img.filter(ImageFilter.DETAIL)
            str1 = "_DETAIL"
        elif op1 == "4":
            newImg = img.filter(ImageFilter.EDGE_ENHANCE)
            str1 = "_EDGE_ENHANCE"
        elif op1 == "5":
            newImg = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            str1 = "_EDGE_ENHANCE_MORE"
        elif op1 == "6":
            newImg = img.filter(ImageFilter.EMBOSS)
            str1 = "_EMBOSS"
        elif op1 == "7":
            newImg = img.filter(ImageFilter.FIND_EDGES)
            str1 = "_FIND_EDGES"
        elif op1 == "8":
            newImg = img.filter(ImageFilter.SMOOTH)
            str1 = "_SMOOTH"
        elif op1 == "9":
            newImg = img.filter(ImageFilter.SMOOTH_MORE)
            str1 = "_SMOOTH_MORE"
        elif op1 == "A":
            newImg = img.filter(ImageFilter.SHARPEN)
            str1 = "_SHARPEN"
        dotIndex = imageName.index(".")
        newImagName = imageName[:dotIndex] + str1 + imageName[dotIndex:]
        newImg.save(newImagName)
        print("Filtered img is saved as ", newImagName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)

def showMenu():
    print("---------------------")
    print("1: 等比例縮放")
    print("2: 圖片旋轉")
    print("3: 產生縮圖")
    print("4: 套用濾鏡")
    print("0: 結束")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        while True:
            showMenu()
            op = input("選擇功能: ")
            if op == "1":
                resizeImg(sys.argv[1])
            elif op == "2":
                rotateImg(sys.argv[1])
            elif op == "3":
                genThumbnal(sys.argv[1])
            elif op == "4":
                applyFilter(sys.argv[1])
            elif op == "0":
                print("Thank you.Bye bye! :)")
                break
            
    else:
        print("argument error")