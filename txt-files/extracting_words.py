# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


wl = "wordlist.txt"  # got the wordlist from https://github.com/layik/kurdi
ww = "wiki_wordlist.txt"
word_set = set()
with open(wl, "r", encoding="utf-8") as rf, open(ww, "a", encoding="utf-8") as wf:
    for word in tqdm(rf):
        word = word.strip()
        if word not in word_set:
            word_set.add(word)
            # print(word)
            host = "http://localhost:9454/" + word
            # print(host)
            # # host = "http://localhost:9454/کوردستان"
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
            }
            url = requests.get(host, headers=headers)
            url.encoding = "utf-8"
            # # # print(host)
            if url.status_code == 200:
                # print(f"{word} = 200")
                soup = BeautifulSoup(url.text, "lxml")
                for w in soup.find_all("div", "mw-body"):
                    for word in w.text.split():
                        # print(word)
                        pattern = re.compile(
                            r"[\nA-Za-z.\"\':٬,Ş#$%;؛|^&=><٭٪+v؟!?•*\–،٫\-ـ\(\)\]\[/‍‍0-9٠-٩۰-۹]+"
                        )
                        word = re.sub(pattern, r"", word)
                        word = (
                            word.replace("ﮫ", "ه")  # H
                            .replace("ﻪ", "ه")  # H
                            .replace("ﻩ", "ه")  # H
                            .replace("ﻫ", "ه")  # H
                            .replace("ھ", "ه")  # H
                            .replace("ﺶ", "ش")
                            .replace("ﺷ", "ش")
                            .replace("ﺸ", "ش")
                            .replace("ﺲ", "س")
                            .replace("ﺳ", "س")
                            .replace("ﺴ", "س")
                            .replace("ﻋ", "ع")
                            .replace("ﻌ", "ع")
                            .replace("ﻏ", "غ")
                            .replace("ﯿ", "ی")
                            .replace("ﯾ", "ی")
                            .replace("ﯽ", "ی")
                            .replace("ﯚ", "ۆ")
                            .replace("ﺐ", "ب")
                            .replace("ﭬ", "ڤ")
                            .replace("ﭭ", "ڤ")
                            .replace("ﭻ", "چ")
                            .replace("ﭼ", "چ")
                            .replace("ﭽ", "چ")
                            .replace("ﺋ", "ئ")
                            .replace("ﺌ", "ئ")
                            .replace("ﻮ", "و")
                            .replace("ﺰ", "ز")
                            .replace("ﺮ", "ر")
                            .replace("ﮋ", "ژ")
                            .replace("ﺪ", "د")
                            .replace("ﻨ", "ن")
                            .replace("ﻧ", "ن")
                            .replace("ﻦ", "ن")
                            .replace("ﻤ", "م")
                            .replace("ﻣ", "م")
                            .replace("ﻢ", "م")
                            .replace("ﺨ", "خ")
                            .replace("ﺧ", "خ")
                            .replace("ﺤ", "ح")
                            .replace("ﺣ", "ح")
                            .replace("ﺠ", "ج")
                            .replace("ﺟ", "ج")
                            .replace("ﭘ", "پ")
                            .replace("ﭙ", "پ")
                            .replace("ﻒ", "ف")
                            .replace("ﻓ", "ف")
                            .replace("ﻔ", "ف")
                            .replace("ﻠ", "ل")
                            .replace("ﻟ", "ل")
                            .replace("ﻞ", "ل")
                            .replace("ﻘ", "ق")
                            .replace("ﻗ", "ق")
                            .replace("ﻖ", "ق")
                            .replace("ى", "ی")
                            .replace("ي", "ی")
                            .replace("ﺘ", "ت")
                            .replace("ﺖ", "ت")
                            .replace("ﺗ", "ت")
                            .replace("ﺎ", "ا")
                            .replace("ﺑ", "ب")
                            .replace("ﺒ", "ب")
                            .replace("ﮕ", "گ")
                            .replace("ﮔ", "گ")
                            .replace("ﮓ", "گ")
                            .replace("ﮑ", "ک")
                            .replace("ﮐ", "ک")
                            .replace("ﮏ", "ک")
                            .replace("ك", "ک")
                            .replace("ﺆ", "ؤ")
                            .replace("ﻻ", "لا")
                            .replace("ﻼ", "لا")
                        )

                        wf.write(word + "\n")
            else:
                #     # print(url, 404)
                #     # print(f"{word} = 404")
                pass
# print(word_set)
print("DONE.")
