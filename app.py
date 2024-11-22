import streamlit as st
import datetime
import requests
# from colorama import Fore, Style

'''
# Estimation des courses de Taxi
'''

st.markdown('''
_Insérer les informations sur votre course_''')

# print(Fore.BLUE + "Preprocessing features..." + Style.RESET_ALL)

estimated_fare=0

with st.form("my_form"):

    '''
    Pick Up
    '''
    columns = st.columns(2)
    pickup_longitude = columns[0].text_input('Longitude', '-74.086173')
    pickup_latitude = columns[1].text_input('Latitude', '40.716279')

    '''
    Drop Off
    '''
    columns2 = st.columns(2)
    dropoff_longitude = columns2[0].text_input('Longitude', '-74.269507')
    dropoff_latitude = columns2[1].text_input('Latitude', '40.687192')

    '''
    Horaire
    '''
    columns3 = st.columns(2)
    date = columns3[0].date_input(
            "Date",
            datetime.date(2024, 11, 27))
    time = columns3[1].time_input('Heure', datetime.time(8, 45))


    # mytime = dt.datetime.strptime('0130','%H%M').time()
    pickup_datetime = datetime.datetime.combine(date, time)

    passenger_count = st.number_input(label= 'Nbr de passagers:',
                                min_value=1,
                                max_value=6,
                                value=1,
                                step=1)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Evaluation")

    if submitted:
        url = 'https://taxifare.lewagon.ai/predict'

        params = { 'pickup_datetime' : pickup_datetime,
                    'pickup_longitude': pickup_longitude,
                    'pickup_latitude': pickup_latitude,
                    'dropoff_longitude' : dropoff_longitude,
                    'dropoff_latitude' : dropoff_latitude,
                    'passenger_count' : passenger_count }

        response = requests.get(url, params=params)
        response.json()

        estimated_fare = round(response.json()['fare'],2)

'''
## Estimation
_cliquer sur "Evaluation"_
'''

if estimated_fare!=0:
    st.metric(label = "Tarif estimé en $", value = estimated_fare)
st.write('Pick Up Time:', date ,":",time, "pour", passenger_count,"passager(s)")

st.write('Pick up:', pickup_longitude,"/", pickup_latitude)
st.write('Drop Off:', dropoff_longitude,"/", dropoff_latitude)
