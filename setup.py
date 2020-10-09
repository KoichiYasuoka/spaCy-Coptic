import setuptools,subprocess,platform

with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/spaCy-Coptic"

setuptools.setup(
  name="spacy_coptic",
  version="0.4.0",
  description="Coptic NLP wrapper for spaCy",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="MIT",
  keywords="Coptic spaCy",
  packages=setuptools.find_packages(),
  install_requires=["spacy>=2.2.2","deplacy>=1.7.0"],
  python_requires=">=3.6",
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: POSIX :: Linux",
    "Topic :: Text Processing :: Linguistic"
  ],
  project_urls={
    "coptic-nlp":"https://github.com/CopticScriptorium/coptic-nlp",
    "Source":URL,
    "Tracker":URL+"/issues",
  }
)
