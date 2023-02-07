import PIL.ImageColor
from PIL import Image
obrazok = Image.open("cica.png")
pixels = obrazok.load()

#def farby_minus(old_pxl):
sirka=obrazok.size[0]
dlzka=obrazok.size[1]
#print(obrazok.size)
#print(pixels[100,100])
for y in range(dlzka-1):
    for x in range(1,sirka-1):
        fuj_pixeli=pixels[x,y]

        red=fuj_pixeli[0]
        green=fuj_pixeli[1]
        blue=fuj_pixeli[2]

        factor=1
        new_red=int(round(factor*red/255)*(255/factor))
        new_green=int(round(factor*green/255)*(255/factor))
        new_blue=int(round(factor*blue/255)*(255/factor))

        mnam_pixeli=(new_red,new_green,new_blue)
        pixels[x,y]=mnam_pixeli

        E_red=red-new_red
        E_blue=green-new_green
        E_green=blue-new_blue

        index1=pixels[x+1,y]
        red1=index1[0]
        blue1=index1[2]
        green1=index1[1]
        FinalRed1=red1+E_red*7/16.0
        FinalBlue1=blue1+E_blue*7/16.0
        FinalGreen1=green1+E_green*7/16.0
        pixels[x+1,y]=(int(FinalRed1),int(FinalGreen1),int(FinalBlue1))


        index2=pixels[x-1,y+1]
        red2=index2[0]
        blue2=index2[2]
        green2=index2[1]
        FinalRed2=red2+E_red*3/16.0
        FinalBlue2=blue2+E_blue*3/16.0
        FinalGreen2=green2+E_green*3/16.0
        pixels[x-1,y+1]=(int(FinalRed2),int(FinalGreen2),int(FinalBlue2))


        index3=pixels[x,y+1]
        red3=index3[0]
        blue3=index3[2]
        green3=index3[1]
        FinalRed3=red3+E_red*5/16.0
        FinalBlue3=blue3+E_blue*5/16.0
        FinalGreen3=green3+E_green*5/16.0
        pixels[x,y+1]=(int(FinalRed3),int(FinalGreen3),int(FinalBlue3))


        index4=pixels[x+1,y+1]
        red4=index4[0]
        blue4=index4[2]
        green4=index4[1]
        FinalRed4=red4+E_red*1/16.0
        FinalBlue4=blue4+E_blue*1/16.0
        FinalGreen4=green4+E_green*1/16.0
        pixels[x+1,y+1]=(int(FinalRed4),int(FinalGreen4),int(FinalBlue4))




obrazok.show()
obrazok.save('BiBamacka.png')
# skuska=(98,66,51)
# print(skuska)
# l=(255,5,50)
# k=float(skuska[0]-l[0])
# o=float(skuska[1]-l[1])
# m=float(skuska[2]-l[2])
# new=(k,o,m)
#   skuska=new
# print(skuska)


