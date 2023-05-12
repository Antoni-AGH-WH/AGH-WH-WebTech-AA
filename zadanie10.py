import httpx
import time
x = 0

Faclist = [
    "https://www.agh.edu.pl/",
    "https://wilgz.agh.edu.pl",
    "https://www.metal.agh.edu.pl",
    "https://eaiib.agh.edu.pl",
    "https://iet.agh.edu.pl",
    "https://imir.agh.edu.pl",
    "http://wggios.agh.edu.pl",
    "https://geod.agh.edu.pl",
    "https://ceramika.agh.edu.pl",
    "http://odlewnictwo.agh.edu.pl",
    "http://wmn.agh.edu.pl",
    "https://wnig.agh.edu.pl",
    "https://www.zarz.agh.edu.pl",
    "https://weip.agh.edu.pl",
    "https://www.fis.agh.edu.pl",
    "https://wms.agh.edu.pl",
    "https://wh.agh.edu.pl",
]
word = "kraków"

if __name__ == "__main__":
    for i in range(len(Faclist)):
        start_time = time.time()
        a = Faclist[i]
        response = httpx.get(a)
        lines = response.text
        b = lines.lower().count(word)
        print("Word Krakow is {} times in {}".format(b, a))
        x = x+b
        end_time = time.time()
        print(end_time - start_time)
    print("Word {} apears {} times".format(word,x))
