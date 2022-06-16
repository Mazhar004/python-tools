# English-Dictionary

## Requirements

- Python3
- Install **pyenchant** `pip install requirements.txt`
- Download 1 files from [GDrive](https://drive.google.com/drive/folders/1HrvgiX6e9rNPNGdCabm_F7CNXf2ijQ2H?usp=sharing)
    - Put this file ```dictionary.pickle``` in **```Dictionary``` Folder**

## English Dictionary Data

- Dictionary data collected from **Oxford dictionary** text file
- Dictionary data collected from **json file** [Link](https://github.com/HarikaGurram/DictionaryEnglishTransfer)
- All English word & meaning comprise in a **JSON** file
- Total number of available word is **131k** (1,31,965)
- If user input word didn't find in JSON, then it will suggest similar word to the user input
- It can be used as follwing method:

```python
  from dictionary import Dictionary
  dictionary_data = Dictionary()
  dictionary_data.suggest_status = True
  print(dictionary_data['cosmos'])
  >>> Everything that exists anywhere.

  print(dictionary_data['helo'])
  >>> We didn not find helo.
  >>> Please have a look similar word matching with your input key
      ['Help', 'Hel', 'Helot', 'Hero', 'He lo', 'He-lo', 'Hel o', 'Hole', 'Hello', 'Halo', 'Hell', 'Held']
```

## Word Game

Word generator game with follwing features:

- Generate all possible word from a given list of word set
- Generate word of given length from a given list of word set
- Show meaning of generated word

```python
  from word_game import WordGame
  word_list = ['hard','ware']
  wg = WordGame(word_list)
  print('Word with 6 length',wg.word_gen(6))
  >>> Word with 6 length ['warder', 'reward', 'wardha', 'adware', 'drawer', 'redraw', 'harder', 'harare'])

  print('Word with 8 length',wg.word_gen(8))
  >>> Word with 8 length ['hardware'])

  print('All Generated WordList',wg.all_word)
  >>> All Generated WordList {8: ['hardware'], 6: ['warder', 'reward', 'wardha', 'adware', 'drawer', 'redraw', 'harder', 'harare']})

  print('Word Meaning',wg['Hardware'])
  >>> The part of a computer that is fixed and cannot be altered without replacement or physical modification.

```

## Play Word

Generate word from given set of words **['rip','ice']** with length of 6

- `python3 play_word.py --word "land" --length 6`

```python
>>> Word with length of 6:
    ['pincer', 'prince']

>>> PINCER

    Pliers made of steel for removing nails from wood.
    --------------------------------------------------
>>> PRINCE

    Son of a prince, king, queen, emperor or empress, or other high-ranking person (such as a grand duke).
    --------------------------------------------------
```
