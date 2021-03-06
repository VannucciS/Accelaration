### How to handle large amount of data ###
# read the large csv file with specified chunksize 
df_chunk = pd.read_csv(r'../input/data.csv', chunksize=1000000)

chunk_list = []  # append each chunk df here 

# Each chunk is in df format
for chunk in df_chunk:  
    # perform data filtering 
    chunk_filter = chunk_preprocessing(chunk)
    
    # Once the data filtering is done, append the chunk to list
    chunk_list.append(chunk_filter)
    
# concat the list into dataframe 
df_concat = pd.concat(chunk_list)

# Filter out unimportant columns
df = df[['col_1','col_2', 'col_3', 'col_4', 'col_5', 'col_6','col_7', 'col_8', 'col_9', 'col_10']]

# Change the dtypes (int64 -> int32)
# This change save 50% of the memory usage

df[['col_1','col_2', 
    'col_3', 'col_4', 'col_5']] = df[['col_1','col_2', 
                                      'col_3', 'col_4', 'col_5']].astype('int32')

# Change the dtypes (float64 -> float32)
df[['col_6', 'col_7',
    'col_8', 'col_9', 'col_10']] = df[['col_6', 'col_7',
                                       'col_8', 'col_9', 'col_10']].astype('float32')
                                       
 
