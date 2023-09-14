from transformers import pipeline
import pandas as pd
sentiment_pipeline = pipeline("sentiment-analysis")
df_combined = pd.read_csv('df_combined_E4b.csv')
df_combined['BERT_sentiment'] = df_combined['review_text'].apply(lambda x:sentiment_pipeline(x))
print(df_combined)
df_combined.to_csv('BERT_results.csv')