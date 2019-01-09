#coding:utf-8
import os;
import shutil;
import zipfile 
from unrar import rarfile



###init
folderList = ['pj']
outputpath = ['output/pj']
###

for each in folderList:
    number = 0
    pathDir = os.listdir(each);  #folderName  
    for fn in pathDir:   #fn = 爱丽娜(17300696007)
        st_number = fn.split('(')[1].split(')')[0]
        st_name = fn.split('(')[0]
        stuNameList = os.listdir(each+r'/'+fn);  #all the file's names
        #print stuNameList[1]
        fileNameList = os.listdir(each+r'/'+fn+r'/'+stuNameList[1])
        if not os.path.exists(outputpath[0]):
        	os.makedirs(outputpath[0])
        output_folder = st_number+' '+st_name
        for i in range(len(fileNameList)):
            hwRoute = each+r'/'+fn+r'/'+stuNameList[1]+r'/'+fileNameList[i]
            format = fileNameList[i].split('.')[-1]
            #shutil.copyfile(hwRoute,outputpath[0]+r'/'+fn+'_'+str(i)+'.'+format)
            if os.path.isdir(outputpath[0]+r'/'+output_folder):
                pass
            else:
                os.mkdir(outputpath[0]+r'/'+output_folder)
            if format == 'rar':
                file = rarfile.RarFile(hwRoute)
                try:
                    file.extractall(outputpath[0]+r'/'+output_folder)
                except:
                    print(fileNameList[i],'fail')
                number+=1

            elif format == 'zip':
                with zipfile.ZipFile(hwRoute) as myzip:
                    try:
                        myzip.extractall(outputpath[0]+r'/'+output_folder)
                    except:
                        print(fileNameList[i],'fail')

                number+=1

            else:
                shutil.copyfile(hwRoute,outputpath[0]+r'/'+output_folder+r'/'+fileNameList[i])
                #print(outputpath[0]+r'/'+fn+r'/'+fileNameList[i])
                number+=1
            





print(number,'finish')


