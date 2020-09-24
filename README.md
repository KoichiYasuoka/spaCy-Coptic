[![Current PyPI packages](https://badge.fury.io/py/spacy-coptic.svg)](https://pypi.org/project/spacy-coptic/)

# spaCy-Coptic

[Coptic NLP](https://corpling.uis.georgetown.edu/coptic-nlp/) wrapper for spaCy

## Basic Usage

```py
>>> import spacy_coptic
>>> nlp=spacy_coptic.load()
>>> doc=nlp("ⲙⲟⲟϣⲉ ϩⲱⲥ ϣⲏⲣⲉ ⲙ̄ⲡⲟⲩⲟⲉⲓⲛ")
>>> for t in doc:
...   print("\t".join([str(t.i+1),t.orth_,t.lemma_,t.pos_,t.tag_,"_",str(0 if t.head==t else t.head.i+1),t.dep_,"_","_" if t.whitespace_ else "SpaceAfter=No"]))
...
1	ⲙⲟⲟϣⲉ	ⲙⲟⲟϣⲉ	VERB	V	_	0	ROOT	_	_
2	ϩⲱⲥ	ϩⲱⲥ	CCONJ	CONJ	_	3	mark	_	_
3	ϣⲏⲣⲉ	ϣⲏⲣⲉ	NOUN	N	_	1	advcl	_	_
4	ⲙ̄	ⲛ	ADP	PREP	_	6	case	_	SpaceAfter=No
5	ⲡ	ⲡ	DET	ART	_	6	det	_	SpaceAfter=No
6	ⲟⲩⲟⲉⲓⲛ	ⲟⲩⲟⲉⲓⲛ	NOUN	N	_	3	nmod	_	_
>>> import deplacy
>>> deplacy.render(doc,WordRight=True)
 ROOT ╔═════════ VERB  ⲙⲟⲟϣⲉ
 mark ║ ╔══════> CCONJ ϩⲱⲥ
advcl ╚>╚═╔═════ NOUN  ϣⲏⲣⲉ
 case     ║ ╔══> ADP   ⲙ̄
  det     ║ ║ ╔> DET   ⲡ
 nmod     ╚>╚═╚═ NOUN  ⲟⲩⲟⲉⲓⲛ
```

`spacy_coptic.load(api)` loads spaCy Language pipeline for Coptic NLP WebAPI. If you have already installed [coptic-nlp](https://github.com/CopticScriptorium/coptic-nlp) and you have `coptic_nlp.py` in current directory, try the pipeline locally just as:

```py
>>> import spacy_coptic
>>> from coptic_nlp import nlp_coptic
>>> nlp=spacy_coptic.load(nlp_coptic)
>>> doc=nlp("ⲙⲟⲟϣⲉ ϩⲱⲥ ϣⲏⲣⲉ ⲙ̄ⲡⲟⲩⲟⲉⲓⲛ")
```

## Installation

```sh
pip install spacy_coptic
```

