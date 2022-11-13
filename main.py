df = pd.read_csv('.../edat_lfse_03.tsv', sep=',|\t')

# rename and remove spaces in column names
df=df.rename(columns = {'geo\\time':'geo'})
for i, col in enumerate(df):
  if col[0].isdigit():
    df=df.rename(columns={col: 'y_'+col.strip()})
  else:
    df=df.rename(columns={col: col.strip()})
  
# convert acronyms of countries
df=df.replace({"geo": acr_to_name})
# covert str into float
for col in df:
  if col in ['sex', 'age', 'unit', 'isced11', 'geo']:
    continue
  df[col] = df[col].map(lambda x: re.findall(r'\d+\.\d+', x)[0] if len(re.findall(r'\d+\.\d+', x))>0 else None)
  
# create connection
conn = sqlite3.connect("EuopeanEducation")

ctypes = ['TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT']
ctypes.extend(['REAL']*30)
cursor = conn.cursor()
cursor.execute(createTableStatement('higher_education', df.columns, ctypes))

# pandas Dataframe to sql
df.to_sql('higher_education', conn, if_exists='replace', index = False)

# graph 1
sql = '''  
SELECT isced11, AVG(y_2021), AVG(y_2020), AVG(y_2019), AVG(y_2018), AVG(y_2017), AVG(y_2016), AVG(y_2015), AVG(y_2014), AVG(y_2013), AVG(y_2012), AVG(y_2011), AVG(y_2010), AVG(y_2009), AVG(y_2008), AVG(y_2007), AVG(y_2006), AVG(y_2005), AVG(y_2004), AVG(y_2003), AVG(y_2002), AVG(y_2001), AVG(y_2000), AVG(y_1999), AVG(y_1998), AVG(y_1997), AVG(y_1996), AVG(y_1995), AVG(y_1994), AVG(y_1993), AVG(y_1992)
FROM higher_education
WHERE isced11!='ED3_4GEN' AND isced11!='ED3_4VOC'
GROUP BY isced11
'''
data = pd.read_sql(sql, conn)
# plot line graph grouped by country
plt.figure(figsize=(10, 5))
for index, row in data.iterrows():
  plt.plot(np.arange(1992, 2022)[::-1], list(row[1:]), linewidth=3, label = row.isced11)

plt.legend()
plt.title("Education in EU by level")
plt.show()

# graph 2
sql = '''  
SELECT age, AVG(y_2021), AVG(y_2020), AVG(y_2019), AVG(y_2018), AVG(y_2017), AVG(y_2016), AVG(y_2015), AVG(y_2014), AVG(y_2013), AVG(y_2012), AVG(y_2011), AVG(y_2010), AVG(y_2009), AVG(y_2008), AVG(y_2007), AVG(y_2006), AVG(y_2005), AVG(y_2004), AVG(y_2003), AVG(y_2002), AVG(y_2001), AVG(y_2000), AVG(y_1999), AVG(y_1998), AVG(y_1997), AVG(y_1996), AVG(y_1995), AVG(y_1994), AVG(y_1993), AVG(y_1992)
FROM higher_education
WHERE isced11='ED5-8' AND isced11!='ED3_4GEN' AND isced11!='ED3_4VOC'

GROUP BY age
'''
data = pd.read_sql(sql, conn)
# plot line graph grouped by country
plt.figure(figsize=(10, 5))
for index, row in data.iterrows():
  plt.plot(np.arange(1992, 2022)[::-1], list(row[1:]), linewidth=3, label = row.age)

plt.legend()
plt.title("Higher Education in EU by age")
plt.show()

# graph 3
sql = '''  
SELECT sex, AVG(y_2021), AVG(y_2020), AVG(y_2019), AVG(y_2018), AVG(y_2017), AVG(y_2016), AVG(y_2015), AVG(y_2014), AVG(y_2013), AVG(y_2012), AVG(y_2011), AVG(y_2010), AVG(y_2009), AVG(y_2008), AVG(y_2007), AVG(y_2006), AVG(y_2005), AVG(y_2004), AVG(y_2003), AVG(y_2002), AVG(y_2001), AVG(y_2000), AVG(y_1999), AVG(y_1998), AVG(y_1997), AVG(y_1996), AVG(y_1995), AVG(y_1994), AVG(y_1993), AVG(y_1992)
FROM higher_education
WHERE isced11='ED5-8' AND isced11!='ED3_4GEN' AND isced11!='ED3_4VOC'
GROUP BY sex

'''
data = pd.read_sql(sql, conn)
# plot line graph grouped by sex
plt.figure(figsize=(10, 5))
for index, row in data.iterrows():
  plt.plot(np.arange(1992, 2022)[::-1], list(row[1:]), linewidth=3, label = row.sex)

plt.legend()
plt.title("Higher Education in EU by sex")
plt.show()
