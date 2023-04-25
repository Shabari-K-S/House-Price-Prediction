import streamlit as st 
import bz2file as bz
import pickle as pkl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='House Price Prection',page_icon='icons/house.png',layout='wide',)

df = pd.read_csv("house_price.csv")
df.head()

df['Location'] = df['Location'].map({ 'Bommanahalli' : 1, 'Whitefield' : 2})

y = df['Price']
y.head()

x = df.drop(['Price'], axis=1)
x.head()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)

from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(x_train,y_train)



with st.sidebar:
    st.empty()


style ="""
<h1 style='text-align: center;' class='house-price'>
    <span style='color:#0f7ab0;'>
            House Price
    </span>
         Prediction
</h1>

"""



c1,c2,c3 = st.columns([2,3,2])
with c2:
    st.markdown(f"{style}", unsafe_allow_html=True)
    st.write("###")
    location = st.selectbox(label='Select your location : ',options=['Salem', 'Chennai'])
    st.write("###")
    c4,c5,c6 = st.columns([2,1,2])
    with c4:
        bhk = st.number_input("Enter your BHK:",min_value=0,max_value=3)
    
    with c6:
        Furnishing = st.radio("Are you Furnishing ?",('Yes','No'))
    
    st.write("###")

    sqft= st.slider("Enter the value of the Sq.ft :",min_value=700,max_value=4000)

    old = st.number_input("Enter how many year old the place is:",min_value=0 ,max_value=70)

    floor = st.number_input("Enter how many Floor:",min_value=0,max_value=13)


    if st.button(" Submit "):
        if location == None or bhk == 0 or Furnishing == None or sqft == None or old == 0 or floor == None:
            st.warning("Plese fill the nessacery detail...")
        else:
            if (location == 'Salem'):
                ltn = 1
            elif (location == 'Chennai'):
                ltn = 2
            if Furnishing == 'Yes':
                fur = 1
            else:
                fur = 0
            
            data = pd.DataFrame(
                {
                    'Location':[ltn],
                    'BHK':[bhk],
                    'Furnishing':[fur],
                    'Sq.ft':[sqft],
                    'Old(years)':[old],
                    'Floor':[floor]
                    }
                )

            price = knn.predict(data)

            
            st.subheader("The price of the land is {} Rupee ".format(price[0]*82.84))