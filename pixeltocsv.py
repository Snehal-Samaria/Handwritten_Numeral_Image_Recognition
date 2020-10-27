def pixel(pxl):
    import os.path
    from os import path
    global flag

    px=[]
    for i in pxl:
        px.append(str(255-int(i)))
    filename='input_database.csv'
    def checkFile(filename):
        if path.exists(filename)==True:
            flag=0
        else:
            flag=1
        return flag
    flag=checkFile(filename)

    print(str(flag))
    
    import csv 
    if flag==1:
        header = []
        for i in range(0,784):
            header.append('Pixel'+str(i))
        #print(header)
        d=dict(zip(header,px))
        #d['Label']=''
        #L=[pv]
        file = open(filename, 'w+', newline ='') 

        with file: 
            writer = csv.DictWriter(file,fieldnames = header) 
            writer.writeheader()
            writer.writerow(d)
        return 'File created & data inserted.'

    else:
        #print(pv)
        L=[px]
        #print(L)

        #d=dict(zip(header,pv))
        #d['Label']=''
        #print(d.values())    
        file = open(filename, 'a+', newline ='') 

        with file: 
            #writer = csv.DictWriter(file, fieldnames = header) 
            # writing data row-wise into the csv file
            write = csv.writer(file) 
            #writer.writeheader()
            write.writerows(L)
        print('Data inserted successfully!')
        return filename
#p=pixel(pixel_ary)
#print(p)
