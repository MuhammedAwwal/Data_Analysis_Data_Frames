import pandas as pd
user_cols = ['user_id', 'age', 'gender', 'occupation', 'Zip_code']    
users = pd.read_table ('http://bit.ly/movieusers' , sep = '|',
                       header = None, names = user_cols)
