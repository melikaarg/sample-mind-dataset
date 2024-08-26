import json

import pandas as pd
import csv

mode = "test"
behavior_path = ("/home/melika/Documents/code/news-recommendation-v1/sampleDataset" + f"/{mode}/behaviors.tsv")
news_path = ("/home/melika/Documents/code/news-recommendation-v1/sampleDataset" + f"/{mode}/news.tsv")

output_behavior_path = ("/home/melika/Documents/code/news-recommendation-v1/sampleDataset" + "/behaviors.tsv")
output_news_path = ("/home/melika/Documents/code/news-recommendation-v1/sampleDataset" + "/news.tsv")

df_bahavior = pd.read_csv(behavior_path, sep="\t", index_col=0, header=None)
df_news = pd.read_csv(news_path, sep="\t", index_col=0, header=None)

# df_bahavior_sample = df_bahavior.sample(n=10, replace=False, random_state=1)
df_bahavior_sample = df_bahavior.sample(n=10, replace=False, random_state=12)

news = []

# df_news[3] = df_news[3].map(lambda x: x.replace("'", ""))
# df_news[3] = df_news[3].map(lambda x: x.replace("\"", ""))
# df_news[4] = df_news[4].map(lambda x: str(x).replace("'", ""))
# df_news[4] = df_news[4].map(lambda x: str(x).replace("\"", ""))
# df_news[3] = df_news[3].map(lambda x: x.replace("'", "").replace("\"", ""))
# df_news[4] = df_news[4].map(lambda x: str(x).replace("'", "").replace("\"", ""))


print(df_news.head(10))

for index, row in df_bahavior_sample.iterrows():
    if type(row[2]) == str:
        for item in str.split(row[2], " "):
            news.append(item)
    if type(row[3]) == str:
        for item in str.split(row[3], " "):
            behavior = str.split(item, "-")
            news.append(behavior[0])

print(len(news))
df_news_sample = df_news[df_news.index.isin(news)]
print(df_news_sample.head(10))


def escape_special_chars(value):
    if isinstance(value, str):
        return value.replace('"', '\\"')
    return value

#
# df_news_sample.loc[:, 6] = df_news_sample.loc[:, 6].apply(escape_special_chars)
# df_news_sample.loc[:, 7] = df_news_sample.loc[:, 7].apply(escape_special_chars)
# df_news_sample.loc[:, 6] = df_news_sample.loc[:, 6].map(lambda x: str(x).replace("'", ''))
# df_news_sample.loc[:, 7] = df_news_sample.loc[:, 7].map(lambda x: str(x).replace("'", ''))
# df_news_sample.loc[:, 7] = df_news_sample.loc[:, 7].map(lambda x: json.dumps(x))

print(df_news_sample.head(10))
# Save the filtered DataFrame to a TSV file
#
#
df_news_sample.to_csv(output_news_path, sep='\t', index=True, header=False, quoting=csv.QUOTE_NONE)
df_bahavior_sample.to_csv(output_behavior_path, sep='\t', index=True, header=False)
#
