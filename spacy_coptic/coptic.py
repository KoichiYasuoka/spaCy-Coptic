#! /usr/bin/python3 -i
# coding=utf-8

import numpy
from spacy.language import Language
from spacy.symbols import LANG,NORM,LEMMA,POS,TAG,DEP,HEAD
from spacy.tokens import Doc
from spacy.util import get_lang_class

class CopticLanguage(Language):
  lang="cop"
  max_length=10**6
  def __init__(self,api):
    self.Defaults.lex_attr_getters[LANG]=lambda _text:"cop"
    self.vocab=self.Defaults.create_vocab()
    self.tokenizer=CopticTokenizer(api,self.vocab)
    self.pipeline=[]
    self._meta={
      "author":"Koichi Yasuoka",
      "description":"derived from Coptic-NLP",
      "lang":"Coptic_NLP_cop",
      "license":"MIT",
      "name":"Coptic_NLP_cop",
      "parent_package":"Coptic-NLP",
      "pipeline":"Tokenizer, POS-Tagger, Parser",
      "spacy_version":">=2.1.0"
    }
    self._path=None

class CopticTokenizer(object):
  to_disk=lambda self,*args,**kwargs:None
  from_disk=lambda self,*args,**kwargs:None
  to_bytes=lambda self,*args,**kwargs:None
  from_bytes=lambda self,*args,**kwargs:None
  def __init__(self,api,vocab):
    self.model=api
    self.vocab=vocab
  def __call__(self,text):
    u=self.model(text) if text else ""
    vs=self.vocab.strings
    r=vs.add("ROOT")
    p={"ACAUS":"VERB","ACOND":"SCONJ","ADV":"ADV","ALIM":"SCONJ","APREC":"SCONJ","ART":"DET","CCIRC":"SCONJ","CFOC":"PART","CONJ":"CCONJ","COP":"PRON","CPRET":"AUX","CREL":"SCONJ","EXIST":"VERB","FUT":"AUX","IMOD":"ADV","NEG":"ADV","NPROP":"PROPN","NUM":"NUM","PDEM":"DET","PPOS":"DET","PREP":"ADP","PTC":"PART","PUNCT":"PUNCT"}
    words=[]
    lemmas=[]
    pos=[]
    tags=[]
    heads=[]
    deps=[]
    spaces=[]
    norms=[]
    for s in u.split("\n"):
      if s.startswith('<norm xml:id="u'):
        id=s[15:s.index('"',16)]
        i=s.index(' orig="')
        form=s[i+7:s.index('"',i+8)]
        words.append(form)
        i=s.find(' lemma="')
        lemmas.append(vs.add(form if i<0 else s[i+8:s.index('"',i+9)]))
        i=s.find(' norm="')
        norms.append(vs.add(form if i<0 else s[i+7:s.index('"',i+8)]))
        i=s.index(' func="')
        dep=s[i+7:s.index('"',i+8)]
        if dep=="root":
          heads.append(0)
          deps.append(r)
        else:
          i=s.find(' head="#u')
          heads.append(0 if i<0 else int(s[i+9:s.index('"',i+10)])-int(id))
          deps.append(vs.add(dep))
        i=s.index(' pos="')
        xpos=s[i+6:s.index('"',i+7)]
        tags.append(vs.add(xpos))
        upos="X"
        if xpos in p:
          upos=p[xpos]
        elif xpos.startswith("A"):
          upos="AUX"
        elif xpos.startswith("N"):
          upos="ADJ" if dep in {"amod","acl"} else "NOUN"
        elif xpos.startswith("P"):
          upos="PRON"
        elif xpos.startswith("V"):
          upos="VERB"
        pos.append(vs.add(upos))
        spaces.append(False)
      elif s.startswith("</norm_group>"):
        spaces[-1]=True
    doc=Doc(self.vocab,words=words,spaces=spaces)
    a=numpy.array(list(zip(lemmas,pos,tags,deps,heads,norms)),dtype="uint64")
    doc.from_array([LEMMA,POS,TAG,DEP,HEAD,NORM],a)
    doc.is_tagged=True
    doc.is_parsed=True
    return doc

class CopticWebAPI(object):
  def __init__(self,api="https://corpling.uis.georgetown.edu/coptic-nlp/api"):
    self.api=api
  def __call__(self,text):
    if text.strip()=="":
      return ""
    from urllib.request import urlopen
    from urllib.parse import quote
    with urlopen(self.api+"?data="+quote(text)) as r:
      return r.read().decode("utf-8")

def load(api=None):
  if api==None:
    parser=CopticWebAPI()
  elif type(api)==str:
    parser=CopticWebAPI(api)
  else:
    parser=api
  return CopticLanguage(parser)

