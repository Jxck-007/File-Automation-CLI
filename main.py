
import os
import shutil
import argparse



class File_Automation():
    

    def __init__(self,upath):
        
        self.path=upath
        self.comp_count=0
        self.soft_count=0
        self.img_count = 0
        self.audio_count = 0
        self.video_count = 0
        self.doc_count = 0
        self.software_extensions=['.exe','.msi']
        self.compressed_extensions =['.zip','.rar','.7z']
        self.audio_extensions = ['.mp3', '.wav', '.aac']
        self.image_extensions = ['.png', '.jpg','.jpeg']
        self.video_extensions= [ '.mp4', '.mov', '.avi' ,'.mkv']
        self.document_extensions=['.txt', '.docx', '.pdf','.xlsx','.pptx','.xlsb']
    def current(self):  
        current_directory = os.getcwd()
        print(f"The Current Directory : {current_directory}")
    
    def list(self):
        print("\n".join(os.listdir(self.path)))
            
    
    def sort(self):
        for _ in os.listdir(self.path):
            self.root,self.ext=os.path.splitext(_)
            fpath=os.path.join(self.path,_)
            if os.path.isdir(fpath):
                continue
            if self.ext.lower() in self.image_extensions :
                path=os.path.join(self.path,'Images')
                os.makedirs(path, exist_ok=True)
                try:
                    shutil.move(fpath,path)
                    print(f'Moved {_} Successfully to Images')
                    self.img_count += 1
                except Exception as e:
                    print(e)


            elif self.ext.lower() in self.audio_extensions:
                path=os.path.join(self.path,'Audio')
                os.makedirs(path, exist_ok=True)
                try:
                    shutil.move(fpath,path)
                    print(f'Moved {_}  Successfully to Audio')
                    self.audio_count += 1
                except Exception as e:
                    print(e)


            elif self.ext.lower() in self.video_extensions :
                path=os.path.join(self.path,'Video')
                os.makedirs(path, exist_ok=True)
                try:
                    shutil.move(fpath,path)
                    print(f'Moved {_} Successfully to Video')
                    self.video_count+=1
                except Exception as e:
                    print(e)


            elif self.ext.lower() in self.document_extensions :
                path=os.path.join(self.path,'Document')
                os.makedirs(path, exist_ok=True)
                try:
                    shutil.move(fpath,path)
                    print(f'Moved {_} Successfully to Document')
                    self.doc_count+=1
                except Exception as e:
                    print(e)

            elif self.ext.lower() in self.compressed_extensions :
                path=os.path.join(self.path,'Compressed')
                os.makedirs(path, exist_ok=True)
                try:
                    shutil.move(fpath,path)
                    print(f'Moved {_} Successfully to Compressed')
                    self.comp_count+=1
                except Exception as e:
                    print(e)

            elif self.ext.lower() in self.software_extensions :
                path=os.path.join(self.path,'Software')
                os.makedirs(path, exist_ok=True)
                try:
                    shutil.move(fpath,path)
                    print(f'Moved {_} Successfully to software')
                    self.soft_count+=1
                except Exception as e:
                    print(e)        
    def total(self):  
        print("\nSummary:")
        print(f"📸 Images moved: {self.img_count}")
        print(f"🎵 Audio moved: {self.audio_count}")
        print(f"🎬 Video moved: {self.video_count}")
        print(f"📄 Documents moved: {self.doc_count}")
        print(f"📄 compressed items moved: {self.comp_count}")
        print(f"💿 Software moved: {self.soft_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='File_Automation',description="File Automation(Auto Sort Files)",usage="This is a Python script that automatically organizes files in a directory into folders based on their file types ")
    parser.add_argument("File_Path",metavar="path",type= str,help="Paste The File Path")
    args = parser.parse_args()                
    upath=args.File_Path
    A=File_Automation(upath)
    if os.path.exists(upath):
        A.current()
        A.list()
        A.sort()
        A.total()
