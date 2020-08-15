CREATE TABLE video_games (
Rank INT PRIMARY Key, 
Name VarChar,
Platform VarChar,
Year INT,
Genre VarChar,
Publisher Varchar,
NA_Sales Int,
EU_Sales Int,
JP_Sales Int,
Other_Sales Int,
Global_Sales Int,
Mean_Playing_Time Int
);

select * from video_games