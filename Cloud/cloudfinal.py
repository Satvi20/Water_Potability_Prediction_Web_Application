import numpy as np
import pickle
import streamlit as st

#loading the saved model
# loaded_model = pickle.load(open('D:/Cloud Project/trained_model.sav','rb'))
# loaded_model = pickle.load(open('trained_final.sav','rb'))
loaded_model = pickle.load(open('/app/water_potability_prediction_web_application/Cloud/trained_final.sav','rb'))

#creating a function for prediction

def water_potability_prediction(input_data):
    
    # input_data =(7.7,200.22,17000.234343,7.72345,356.434345,500.32545,10.343434,100.324343,3.5353434)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "The water is not suitable for drinking"
    else:
       return "The water is suitable for drinking"


def main():
    
    # giving a title
    st.title("Water Potability Prediction Web App")
    
    # getting the input data from the user
    
    col1, col2, col3 = st.columns(3)
    with col1:
     ph = st.slider('Value of ph?', 1.4317815547427415, 13.999999999999998, 7.0)
     Chloramines = st.slider('Value of Chloramines?', 1.3908709048851806, 13.127000000000002, 7.0)
     Organic_carbon = st.slider('Value of Organic_carbon?', 2.1999999999999886,27.00670661116601, 15.0)
    with col2:
     Hardness = st.slider("Value of Hardness", 73.4922336890611, 317.33812405558257, 150.0)
     Sulfate = st.slider("Value of Sulfate", 129.00000000000003,481.0306423059972, 250.0)
     Trihalomethanes = st.slider("Value of Trihalomethanes" ,8.577012932983806, 124.0, 65.0)
    with col3:
     Solids = st.slider("Value of Solids" , 320.942611274359,56488.67241273919, 25555.0)
     Conductivity = st.slider("Value of Conductivity" ,201.6197367551575, 753.3426195583046, 455.0)
     Turbidity = st.slider("Value of Turbidity" ,1.45,6.494748555990993, 3.0)
    
    
    # code for Prediction
    testing = ''
    
    # creating a button for prediction
    
    if st.button('Test Result'):
        testing = water_potability_prediction([ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])
        
    st.success(testing)
    
if __name__ =='__main__':
    main()


    
    
    
