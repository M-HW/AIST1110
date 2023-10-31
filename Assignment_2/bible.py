import requests, json, string

def get_text(ver='akjv', bk=None, ch=None):
    url = 'https://getbible.net/v2/' + ver
    if bk:
        url += '/'+str(bk)
    if ch:
        url += '/'+str(ch)
    url += '.json'
    r= requests.get(url)
    #print(r.json())
    text = ''
    if bk == None and ch == None:
        for i in r.json()["books"]:
            for k in i["chapters"]:
                for b in k["verses"]:
                    text += b["text"] +' '
    elif ch== None:
        for a in r.json()["chapters"]:
            for b in a["verses"]:
                text += b["text"] +' '
    else:
        for b in r.json()["verses"]:
            text += b["text"] +' '
    return text

def top_words(text: str, n=10):
    remove = string.punctuation
    #remove = remove.replace("'", '')
    count ={}
    words = text.split()
    stop_word = []
    with open('stopwords.txt') as fin:
        for line in fin:
            words1 = line.split()
            for word1 in words1:
                stop_word.append(word1)
    for word in words:
        word_strip = word.strip(remove) 
        word_strip_lower = word_strip.lower()
        if word_strip_lower in stop_word or len(word_strip) == 1:
            continue
        if word_strip not in count:
            count[word_strip] = 1
        else:          
            count[word_strip] += 1
    count_sorted_list = sorted(count, key=count.get, reverse= True)
    count_sorted = {}
    n_c = 0
    for i in count_sorted_list:
        if n_c >= n:
            break
        count_sorted[i] = count[i]
        n_c += 1
    return count_sorted




if __name__ == "__main__":
    versions = ["akjv", "kjv", "web"]
    torah = {"Gen": 1, "Ex": 2, "Lev": 3, "Num": 4, "Deut": 5}
    gospel = {"Matt": 40, "Mark": 41, "Luke": 42, "John": 43}
    scripture = get_text("web", torah["Gen"], 1) # chapter
    words = top_words(scripture)
    print("Gen1:\n", words)

    for g in gospel: # book
        scripture = get_text(bk=gospel[g])
        words = top_words(scripture)
        print(g + ":\n", words)

    for v in versions: # bible
        scripture = get_text(v)
        words = top_words(scripture)
        print(v + ":\n", words)
