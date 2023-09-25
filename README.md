# PubMed Knowledgebase AI Chatbot powered by BioGPT
This chatbot web application allows you to interact with large language model Bio-GPT to query PubMed,which is an extensive and comprehensive biomedical literature knowledge database. This application not only aims at providing various context-based answers to targeted queries but also helping researches to explore potential subtle relationships.

### More about BioGPT:
BioGPT is a generative pre-trained transformer for biomedical text generation and mining developed by microsoft. The original paper about it can be found here if you are interested in more details. [click here](https://academic.oup.com/bib/article-abstract/23/6/bbac409/6713511?redirectedFrom=fulltext)


### ChatBot Installation
```
conda create -n pubmed_chatbot python=3.9.18
pip install -r requirements.txt
```

### How to use?
- Enter a keyword or a seed query in the text box and press enter to receive gap-fill responses
- When "Exploration mode" is turned on, new responses will be generated for each query rerun to explore more diverse and interesting answers

### **Tool Live Demo URL** : 
- This biomedical AI chatbot was packaged and deployed to google cloud and currently hosted on GCP for demo purpose. You can try it out live at here. [click here](http://34.23.165.128:8501/) 

### Example queries and answers :
 - Inflammation related gene include
 - FN1 vs CRC neoplasm
 - TP53 
 
 ![Q1](https://github.com/mojocraftdojo/pubmed_chatbot_llm/blob/main/UI_demo1.png "demo1")
 ![Q2](https://github.com/mojocraftdojo/pubmed_chatbot_llm/blob/main/UI_demo2.png "demo2")

 
 
