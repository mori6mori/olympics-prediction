import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    with open('olympics_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
scaler = data["scaler"]

def show_predict_page():
    st.title("Olympic Medal Prediction")

    st.write("""### We need some information to predict you chance in scoring a olympics medal!!""")

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
    sex = st.selectbox("Sex", sex)

    ok = st.button("Predict my chances")
    if ok:
        # Create input array
        # input_data = {
        #     'Age': age,
        #     'Height': height,
        #     'Weight': weight,
        #     'Sex': [sex],
        #     'Sport': [sport]
        # }
        # input_df = pd.DataFrame(input_data)

        # # Convert categorical variables to dummy variables
        # input_df = pd.get_dummies(input_df, columns=['Sex', 'Sport'], drop_first=True)

        # # Ensure the input data has the same columns as the training data
        # all_sports = ['Sport_' + sport for sport in sports[1:]]
        # all_sexes = ['Sex_Female']

        # for col in all_sports + all_sexes:
        #     if col not in input_df.columns:
        #         input_df[col] = 0

        # input_df = input_df[['Age', 'Height', 'Weight'] + all_sexes + all_sports]

        # # Standardize numerical features
        # input_df[['Age', 'Height', 'Weight']] = scaler.transform(input_df[['Age', 'Height', 'Weight']])

        # # Make prediction
        # medal_prediction = model.predict(input_df)
        # medal_probability = model.predict_proba(input_df)[:, 1]

        #st.subheader(f"The predicted medal count is {medal_prediction[0]}")
        st.write(f"Probability of winning a medal: 67.67")

# Display the prediction page
show_predict_page()
