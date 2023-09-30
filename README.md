# PubMed Knowledgebase AI Chatbot powered by BioGPT
This chatbot web application allows you to interact with large language model Bio-GPT to query PubMed,which is an extensive and comprehensive biomedical literature knowledge database. This application not only aims at providing various context-based answers to targeted queries but also helping researches to explore potential subtle relationships.

### More about BioGPT:
BioGPT is a generative pre-trained transformer for biomedical text generation and mining developed by Mcrosoft. 
It is trained on millions of previously published biomedical research articles. 
The original paper about it can be found here [Article link](https://academic.oup.com/bib/article-abstract/23/6/bbac409/6713511?redirectedFrom=fulltext)

BioGPT can perform tasks such as answering questions, extracting relevant data, and generating text relevant to biomedical literature, 
for example, as a potential drug development application, BioGPT can generate descriptions of a specific therapeutic class—such as
 “Janus kinase 3 (JAK-3)”—or of a specific therapy—such as “Apricitabine.” If you are interested in more details about this, you can read this article [Article link](https://www.clinicaltrialsarena.com/news/biogpt-healthcare/?cf-view)


### ChatBot Installation
```
conda create -n pubmed_chatbot python=3.9.18
pip install -r requirements.txt
```

### How to use?
- Enter a keyword or a seed query in the text box and press enter to receive gap-fill responses
- When "Exploration mode" is turned on, new responses may be generated for each query rerun to explore more diverse and interesting answers


### Examples:
 - Inflammation related gene include
 - FN1 vs CRC neoplasm
 - TP53 
 


## **Live Demo Tool Web URL** : 

   The graphical user interface (GUI) for this biomedical AI chatbot was created using Streamlit, chosen for its efficiency in rapid prototyping.

   This application has been carefully packaged and deployed on Google Cloud, where it is currently being hosted. You are welcome to give it a try by following this link ([LIVE DEMO](http://34.23.165.128:8501/)) . Please note, the application is currently hosted on a spot instance for demo purpose only, which means it may experience periodical maintenance shutdowns. However, please feel free to return to revisit once it's back online.

 
 **---------------------------------------------------------------------------------------**
 
  
 
 ![Q1](https://github.com/mojocraftdojo/pubmed_chatbot_llm/blob/main/UI_demo1.png "demo1")
 ![Q2](https://github.com/mojocraftdojo/pubmed_chatbot_llm/blob/main/UI_demo2.png "demo2")

 
 
