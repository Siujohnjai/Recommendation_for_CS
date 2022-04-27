# Final Year Project Group RAYW4: A Knowledge Graph-based Recommendation Website for Computer Science Learners

## Crawling
crawling final: Scraping the article HTML source code from website using selenium 
html2txt：extract text and heading from HTML source code to txt files

## Entity extraction (entity_extraction subfolder)
Follow the instructions in https://github.com/stanfordnlp/stanza to pip install the stanza library and run the code after it. This subfolder includes two .py files:
- `corenlp.py` - Extraction of OpenIE triples and their wiki entities
- `corenlp_wiki.py` - Tokenization of the article and the extraction of tokens' wiki entities

## DKN

## Flask (flask_server subfolder)
See the readme in the subfolder for more instructions to run the code

## Wix website (wix subfolder)
These codes are copied from the Wix online editor, where each page is saved independently in a .js file. 
- HOME page (home.js)
- SEARCH page (search.js)
- COLLECTION page (collection.js)
- INTERESTS page (interests.js)
- REGISTER page (signup.js)
- LOGIN page (login.js)
