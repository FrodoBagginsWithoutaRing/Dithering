#na zaciatku budeme mat dva body a nasou ulohou je pixel po pixli vykreslit usečku (a,b)(c,d)
#a<c,   b<d

#doplnit tak aby to fungovalo vzdy !!!!!!
#input dlzku
from PIL import Image
pic=Image.new('RGB',(250,250),'white')
pixels=pic.load()
A=(2,2)
B=(100,50)
k = (B[1]-A[1])/(B[0]-A[0])
q=A[1]-k*A[0]
for x in range(A[0],B[0]):
    y=(k*x+q)
    pixels[x,y]=(0,0,0)

pic.show()




#priprady pozor na to ak ti zadaju prvy bod B
# pozor ak je y vacie nez x
# ked je kolma bude zle
