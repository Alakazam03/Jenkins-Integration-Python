import os
import numpy as np
from collections import Counter

def make_Dictionary(root_dir):
    all_words=[]
    emails=[os.path.join(root_dir,f) for f in os.listdir(root_dir)]
    for mail in emails:
        with open(mail) as m:
            for line in m:
                words=line.split()
                all_words+=words
    dictionary = Counter(all_words)
    list_to_remove = dictionary.keys()
    print list_to_remove
    for item in list_to_remove:
        if item.isalpha() == False:
            del dictionary[item]
        elif len(item) ==1:
            del dictionary[item]


    return dictionary.most_common(3000)








TRAIN_DIR = "../train-mails"
TEST_DIR = "../test-mails"

dictionary = make_Dictionary(TRAIN_DIR)
print (dictionary)
