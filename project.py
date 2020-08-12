import os, shutil


    


folders = {
    'videos':['.mp4'],
    'audios':['.wav','.mp3'],
    'images':['.jpg','.png'],
    'documents':['.doc','.xlsx','.xls','.pdf','.zip','.docx']
}

def rename():
    for i in os.listdir(directory):
        if os.path.isdir(os.path.join(directory,i))== True:
            os.rename(os.path.join(directory,i),os.path.join(directory, i.lower()))


def move_file(ext, file_name):
    find = False
    for i in folders:
        if "."+ext in folders[i]:
            if i not in os.listdir(directory):
                os.mkdir(os.path.join(directory, i))
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,i))            
            find=True
            break

    if find == False:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory, other_name))
        shutil.move(os.path.join(directory,file_name),os.path.join(directory,other_name))            
        

directory = input("Enter The Path: ")
other_name = input("Enter THe Folder Name For Unknown Files: ")

rename()
all_files = os.listdir(directory)

for i in all_files:
    if os.path.isfile(os.path.join(directory,i))== True:
        move_file(i.split('.')[-1].lower(),i)
print('Files are Successfully send to their Specified Folder')
