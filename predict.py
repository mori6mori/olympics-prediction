import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load the model
def load_model():
    with open('medal_pred_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

predictor = data["model"]

def show_predict_page():
    st.title("Want to test your chances at 2024 Paris Olympics?")
    st.write("""### We need some information to predict your probability to WIN""")
    
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
    age = st.slider("Your Age", 0, 100, 13)
    weight = st.slider("Your Weight (kg)", 0, 300, 20)

    sports = ('Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Speed Skating',
       'Cross Country Skiing', 'Athletics', 'Ice Hockey', 'Swimming',
       'Badminton', 'Sailing', 'Biathlon', 'Gymnastics',
       'Art Competitions', 'Alpine Skiing', 'Handball', 'Weightlifting',
       'Wrestling', 'Luge', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh',
       'Fencing', 'Equestrianism', 'Shooting', 'Boxing', 'Taekwondo',
       'Cycling', 'Diving', 'Canoeing', 'Tennis', 'Modern Pentathlon',
       'Figure Skating', 'Golf', 'Softball', 'Archery', 'Volleyball',
       'Synchronized Swimming', 'Table Tennis', 'Nordic Combined',
       'Baseball', 'Rhythmic Gymnastics', 'Freestyle Skiing',
       'Rugby Sevens', 'Trampolining', 'Beach Volleyball', 'Triathlon',
       'Ski Jumping', 'Curling', 'Snowboarding', 'Rugby',
       'Short Track Speed Skating', 'Skeleton', 'Lacrosse', 'Polo',
       'Cricket', 'Racquets', 'Motorboating', 'Military Ski Patrol',
       'Croquet', 'Jeu De Paume', 'Roque', 'Alpinism', 'Basque Pelota',
       'Aeronautics')

    sport = st.selectbox("Sport", sports)
    
    ok = st.button("Reveal My Chances")
    if ok:
        # Encode the input features
        X = pd.DataFrame([[country, age, weight, sport]], columns=['Country', 'Age', 'Weight', 'Sport'])

        # Define the column transformer
        numeric_features = ['Age', 'Weight']
        numeric_transformer = StandardScaler()

        categorical_features = ['Country', 'Sport']
        categorical_transformer = OneHotEncoder(handle_unknown='ignore')

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)])

        # Fit and transform the input data
        preprocessor.fit(X)
        X_preprocessed = preprocessor.transform(X)

        # Predict the probability
        prob = predictor.predict_proba(X_preprocessed)[:, 1]
        
        st.subheader(f"The estimated probability of winning is {prob[0]:.2f}")

