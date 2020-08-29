from io import StringIO
import pandas as pd
import datacompy

# you can use this library to compare 2 tables completely which can reside in different databases

# Details and other comparison methods: https://capitalone.github.io/datacompy/pandas_usage.html


data1 = """acct_id,dollar_amt,name,float_fld,date_fld
10000001234,123.45,George Maharis,14530.1555,2017-01-01
10000001235,0.45,Michael Bluth,1,2017-01-01
10000001236,1345,George Bluth,,2017-01-01
10000001237,123456,Bob Loblaw,345.12,2017-01-01
10000001239,1.05,Lucille Bluth,,2017-01-01
"""

data2 = """acct_id,dollar_amt,name,float_fld
10000001234,123.4,George Michael Bluth,14530.155
10000001235,0.45,Michael Bluth,
10000001236,1345,George Bluth,1
10000001237,123456,Robert Loblaw,345.12
10000001238,1.05,Loose Seal Bluth,111
"""

df1 = pd.read_csv(StringIO(data1))
df2 = pd.read_csv(StringIO(data2))

compare = datacompy.Compare(
    df1,
    df2,
    join_columns='acct_id',  #You can also specify a list of columns
    abs_tol=0, #Optional, defaults to 0
    rel_tol=0, #Optional, defaults to 0
    df1_name='Original', #Optional, defaults to 'df1'
    df2_name='New' #Optional, defaults to 'df2'
    )
compare.matches(ignore_extra_columns=False)

# compare = datacompy.Compare(df1, df2, join_columns=['acct_id', 'name'])
# compare = datacompy.Compare(df1, df2, on_index=True)

# This method prints out a human-readable report summarizing and sampling differences
print(compare.report())