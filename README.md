# t20_cricket_analysis
data visualization project for T20 cricket match analysis for selecting playing 11

1. Web scraping using Brightdata:
Raw data collected from Brightdata and generated json files from 
escncrickinfo 

2. Data preparation: 
Includes,
* data cleaning
* removing special characters in players name
* connecting the different tables usign common values in column
* creating modified json files 

3. Data Transformation using power query:
* dim players data transformation includes deleting duplicate entries, removing (c) 
after the name
* dim match summary data transformation
if date < 22 oct then qualifier match
else super 12
* fact bowling summary data transformation includes,
	- renaming column name(0s -> zeros) 
	- replace null with 0 
	- add custom col called balls to measure strike rate
* fact batting summary data transformation includes,
	- removing (c) after the name
	
4. Data Modeling and building parameters using dax:
* Data Modeling creation,
	- dim_players and bowling summary linked with name
	- dim_players and batting summary linked with name
* Create DAX measure -> used to build actual visuals

5. Build the visuals and dashboard in powerbi