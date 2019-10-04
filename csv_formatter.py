#########################
#                       #
# ghPython              #
#                       #
# in  : RECOMUPUTE      #
# out : FORMAT         #
#                       #
#########################




import csv


if RECOMPUTE:
    pass



with open('C:/Users/yoshioca/Documents/Matrix_Font/Matrix_Font.csv') as f:
    
    reader = csv.reader(f)
    l = [row for row in reader]



panel = []

for i in xrange(len(l)):
    
    ### reverse list
    # i = len(l) - (i+1)
    
    if i%2 == 0:
        
        # print(l[i])
        # print(l[i+1])
        
        
        ### formatter
        char = l[i]
        char = char[0]
        
        mat = str(l[i+1])
        mat = mat[1 : -1]
        mat = mat.replace("'", "")
        mat = mat.replace(" ", "")
        
        
        ### Set Dictionary
        out = "[\"{}\", {}],".format(char, mat)
        
        ### Debug, Number Slider
        # out = "[\"{}\", {}],".format(int(i/2), mat)
        
        
        print(out)
        
        panel.append(out)



FORMAT = panel