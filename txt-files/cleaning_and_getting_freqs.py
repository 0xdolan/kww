import re
from collections import Counter

# REMOVE ALL THE EXTRA CHARACTERS OUT OF ARABIC RANGE
wl = "wiki_wordlist_original.txt"
cleaned_wl = "cleaned_wl.txt"
with open(wl, "r", encoding="utf-8") as rf, open(
    cleaned_wl, "a", encoding="utf-8"
) as cwl:
    extra_chars = re.compile(
        r"[^'آأؤإئابةتثجحخدذرزسشصضطظعغؽفقلمنهوًٌٍَُِّْٖٓٔٗٚٛٞٮٰٱٶٹپچڈڌڎڏڑڒڕژښڤکگڵڼڽۀۆۉۊۋیۍێۏېەۗۡۥ\n']+"
    )
    word = re.sub(extra_chars, r"", rf.read())
    word = re.sub(re.compile(r"[\n]+"), r"\n", word)
    cwl.write(word + "\n")


# COUNT THE FREQUENTS
count = "count.txt"
with open(cleaned_wl, "r", encoding="utf-8") as rf, open(
    count, "w", encoding="utf-8"
) as cf:
    # print(sorted(set(rf.read())))
    count = Counter(rf.read().split("\n"))
    # print(count.most_common(50))
    for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True):
        l = f"{k},{v}"
        cf.write(l + "\n")


print("Finished")
