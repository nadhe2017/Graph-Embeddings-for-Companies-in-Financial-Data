Collect company descriptions for companies mentioned in the below file(s) from bloomberg : https://www.bloomberg.com/research//common/symbollookup/symbollookup.asp?region=ALL&textIn=a&x=0&y=0&lookuptype=private.
For now we can focus on the document level entities.

## doc_level_entities.txt :  
- Entites in decreasing order of their frequency at the document level
- Has format "Company Name" : "Description" with the "Description" obtained from the bloomberg website.
                        
## sent_level_entities.txt :
- Entites in decreasing order of their frequency at the sentence level
- Has format "Company Name" : "Description" with the "Description" obtained from the bloomberg website.
                         
## doc_level_entities_count.txt : 
- Count of entities at the document level

## sent_level_entities_count.txt : 
- Count of entities at the sentence level

## Tips for gathering the descriptions
- Sometimes searching for the complete name on the website might not yield a search result. Truncate the name and search. I would suggest using Google if necessary since bloomberg database is likely incomplete. Use your discretion to choose the correct company name from the results.
- The entity names in the above file(s) are not perfect. Try to look for complete company names. For e.g., "Goldman Sachs & Co" is identified as "Sachs & Co". Put the correct description for the company name and prefix the corrected company name with a \* as follows:
  - "\*Goldman Sachs & Co" : "Description for Goldman Sachs & Co"
- If a description cannot be found leave the description as is, don't delete the key from the dictionary.
- Ignore entities which are clearly misidentified. For e.g., "Surviving Corporation" is a term that denotes an entity post-merger. It is not a company name.
