import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    # Same data inside code
    data = pd.DataFrame({
        'time': [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],
        'day': ['Monday','Monday','Monday','Monday','Monday',
                'Tuesday','Tuesday','Wednesday','Wednesday',
                'Thursday','Thursday','Friday','Friday',
                'Saturday','Sunday'],
        'vehicles': [120,200,250,300,280,260,270,290,320,350,400,420,380,300,200],
        'weather': ['Clear','Clear','Cloudy','Clear','Clear',
                    'Rain','Cloudy','Clear','Clear',
                    'Rain','Rain','Clear','Cloudy','Clear','Clear']
    })

    # Convert categorical to numeric
    data['day'] = data['day'].astype('category').cat.codes
    data['weather'] = data['weather'].astype('category').cat.codes

    X = data[['time', 'day', 'weather']]
    y = data['vehicles']

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_traffic(model, time, day, weather):
    return model.predict([[time, day, weather]])
