# Final Year Project Group RAYW4: A Knowledge Graph-based Recommendation Website for Computer Science Learners

## Web crawling (`crawling` subfolder)
We took reference from the selenium official page https://www.selenium.dev/documentation/webdriver/ to do the crawling
- `Crawling_final.ipynb`: Scraping the article HTML source code from website using selenium 
- `html2txt.ipynb`: Extract text and heading from HTML source code to txt files

## Entity extraction (`entity_extraction` subfolder)
Follow the instructions in https://github.com/stanfordnlp/stanza to pip install the stanza library and run the code after it. This subfolder includes two .py files:
- `corenlp.py`: Extraction of OpenIE triples and their wiki entities
- `corenlp_wiki.py`: Tokenization of the article and the extraction of tokens' wiki entities

## Knowledge graph embeddings  (`kg` subfolder)
This subfolder contains two schemes to get the knowledge graph embedding referencing https://github.com/thunlp/Fast-TransX
- `wikidata_server.py`: Server for requesting OpenKE WikiData KG entity embeddings
- `kg_preprocess.py`: Preprocess the data stream for training
- `Fast-TransX`: THU C++ implementation for KG training

## Recommendation model - DKN (`DKN` subfolder)
-  `data_loader.py`: Data Loader for tensorflow version
-  `DKN.py`: Tensorflow implementation of the DKN model
- `train.py`: training function of the Tensorflow implementation
- `main.py`: Microsoft recommenders version implementation of the training flow

## Backend Flask server (`flask_server` subfolder)
See the readme in the subfolder for more instructions to run the code

## Wix website (`wix` subfolder)
We wrote the frontend on the Wix online editor. This code is a copy from the editor, where each page is saved independently in a .js file. 
- `home.js`: HOME page
- `search.js`: SEARCH page 
- `collection.js`: COLLECTION page
- `interests.js`: INTERESTS page
- `signup.js`: REGISTER page 
- `login.js`: LOGIN page
