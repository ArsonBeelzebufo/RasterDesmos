import dotenv
import os

def bmp(bmpPath):
    with open(bmpPath,'rb') as file:
        pass

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