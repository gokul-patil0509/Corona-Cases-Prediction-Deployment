import pandas as pd
import numpy as np
import pickle


## ____ MODEL NO. 1 ____ ##

### Loading the dataset
df = pd.read_csv('Countries_wise.csv')


# Keeping only consistent country
consistent_country =['Afghanistan', 'Argentina', 'Australia', 'Bangladesh', 'Bhutan', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'India',
                     'Indonesia', 'Iran', 'Ireland', 'Israel', 'Italy', 'Japan', 'Kenya', 'Mexico', 'Nepal', 'Netherlands', 'New Zealand', 'Pakistan', 
                     'Russia', 'Saudi Arabia', 'Singapore', 'South Africa', 'Spain', 'Sri Lanka', 'Switzerland', 'Thailand', 'Turkey', 'US',
                     'United Kingdom', 'Zimbabwe']

df = df[(df['Country'].isin(consistent_country))]

# --- Data Preprocessing ---
# Converting categorical features using OneHotEncoding method
encoded_df = pd.get_dummies(data=df, columns=['Country', 'Current_Status'])


# Rearranging the columns
encoded_df = encoded_df[['Country_Afghanistan', 'Country_Argentina', 'Country_Australia', 'Country_Bangladesh', 'Country_Bhutan', 'Country_Brazil', 'Country_Canada', 'Country_China',
                         'Country_France', 'Country_Germany', 'Country_India', 'Country_Indonesia', 'Country_Iran', 'Country_Ireland', 'Country_Israel', 'Country_Italy', 'Country_Japan', 'Country_Kenya',
                         'Country_Mexico', 'Country_Nepal', 'Country_Netherlands', 'Country_New Zealand', 'Country_Pakistan', 'Country_Russia', 'Country_Saudi Arabia', 'Country_Singapore', 'Country_South Africa',
                         'Country_Spain', 'Country_Sri Lanka', 'Country_Switzerland', 'Country_Thailand', 'Country_Turkey', 'Country_US', 'Country_United Kingdom', 'Country_Zimbabwe',
                         'Current_Status_Confirmed', 'Current_Status_Active', 'Current_Status_Recovered', 'Current_Status_Deaths', 'Day', 'Month', 'Year', 'Total_Cases']]


# Splitting the data into train and test set
X = encoded_df.drop(labels='Total_Cases', axis=1)
y = encoded_df['Total_Cases'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)


# Random Forest Regression Model
from sklearn.ensemble import RandomForestRegressor
country_regressor = RandomForestRegressor()
country_regressor.fit(X_train,y_train)


# Creating a pickle file for the classifier
filename = 'countries_wise-upcoming-cases-rfr-model.pkl'
pickle.dump(country_regressor, open(filename, 'wb'))




## ____ MODEL NO. 2 ____ ##

### Loading the dataset
df = pd.read_csv('Statewise_Dataset.csv')

# Keeping only consistent state
consistent_state = ['Kerala', 'Delhi', 'Telangana', 'Rajasthan', 'Haryana', 'Uttar Pradesh', 'Ladakh', 'Tamil Nadu', 'Jammu and Kashmir',
                    'Karnataka', 'Maharashtra', 'Punjab', 'Andhra Pradesh', 'Uttarakhand', 'Odisha', 'West Bengal', 'Chandigarh',
                    'Chhattisgarh', 'Gujarat', 'Madhya Pradesh', 'Bihar', 'Mizoram', 'Goa', 'Andaman and Nicobar Islands', 'Jharkhand']
                    


df = df[(df['Detected State'].isin(consistent_state))]

# --- Data Preprocessing ---
# Converting categorical features using OneHotEncoding method
encoded_df = pd.get_dummies(data=df, columns=['Detected State', 'Current Status'])


# Rearranging the columns
encoded_df = encoded_df[['Detected State_Kerala', 'Detected State_Delhi', 'Detected State_Telangana', 'Detected State_Rajasthan', 'Detected State_Haryana', 'Detected State_Uttar Pradesh', 'Detected State_Ladakh', 'Detected State_Tamil Nadu', 'Detected State_Jammu and Kashmir', 'Detected State_Karnataka', 'Detected State_Maharashtra', 'Detected State_Punjab', 'Detected State_Andhra Pradesh',
                         'Detected State_Uttarakhand', 'Detected State_Odisha', 'Detected State_West Bengal', 'Detected State_Chandigarh', 'Detected State_Chhattisgarh', 'Detected State_Gujarat', 'Detected State_Madhya Pradesh', 'Detected State_Bihar', 'Detected State_Mizoram', 'Detected State_Goa', 'Detected State_Andaman and Nicobar Islands', 'Detected State_Jharkhand',
                         'Current Status_Active', 'Current Status_Recovered',  'Current Status_Deceased', 'Day', 'Month', 'Year', 'Num Cases']]


