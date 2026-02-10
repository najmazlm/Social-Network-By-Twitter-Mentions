
import pandas as pd

# Misalkan Anda telah memuat DataFrame Anda, atau Anda dapat menggantinya dengan cara yang sesuai
df = pd.read_excel("theerastour1.xlsx")
df

# Drop duplicates based on 'text_column'
df_no_duplicates = df.drop_duplicates(subset='full_text')

# Display the result
df_no_duplicates

# Mencari baris yang berisi mention (@)
mention_condition = df_no_duplicates['full_text'].str.contains('@', case=False)  # case=False untuk memperlakukan huruf besar dan kecil sama

# Membuat DataFrame baru hanya dengan baris yang memenuhi kondisi mention
df_with_mention = df_no_duplicates[mention_condition]
df_with_mention

def onlyMention(text):
  words = text.split()
  Mentions = [word for word in words if '@' in word]
  return ' '.join(Mentions)

#df = pd.read_excel('eras only mention.xlsx')
df_with_mention['full_text'] = df_with_mention['full_text'].apply(onlyMention)
df_with_mention
#df_with_mention.to_excel('eras mention.xlsx')

import pandas as pd

# Assuming df is your DataFrame and 'full_text' is the column containing text
df = pd.read_excel("eras mention3.xlsx")

# Define a function to split the text into separate cells
def split_text(text):
    return text.split()

# Apply the split_text function to the 'full_text' column
split_words = df['full_text'].apply(split_text)

# Create a new DataFrame with the separate words and the index of the original DataFrame
new_df = pd.DataFrame(split_words.tolist(), index=split_words.index).stack().reset_index(level=1, drop=True)

# Concatenate the original DataFrame with the new DataFrame
df_split = pd.concat([df.drop('full_text', axis=1), new_df], axis=1)


# Display the result
df_split
#df_split.to_excel('mention theeras.xlsx')

df = pd.read_excel("mention theeras clean.xlsx")

# Remove the @ symbol from the 'text_column'
df['mention'] = df['mention'].replace('@', '', regex=True)
df
df.to_excel('mention theeras clean2.xlsx')
