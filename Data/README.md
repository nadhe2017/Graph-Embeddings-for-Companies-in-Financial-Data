- Scripts folder contains:
	1. `b_private_companies.py`: Scripts used to scrape all the data like SEC filings and company names.
	2. `entity_extraction.py`: Script for using Comprehensive_Database and 8-K fillings to do entity_extraction, the test result should be updated tomorrow.

- `manual` folder contains:

	1. `Q1-Q4`: Hand labeled graph for each quater.
	2. `vis_process.py`: Script that process the manually labeled data to nodes and links for visualization and model training.
	3. `build_graph_data.py`: Script for composing dataset that can be trained for DMTE model from manually labeled data.
	4. `manual.json`: Parsed output from `vis_process.py`.
	5. `sec_dataset` folder: The output from `build_graph_data.py`. To train DMTE model, just copy & past this folder to the model. 

- `Comprehensive_Database.rar` has 2 files containing company names:
	1. **public_companies_database.csv** : A database of ~6,800 public companies in the US.  
	Format: Symbol | Name | Sector | Industry
	2. **private_companies_database.csv** : A database of ~1.8 million private companies worldwide.  
	Format: Company | Country
- `raw_8_K_fillings.zip` contains the raw 8-K fillings for all 4 quaters in 2018, is used for entity extraction.
- `Item_2.01_filings_2018_html.zip` contains the item 2.01 part extracted from 2018, is used for manual labeling.