import file_reader

class latest_daily_report():
    def __init__(self):
        self.src_lines = []
        self.recite_lines = []
        list = file_reader.get_latest_daily_sentences_files()
        src_file = list.pop() #need rethink the return value
        
        for file in file_reader.get_latest_daily_sentences_files():
            pass
    
        
def main(self):
    file_reader.get_sentences_files()

if __name__ == '__main__':
    main()
