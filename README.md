# BConTrast

This repository contains the train, dev, and test sets of the BConTrasT corpus used in the [chat translation task](http://www.statmt.org/wmt20/chat-task.html) for [WMT20](http://www.statmt.org/wmt20/index.html).
It is based on the [Taskmaster-1 corpus](https://arxiv.org/pdf/1909.05358.pdf) which includes monolingual (i.e. English) task-based dialogs in six domains, 
  i.e. (i) ordering pizza, (ii) creating auto repair appointments, (iii) setting up ride service, (iv) ordering movie tickets, (v) ordering coffee drinks, and (vi) making restaurant reservations.
  A subset of [Taskmaster-1 corpus](https://arxiv.org/pdf/1909.05358.pdf) was selected and translated into German at [Unbabel](https://unbabel.com).
  
Each conversation in the data file has the following structure:
* ConversationID: A unique identifier for each conversation.
* Utterances: An array of utterances that make up the conversation. Each utterance has the following fields:
  - UtteranceID: A 0-based index indicating the order of the utterances in the conversation.
  - Speaker: Either customer or agent, indicating which role generated this utterance.
  - Source: The utterance in the original source language.
  - Target: The utterance in the translated target language.
    

**Note:** Since here we assume customer and agent speak in their own language, the source and target text might be in English or German depending on the role.

# License
Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
The dataset in this repository, used for the WMT20 shared task, is provided under the terms of the [CC-BY-SA-4.0](LICENSE-CC-BY-SA-4.0). 

# Citation
If you use this please cite:

M Amin Farajian, António V Lopes, André FT Martins, Sameen Maruf, Gholamreza Haffari (2020). Findings of the wmt 2020 shared task on chat translation (https://aclanthology.org/2020.wmt-1.3/)

    @inproceedings{farajian-etal-2020-findings,
        title = "Findings of the {WMT} 2020 Shared Task on Chat Translation",
        author = "Farajian, M. Amin  and
          Lopes, Ant{\'o}nio V.  and
          Martins, Andr{\'e} F. T.  and
          Maruf, Sameen  and
          Haffari, Gholamreza",
        booktitle = "Proceedings of the Fifth Conference on Machine Translation",
        month = nov,
        year = "2020",
        address = "Online",
        publisher = "Association for Computational Linguistics",
        url = "https://aclanthology.org/2020.wmt-1.3",
        pages = "65--75",
    }


