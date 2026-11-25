# Usage: python3 tools/library_add.py new.yml  -- adds/merges references into _data/library.yml
import sys, yaml, unicodedata, re
import os
REPO=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','_data')+'/'
lib=yaml.safe_load(open(REPO+'library.yml')); topics=yaml.safe_load(open(REPO+'library_topics.yml'))
new=yaml.safe_load(open(sys.argv[1]))
for t in new.get('topics',[]):
    if not any(x['id']==t['id'] for x in topics):
        pos=t.pop('after',None); idx=[x['id'] for x in topics].index(pos)+1 if pos else len(topics); topics.insert(idx,t)
def asc(s): return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
byk={e['key']:e for e in lib}
for m in new.get('move',[]): byk[m['key']]['topic']=m['topic']
for e in new.get('entries',[]):
    if e['key'] in byk:
        for c in e['cited_in']:
            if c not in byk[e['key']]['cited_in']: byk[e['key']]['cited_in'].append(c)
        continue
    first=e['authors'][0].split(',')[0] if e['authors'] else e['title']
    first=re.sub(r'^(von|van|de)\s+','',first)
    e['sort']=f"{asc(first)} {e['year']} {asc(e['title'])[:40]}"
    lib.append(e); byk[e['key']]=e
ids={t['id'] for t in topics}; assert all(e['topic'] in ids for e in lib)
lib.sort(key=lambda x:x['sort'])
yaml.safe_dump(lib,open(REPO+'library.yml','w'),allow_unicode=True,sort_keys=False,width=1000)
yaml.safe_dump(topics,open(REPO+'library_topics.yml','w'),allow_unicode=True,sort_keys=False,width=1000)
print(len(lib),'entries,',len(topics),'topics')
