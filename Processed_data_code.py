import pandas as pd
raw_data = pd.read_csv(r"E:\Self-study\Online course\Udemy\Business Intelligence Analyst\S47 _ Integration - Data processing\Absenteeism_data.csv")
processed_data = raw_data.copy()

#Setting display options:
pd.set_option('max_rows',10,'max_columns',None)

#Drop ID column from the dataframe
processed_data = processed_data.drop('ID', axis = 1)
#print(processed_data)

#Group reason for absence into 4 different groups, drop reason 0 from the list
processed_data['Reason for Absence'] = processed_data['Reason for Absence'].replace(range(1,15),1)
processed_data['Reason for Absence'] = processed_data['Reason for Absence'].replace(range(15,18),2)
processed_data['Reason for Absence'] = processed_data['Reason for Absence'].replace(range(18,22),3)
processed_data['Reason for Absence'] = processed_data['Reason for Absence'].replace(range(22,29),4)

#Create dummies columns for ['Reason for Absence'] column
reason = pd.get_dummies(processed_data['Reason for Absence'])

#Merge reason and processed_data together to create a new dataframe, drop the reason 0 column
processed_data = pd.concat([reason.drop(0, axis = 1),processed_data],axis = 1)

#Rename columns 1,2,3,,4 and rop column 'Reason for Absence'
processed_data = processed_data.rename(columns = {1:'Reason_1', 2:'Reason_2', 3:'Reason_3', 4:'Reason_4'})
processed_data = processed_data.drop('Reason for Absence', axis = 1)

#Extract month and day of the week into 2 different columns from 'Date' column
#Drop the 'Date' column
processed_data['Date'] = pd.to_datetime(processed_data['Date'], format = '%d/%m/%Y')
processed_data['Month'] = processed_data['Date'].dt.month
processed_data['Day_of_the_week'] = processed_data['Date'].dt.dayofweek
processed_data = processed_data.drop('Date', axis = 1)

#Change the value of 'Education' column from 1 to 0, 2 / 3 / 4 to 1
processed_data['Education'] = processed_data['Education'].map({1:0, 2:1, 3:1, 4:1})

#Reorder column in processed_data dataframe
new_order = ['Reason_1' , 'Reason_2' , 'Reason_3' , 'Reason_4' ,'Month','Day_of_the_week', 'Transportation Expense','Distance to Work', 'Age' ,'Daily Work Load Average' ,'Body Mass Index','Education' ,'Children' ,'Pets' ,'Absenteeism Time in Hours']
processed_data = processed_data[new_order]

#print dataframe for result confirmation
print(processed_data)
