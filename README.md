# Cryptocurrecny_data_pipeline
-developed an ETL pipeline that extracts data from the top 10 (at time of development) cryptocurrencies utilizing the CoinLore API 

-loaded data into a MySql database on a local linux system

-scheduled pipeline to extract data daily with cron

The tables in the database are as follows:

![tables](https://user-images.githubusercontent.com/28849195/114291289-3b6f1c80-9a54-11eb-8326-2a023732031e.png)

Here is an example schema for the bitcoin table which is also identical to the 9 other tables:
![bitcoin_table](https://user-images.githubusercontent.com/28849195/114291301-56419100-9a54-11eb-82b9-f65117e6f95c.png)
