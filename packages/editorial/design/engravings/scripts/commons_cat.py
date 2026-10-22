"""List files in Commons categories (titles only). usage: python -I commons_cat.py "Category:Foo" ["Category:Bar" ...]"""
import json, sys, urllib.parse, urllib.request

UA = "AccidentalGuideResearch/0.1 (illustration shortlist; contact hi@accidental.info)"
API = "https://commons.wikimedia.org/w/api.php"


def get(params):
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


for cat in sys.argv[1:]:
    cont = {}
    while True:
        d = get({"action": "query", "list": "categorymembers", "cmtitle": cat, "cmlimit": "500",
                 "format": "json", "cmtype": "file|subcat", **cont})
        for m in d["query"]["categorymembers"]:
            print(cat.split(":", 1)[1], "\t", m["title"])
        if "continue" in d:
            cont = d["continue"]
        else:
            break
