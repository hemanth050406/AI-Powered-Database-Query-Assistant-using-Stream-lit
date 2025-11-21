import sqlite3
import pandas as pd # type: ignore

#Connectt to SQlite
# Step 1: Connect to SQLite database (or create one if not exists)
connection=sqlite3.connect("visa_database.db")

#step 2: Reading the bank dataset
df=pd.read_csv('visadataset.csv')

# step 3: Create a cursor object to insert record,create table
cursor=connection.cursor()

# Step 4: Store the DataFrame in a SQL table called "isa_approval"
df.to_sql('visa_approval', connection, if_exists='replace', index=False)

# Step 5: Confirm storage
print("visa dataset stored successfully in SQLite database.")

# Step 6: Read back the data to confirm
stored_df = pd.read_sql("SELECT * FROM visa_approval", connection)
print(stored_df)

#Disspaly ALl the records
for row in stored_df:
    print(row)

#Commit your changes int he databse
connection.commit()
connection.close()