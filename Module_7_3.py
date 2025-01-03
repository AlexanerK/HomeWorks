from idlelib.replace import replace

class WordsFinder:
    all_words = dict()
    def __init__(self,*name):
        self.file_names = name

    def get_all_words(self):
        for i in self.file_names:
            with (open(i, encoding='utf-8') as file):
                text_word = [file.read().lower().replace(',','').replace('.','')
                    .replace('=','').replace('!','').replace('?','').
                                   replace('-','').replace(':','').
                                   replace(';','').split()]
                words = dict(zip([i], text_word))
            self.all_words.update(words)
        return self.all_words

    def find(self, word):
        self.word = word.lower()
        index_dict = {}
        index =[]
        g = []
        for words in self.get_all_words().values():
            print(words)
            if self.word in words:
                j = [words.index(self.word)+1]
                g.append(j)
        index = dict(zip(self.file_names, g))
        index_dict.update(index)
        return index_dict

    def count(self,word):
        self.word = word.lower()
        count_dict = {}
        count =[]
        for words in self.get_all_words().values():
            if self.word in words:
                i = [words.count(self.word)]
                count.append(i)
        counts = dict(zip(self.file_names, count))
        count_dict.update(counts)
        return count_dict





finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))