# Splitting the data into train and test set
X_train = encoded_df.drop(labels='Num Cases', axis=1)
y_train = encoded_df['Num Cases'].values


# Random Forest Regression Model
from sklearn.ensemble import RandomForestRegressor
state_regressor = RandomForestRegressor()
state_regressor.fit(X_train,y_train)

# Creating a pickle file for the classifier
filename = 'state-wise-upcoming-cases-rf-model.pkl'
pickle.dump(state_regressor, open(filename, 'wb'))





## ____ MODEL NO. 3 ____ ##


### Loading the dataset
df = pd.read_csv('District_wise_Dataset.csv')

# Keeping only consistent District
consistent_district = ['East Delhi', 'Hyderabad', 'Agra', 'South West Delhi', 'Ghaziabad', 'West Delhi', 'Gurugram', 'Kargil', 'Kolkata', 'Chennai', 'Ratnagiri', 'Srinagar',  'Vadodara', 'Jabalpur', 
                    'Leh', 'Kancheepuram', 'Pathanamthitta', 'North Delhi', 'Jammu', 'North East Delhi', 'Chandigarh', 'Raipur', 'Rajkot', 'Surat',  'Visakhapatnam', 'North West Delhi', 'Ahmedabad',
                    'Bengaluru Urban', 'Kannur', 'Pune', 'Amritsar', 'Ernakulam',  'Varanasi', 'Patna', 'Bhopal', 'Uttara Kannada', 'Jodhpur', 'Palghar', 'Sangli', 'Satara', 'Indore',  'Ludhiana',
                    'Kottayam', 'Jaipur', 'Mumbai', 'Nagpur', 'Ujjain', 'Gwalior', 'Aizawl', 'North Goa', 'South Andaman', 'Sindhudurg', 'North and Middle Andaman', 'Gondia', 'Kolhapur', 'Ajmer',
                    'Lucknow', 'New Delhi', 'Thiruvananthapuram', 'Ambala', 'Jalgaon', 'Buldhana', 'Porbandar', 'Nashik', 'Tiruvannamalai', 'Viluppuram', 'Anantapur', 'Ranchi', 'Kanyakumari', 'Udaipur',
                    'Ahmednagar', 'Thane', 'Raigad', 'Yavatmal', 'Osmanabad',  'Firozabad',  'Patiala', 'Jajpur', 'Amravati', 'Haridwar', 'Mirzapur', 'Latur', 'Bengaluru Rural', 'Nagaur', 'Parbhani', 
                    'Aurangabad', 'Dehradun', 'Malappuram', 'South Delhi', 'Jalna', 'Kota',  'Mathura', 'Rampur', 'Pulwama', 'Akola', 'Khandwa', 'Dhar', 'Beed', 'Sundargarh', 'Vijayapura', 'Kurukshetra', 
                    'Solapur', 'Dhule', 'Chandrapur', 'Gonda']
                    
df = df[(df['Detected District'].isin(consistent_district))]

# --- Data Preprocessing ---
# Converting categorical features using OneHotEncoding method
encoded_df = pd.get_dummies(data=df, columns=['Detected District', 'Current Status'])


