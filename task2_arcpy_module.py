# # utf-8

# # Lage samme kart som i Powerpoint 


# # 1. importer arcpy modul
# import  # ...
# import pandas as pd

# # 2. Last ned fra github

# old_points =  # ...
# new_points =  # ...
# place_names =  # ...

# # Tips: bruk .ipynb i tillegg .py fil for å inspisere data 

# # 3. Sjekk ut data 
# df_old = pd.read_csv(old_points)
# #print(df_old.head())

# df_new = # ...

# # 4. Samle data i én DataFrame 
# df_concat = # ...


# # 5. Join på ID-felt 


# # 6. "Vask" data. X_DMS og Y_DMS må være numerisk for å bruke arcpy.management.XYTableToPoint. 
# # konverter til floats
# print(df.dtypes)

# # 7. Skriv df til CSV som vi kan bruke i arcpy.management.XYTableToPoint
# df.to_csv(r'path\to\result_table.csv')

# # 8. Bruk arcpy.management.XYTableToPoint

# print("Ferdig :) ")
