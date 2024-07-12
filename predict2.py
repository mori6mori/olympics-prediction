import streamlit as st
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb

def load_model():
    with open('medal_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
scaler = data["scaler"]
le_sex = data["le_sex"]
le_sport = data["le_sport"]
le_country = data["le_country"]

def show_predict_page():
    st.title("Olympic Medal Prediction")

    st.write("""### We need some information to predict your chance of winning an Olympic medal!""")
    st.write(le_sport.transform('Canoeing'))
    #sports = le_sport.classes_
    #countries = le_country.classes_

    sports = (
        "Athletics", "Swimming", "Gymnastics", "Cycling", "Wrestling", "Boxing", "Basketball", 
        "Football", "Tennis", "Rowing", "Fencing", "Equestrian", "Weightlifting", "Shooting", 
        "Archery", "Judo", "Canoeing", "Sailing", "Diving", "Hockey", "Volleyball", 
        "Handball", "Table Tennis", "Badminton", "Taekwondo", "Triathlon", "Water Polo"
    )
    
    countries = ('China', 'Denmark', 'Netherlands', 'USA', 'Finland', 'Norway',
       'Romania', 'Estonia', 'France', 'Morocco', 'Spain', 'Egypt',
       'Iran', 'Bulgaria', 'Italy', 'Chad', 'Azerbaijan', 'Sudan',
       'Russia', 'Argentina', 'Cuba', 'Belarus', 'Greece', 'Cameroon',
       'Turkey', 'Chile', 'Mexico', 'Nicaragua', 'Hungary', 'Nigeria',
       'Algeria', 'Kuwait', 'Bahrain', 'Pakistan', 'Iraq', 'Syria',
       'Lebanon', 'Qatar', 'Malaysia', 'Germany', 'Canada', 'Ireland',
       'Australia', 'South Africa', 'Eritrea', 'Tanzania', 'Jordan',
       'Tunisia', 'Libya', 'Belgium', 'Djibouti', 'Palestine', 'Comoros',
       'Kazakhstan', 'Brunei', 'India', 'Saudi Arabia', 'Maldives',
       'Ethiopia', 'United Arab Emirates', 'Yemen', 'Indonesia',
       'Philippines', 'Singapore', 'Uzbekistan', 'Kyrgyzstan',
       'Tajikistan', 'Japan', 'Republic of Congo', 'Switzerland',
       'Brazil', 'Monaco', 'Israel', 'Uruguay', 'Sweden',
       'Virgin Islands, US', 'Sri Lanka', 'Armenia', 'Ivory Coast',
       'Kenya', 'Benin', 'Ukraine', 'UK', 'Ghana', 'Somalia', 'Latvia',
       'Niger', 'Mali', 'Afghanistan', 'Poland', 'Costa Rica', 'Panama',
       'Georgia', 'Slovenia', 'Croatia', 'Guyana', 'New Zealand',
       'Portugal', 'Paraguay', 'Angola', 'Venezuela', 'Colombia',
       'Bangladesh', 'Peru', 'El Salvador', 'Puerto Rico', 'Uganda',
       'Honduras', 'Ecuador', 'Turkmenistan', 'Mauritius', 'Seychelles',
       'Czech Republic', 'Luxembourg', 'Mauritania', 'Saint Kitts',
       'Trinidad', 'Dominican Republic', 'Saint Vincent', 'Jamaica',
       'Liberia', 'Suriname', 'Nepal', 'Mongolia', 'Austria', 'Palau',
       'Lithuania', 'Togo', 'Namibia', 'Curacao', 'Iceland',
       'American Samoa', 'Samoa', 'Rwanda', 'Dominica', 'Haiti', 'Malta',
       'Cyprus', 'Guinea', 'Belize', 'South Korea', 'Thailand', 'Bermuda',
       'Serbia', 'Sierra Leone', 'Papua New Guinea',
       'Individual Olympic Athletes', 'Oman', 'Fiji', 'Vanuatu',
       'Moldova', 'Bahamas', 'Guatemala', 'Virgin Islands, British',
       'Mozambique', 'Central African Republic', 'Madagascar',
       'Bosnia and Herzegovina', 'Guam', 'Cayman Islands', 'Slovakia',
       'Barbados', 'Guinea-Bissau', 'Timor-Leste',
       'Democratic Republic of the Congo', 'Gabon', 'San Marino', 'Laos',
       'Botswana', 'Refugee Olympic Athletes', 'Cambodia', 'North Korea',
       'Solomon Islands', 'Senegal', 'Cape Verde', 'Equatorial Guinea',
       'Bolivia', 'Andorra', 'Antigua', 'Zimbabwe', 'Grenada',
       'Saint Lucia', 'Micronesia', 'Myanmar', 'Malawi', 'Zambia',
       'Taiwan', 'Sao Tome and Principe', 'Macedonia', 'Tonga',
       'Liechtenstein', 'Montenegro', 'Gambia', 'Cook Islands', 'Albania',
       'Swaziland', 'Burkina Faso', 'Burundi', 'Aruba', 'Nauru',
       'Vietnam', 'Bhutan', 'Marshall Islands', 'Kiribati', 'Unknown',
       'Tuvalu', 'Kosovo', 'South Sudan', 'Lesotho')

    
   
    country = st.selectbox("Country", countries)
    sex = ("Male", "Female")

    age = st.slider("Age", 15, 45, 25)
    height = st.slider("Height (cm)", 140, 220, 170)
    weight = st.slider("Weight (kg)", 40, 150, 70)
    sport = st.selectbox("Sport", sports)
    year = st.slider("Year", 1964, 2022, 1964)
    sex = st.selectbox("Sex", sex)

    ok = st.button("Predict my chances")
    if ok:
        
        sex_value = 1 if sex == "Male" else 0
        
        input_data = {
            'Age': age,
            'Height': height,
            'Weight': weight,
            'Year': year,  # Added Year to input data
            'Sex': [sex_value],
            'Sport': [sport],
            'Country': [country]
        }
        input_df = pd.DataFrame(input_data)
        
        # input_df['Sex'] = input_df['Sex'].astype(str)
        # st.write(input_df['Sex'])
        input_df['Sport'] = input_df['Sport']
        input_df['Country'] = input_df['Country']

        # Encode categorical variables
        input_df['Sex'] = le_sex.transform(input_df['Sex'])
        input_df['Sport'] = le_sport.transform(input_df['Sport'])
        sport = input_df['Sport']
        st.write(sport)
        input_df['Country'] = le_country.transform(input_df['Country'])

        # Standardize numerical features
        input_df[['Age', 'Height', 'Weight']] = scaler.transform(input_df[['Age', 'Height', 'Weight']])

        # Ensure the input data has the same columns as the training data
        required_columns = ['Age', 'Height', 'Weight', 'Year',  'Sport', 'Sex','Country']
        input_df = input_df[required_columns]

        # Make prediction
        medal_prediction = model.predict(input_df)
        medal_probability = model.predict_proba(input_df)[:, 1]

        st.subheader(f"The predicted medal count is {medal_prediction[0]}")
        st.write(f"Your Probability of winning a medal: {medal_probability[0] * 100:.2f}%")


