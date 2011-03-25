import fnmatch
import os

def get_sentences_files():
    for file in os.listdir('../resources/sentences/'):
        if fnmatch.fnmatch(file, '*.txt'):
            yield file

def get_latest_daily_sentences_files():
    list = sorted(os.listdir('../resources/sentences/'))
    if(len(list) > 0):
        latest_day = list[0][0:10]
    else:
        raise ValueError("There is no sentences files!")
    
    for file in list:
        if(file[0:10] == latest_day):
            yield file
            #pass
        else:
            break

            
def main():
    get_sentences_files()
    get_latest_daily_sentences_files()

if __name__ == '__main__':
    main()