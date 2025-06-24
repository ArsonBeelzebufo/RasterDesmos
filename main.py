import dotenv
import os

def bmp(bmpPath): #assumes BITMAPINFOHEADER, V4, or V5
    with open(bmpPath,'rb') as file:
        content=file.read()
        with open("out.txt",'w') as file:
            file.write(' '.join([str(content[i]) for i in range(len(content))]))
        DIB=int.from_bytes(content[14:18],byteorder='little')
        wPixels=int.from_bytes(content[18:22],byteorder='little')
        hPixels=int.from_bytes(content[22:26],byteorder='little')
        bitsPerPixel=int.from_bytes(content[28:30],byteorder='little')
        compression=content[30:34]
        print(compression)
        if DIB>40:
            colorspace=content[70:74].decode('ascii')
            print(colorspace)
            if compression==b'\x03\x00\x00\x00':
                rMask=content[54:58]
                gMask=content[58:62]
                bMask=content[62:66]
                aMask=content[66:70]
            if colorspace=='':
                rGamma=content[110:114]
                gGamma=content[114:118]
                bGamma=content[118:122]

def polygonize(*pixel): #x,y,rgba
    x=pixel[0]
    y=-pixel[1]
    c=pixel[2]
    return f"\\operatorname{{polygon}}\\left(\\left({x},{y}\\right),\\left({x+1},{y}\\right),\\left({x+1},{y-1}\\right),\\left({x},{y-1}\\right)\\right)",f"\\operatorname{{rgb}}\\left({int(c[:2],16)},{int(c[2:4],16)},{int(c[4:6],16)}\\right)",f"{int(c[6:],16)}/255"
def equatize(colorArray):
    eqs="["
    cEq="C=["
    oEq="O=["
    for y in range(len(colorArray)):
        for x in range(len(colorArray[y])):
            temp=polygonize(x,y,colorArray[y][x])
            eqs+=temp[0]+','
            cEq+=temp[1]+','
            oEq+=temp[2]+','
    eqs=eqs[:-1]+']'
    cEq=cEq[:-1]+']'
    oEq=oEq[:-1]+']'
    return eqs+'\n'+cEq+'\n'+oEq

dotenv.load_dotenv()
filepath=os.getenv("RasterPath")
bmp(filepath)