- Scripts folder contains:
	1. Scripts used to scrape all the data like SEC filings and company names.
	2. Python script for using Comprehensive_Database and 8-K fillings to do entity_extraction, the test result should be updated tomorrow.
- Comprehensive_Database.rar has 2 files containing company names:
	1. **public_companies_database.csv** : A database of ~6,800 public companies in the US.  
	Format: Symbol | Name | Sector | Industry
	2. **private_companies_database.csv** : A database of ~1.8 million private companies worldwide.  
	Format: Company | Country
- raw_8_K_fillings.zip contains the raw 8-K fillings for all 4 quaters in 2018, is used for entity extraction.
