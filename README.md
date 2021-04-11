# Cryptocurrecny_data_pipeline
-developed an ETL pipeline that extracts data from the top 10 (at time of development) cryptocurrencies utilizing the CoinLore API 

-loaded data into a MySql database on a local linux system

-scheduled pipeline to extract data daily with cron

The tables in the database are as follows:

![tables](https://user-images.githubusercontent.com/28849195/114291289-3b6f1c80-9a54-11eb-8326-2a023732031e.png)

The bitcoin table schema looks as follows (The other tables follow this schema aswell) :
![bitcoin_table](https://user-images.githubusercontent.com/28849195/114291301-56419100-9a54-11eb-82b9-f65117e6f95c.png)
