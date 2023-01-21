import autodatadictionary as ad

# ad.to_dictionary_from_db(
#      sql_alchemy_connection_string='postgresql://phil:sokoro.phil@localhost:5432/cpims',
#      schema='schema')

# import csv

# # Get the dictionary from the database
# dictionary = ad.to_dictionary_from_db(sql_alchemy_connection_string='postgresql://phil:sokoro.phil@localhost:5432/cpims',
#                                      schema='schema')

# # Open a file for writing
# with open('database_dictionary.csv', 'w', newline='') as csvfile:
#     # Create a CSV writer
#     writer = csv.DictWriter(csvfile, fieldnames=['Table Name', 'Column Name', 'Data Type'])

#     # Write the header row
#     writer.writeheader()

#     # Write the data rows
#     for table_name, columns in dictionary.items():
#         for column in columns:
#             writer.writerow({'Table Name': table_name, 'Column Name': column['name'], 'Data Type': column['type']})


# import csv
# import sqlalchemy

# # Connect to the database
# engine = sqlalchemy.create_engine('postgresql://phil:sokoro.phil@localhost:5432/cpims')

# # Get a list of all table names
# table_names = engine.table_names()

# # Open a file for writing
# with open('database_dictionary.csv', 'w', newline='') as csvfile:
#     # Create a CSV writer
#     fieldnames = ['Table Name', 'Column Name', 'Data Type']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     # Write the header row
#     writer.writeheader()

#     # Get the information for each table
#     for table_name in table_names:
#         # Get the table's metadata
#         metadata = sqlalchemy.MetaData(bind=engine, reflect=True)
#         table = sqlalchemy.Table(table_name, metadata, autoload=True)

#         # Write the information for each column in the table
#         for column in table.columns:
#             writer.writerow({'Table Name': table_name, 'Column Name': column.name, 'Data Type': column.type})


import csv
import sqlalchemy

# Connect to the database
engine = sqlalchemy.create_engine('postgresql://phil:sokoro.phil@localhost:5432/cpims')

# Get a list of all table names
table_names = engine.table_names()

# Open a file for writing
with open('data_dictionary.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    fieldnames = ['Table Name', 'Column Name', 'Data Type', 'Primary Key', 'Nullable', 'Default Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Get the information for each table
    for table_name in table_names:
        # Get the table's metadata
        metadata = sqlalchemy.MetaData(bind=engine, reflect=True)
        table = sqlalchemy.Table(table_name, metadata, autoload=True)

        # Write the information for each column in the table
        for column in table.columns:
            writer.writerow({'Table Name': table_name, 
                             'Column Name': column.name, 
                             'Data Type': column.type,
                             'Primary Key': column.primary_key,
                             'Nullable': column.nullable,
                             'Default Value': column.server_default
                            })
