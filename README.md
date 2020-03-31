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
# Citation
TBA