# Rearranging the columns
encoded_df = encoded_df[['Detected District_East Delhi', 'Detected District_Hyderabad', 'Detected District_Agra', 'Detected District_South West Delhi', 'Detected District_Ghaziabad', 'Detected District_West Delhi', 'Detected District_Leh', 'Detected District_Kancheepuram', 'Detected District_Pathanamthitta', 'Detected District_North Delhi', 'Detected District_Jammu',
                         'Detected District_Bengaluru Urban', 'Detected District_Kannur', 'Detected District_Pune', 'Detected District_Amritsar', 'Detected District_Ernakulam', 'Detected District_Kottayam', 'Detected District_Jaipur', 'Detected District_Mumbai', 'Detected District_Nagpur', 'Detected District_Lucknow', 'Detected District_New Delhi', 'Detected District_Thiruvananthapuram',
                         'Detected District_Ahmednagar', 'Detected District_Thane', 'Detected District_Raigad', 'Detected District_Yavatmal', 'Detected District_Aurangabad', 'Detected District_Dehradun', 'Detected District_Malappuram', 'Detected District_South Delhi', 'Detected District_Gurugram', 'Detected District_Kargil', 'Detected District_Kolkata', 'Detected District_Chennai',
                         'Detected District_Ratnagiri', 'Detected District_Srinagar', 'Detected District_North East Delhi', 'Detected District_Chandigarh', 'Detected District_Raipur', 'Detected District_Rajkot', 'Detected District_Surat', 'Detected District_Visakhapatnam', 'Detected District_North West Delhi', 'Detected District_Ahmedabad', 'Detected District_Vadodara',
                         'Detected District_Jabalpur', 'Detected District_Varanasi', 'Detected District_Patna', 'Detected District_Bhopal', 'Detected District_Uttara Kannada', 'Detected District_Jodhpur', 'Detected District_Palghar', 'Detected District_Sangli', 'Detected District_Satara', 'Detected District_Indore', 'Detected District_Ujjain', 'Detected District_Gwalior', 'Detected District_Aizawl',
                         'Detected District_Ludhiana', 'Detected District_North Goa', 'Detected District_South Andaman', 'Detected District_Sindhudurg', 'Detected District_North and Middle Andaman', 'Detected District_Gondia', 'Detected District_Kolhapur', 'Detected District_Ajmer', 'Detected District_Ambala', 'Detected District_Jalgaon',
                         'Detected District_Buldhana', 'Detected District_Porbandar', 'Detected District_Nashik', 'Detected District_Tiruvannamalai', 'Detected District_Viluppuram', 'Detected District_Anantapur', 'Detected District_Ranchi', 'Detected District_Kanyakumari', 'Detected District_Udaipur', 'Detected District_Osmanabad', 'Detected District_Firozabad', 'Detected District_Patiala',
                         'Detected District_Jajpur', 'Detected District_Amravati', 'Detected District_Haridwar', 'Detected District_Mirzapur', 'Detected District_Latur', 'Detected District_Bengaluru Rural', 'Detected District_Nagaur', 'Detected District_Jalna', 'Detected District_Kota', 'Detected District_Mathura', 'Detected District_Parbhani', 'Detected District_Rampur', 'Detected District_Pulwama', 'Detected District_Akola',
                         'Detected District_Khandwa', 'Detected District_Dhar', 'Detected District_Beed', 'Detected District_Sundargarh', 'Detected District_Vijayapura', 'Detected District_Kurukshetra', 'Detected District_Solapur', 'Detected District_Dhule', 'Detected District_Chandrapur', 'Detected District_Gonda',
                         'Current Status_Confirmed', 'Current Status_Recovered', 'Current Status_Deceased', 'Day', 'Month', 'Year', 'Num Cases']]


# Splitting the data into train and test set
X_train = encoded_df.drop(labels='Num Cases', axis=1)
y_train = encoded_df['Num Cases'].values


# Random Forest Regression Model
from sklearn.ensemble import RandomForestRegressor
district_regressor = RandomForestRegressor()
district_regressor.fit(X_train,y_train)

# Creating a pickle file for the classifier
filename = 'district-wise-upcoming-cases-rf-model.pkl'
pickle.dump(district_regressor, open(filename, 'wb'))





## ____ MODEL NO.4 ____ ##


### Loading the dataset
df = pd.read_csv('COVID-19 Symptoms.csv')


# --- Data Preprocessing ---
# Arrange columns in below order
df = df[['Corona result', 'age', 'Gender', 'body temperature', 'Dry_Cough', 'sour_throat', 'weakness', 'breathing_problem', 'pain in chest',
         'in contact to infected people', 'diabetes', 'heart_disease', 'lung_disease', 'high blood pressue', 'kidney_disease']]

# Renaming pain in chest as PIC , in contact to infected people as ICTIP and high blood pressue as HBP
df = df.rename(columns={'pain in chest':'PIC', 'in contact to infected people':'ICTIP', 'high blood pressue':'HBP'})

# Converting categorical features using OneHotEncoding method
df = pd.get_dummies(df,drop_first=True)

# independent and dependent features
X = df.iloc[:,1:]
y = df.iloc[:,0]

# Splitting the data into train and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state=0)

# --- Model Building ---
# Random Forest Classifier Model
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20)
classifier.fit(X_train, y_train)

# Creating a pickle file for the classifier
filename = 'novel-corona-virus-prediction-rfc-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))
