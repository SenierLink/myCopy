from pathlib import Path
import shutil

PATH = "D:\Document\工作\\0057"
TARGE_PATH="D:\Document\工作\mp4"

def main():
    targe_path = Path(TARGE_PATH)
    if not targe_path.exists():
        targe_path.mkdir(parents=True)
    for item in Path(PATH).rglob("*"):
        if "mp4" in item.suffix:
            old_name = item.name
            new_name = item.parent.name + old_name
            new_file = TARGE_PATH+"\\"+new_name
            shutil.copyfile(item.resolve(),new_file)
            print(item.resolve())

            
            
        
    
if __name__ == '__main__':
    main()