def delete_ignore_columns(airport_df, glossary_df):
  def lower_str(x):
    if type(x) is str:
      return x.lower()
    return x

  glossary_df = glossary_df.apply(
    lambda x: x.apply(
        lambda x: lower_str(x)
    ),
    axis=1
  )
  glossary_df["English"] = glossary_df["English"].apply(
      lambda x: str(x).replace(" ", "")
  )
  
  original_cols = airport_df.columns
  airport_df.columns = [s.lower() for s in airport_df.columns]
  dict_cols = dict(zip(list(airport_df.columns), list(original_cols)))
  
  col_to_del = list(glossary_df['English'][glossary_df['Meaning'].apply(lambda x: 'to ignore' in x)])
  col_to_del = list(set(col_to_del).intersection(set(airport_df.columns)))
  
  airport_df = airport_df.drop(columns=col_to_del)
  print(dict_cols)
  airport_df.columns = [dict_cols[s] for s in airport_df.columns]
  return airport_df