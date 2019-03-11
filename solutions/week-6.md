# Week 6

Challenge

```text
string = "cbs aob'g zwts cf rsohv ksfs pih o gaozz dfwqs hc dom tcf hvs oqeiwfsasbh ct hvs ybckzsrus kvwqv w gciuvh, tcf hvs rcawbwcb w gvcizr oqeiwfs obr hfobgawh cjsf hvs szsasbhoz tcsg ct cif foqs"
my = string.split()

word = "the"
freq = 4

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

check_word_freq = {}
for i in my:
    try:
        check_word_freq[i] = check_word_freq[i] + 1
    except:
        check_word_freq[i] = 1

shift = 0
for key in check_word_freq.keys():
    if len(key) == len(word):
        if check_word_freq[key] == freq:
            shift = ord(word[0]) - ord(key[0]) 

for i in string:
    if i not in [" ", "'", ","]:
        print(alphabet[(alphabet.index(i) + shift) % 26], end = "")
    else:
        print(i, end = "")
```

