# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run()
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/t4-Vy4iOU19i8y6E3Px_ww/spacex-dash-app.py"_launch_dash.csv"
python3.11 spacex-dash-app.pyiOU19i8y6E3Px_ww/space
Defaulting to user installation because normal site-packages is not writeable
Collecting pandas
  Downloading pandas-3.0.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
Collecting dash
  Downloading dash-4.1.0-py3-none-any.whl.metadata (11 kB)
Collecting numpy>=1.26.0 (from pandas)
  Downloading numpy-2.4.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: Flask<3.2,>=1.0.4 in /usr/local/lib/python3.11/dist-packages (from dash) (3.1.2)
Requirement already satisfied: Werkzeug<3.2 in /usr/local/lib/python3.11/dist-packages (from dash) (3.1.3)
Collecting plotly>=5.0.0 (from dash)
  Downloading plotly-6.7.0-py3-none-any.whl.metadata (8.6 kB)
Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.11/dist-packages (from dash) (8.7.0)
Requirement already satisfied: typing_extensions>=4.1.1 in /usr/local/lib/python3.11/dist-packages (from dash) (4.15.0)
Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from dash) (2.32.5)
Collecting retrying (from dash)
  Downloading retrying-1.4.2-py3-none-any.whl.metadata (5.5 kB)
Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.11/dist-packages (from dash) (1.6.0)
Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from dash) (80.9.0)
Requirement already satisfied: blinker>=1.9.0 in /usr/local/lib/python3.11/dist-packages (from Flask<3.2,>=1.0.4->dash) (1.9.0)
Requirement already satisfied: click>=8.1.3 in /home/theia/.local/lib/python3.11/site-packages (from Flask<3.2,>=1.0.4->dash) (8.1.8)
Requirement already satisfied: itsdangerous>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from Flask<3.2,>=1.0.4->dash) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.2,>=1.0.4->dash) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in /usr/local/lib/python3.11/dist-packages (from Flask<3.2,>=1.0.4->dash) (3.0.3)
Collecting narwhals>=1.15.1 (from plotly>=5.0.0->dash)
  Downloading narwhals-2.21.0-py3-none-any.whl.metadata (16 kB)
Requirement already satisfied: packaging in /home/theia/.local/lib/python3.11/site-packages (from plotly>=5.0.0->dash) (24.2)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
Requirement already satisfied: zipp>=3.20 in /usr/local/lib/python3.11/dist-packages (from importlib-metadata->dash) (3.23.0)
Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (2025.10.5)
Downloading pandas-3.0.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (11.3 MB)
   ━━━━━━━━━━━━━━━ 11.3/11.3 MB 33.5 MB/s  0:00:00
Downloading dash-4.1.0-py3-none-any.whl (7.2 MB)
   ━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 35.1 MB/s  0:00:00
Downloading numpy-2.4.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
   ━━━━━━━━━━━━━━━ 16.9/16.9 MB 37.1 MB/s  0:00:00
Downloading plotly-6.7.0-py3-none-any.whl (9.9 MB)
   ━━━━━━━━━━━━━━━━━ 9.9/9.9 MB 35.5 MB/s  0:00:00
Downloading narwhals-2.21.0-py3-none-any.whl (451 kB)
Downloading retrying-1.4.2-py3-none-any.whl (10 kB)
Installing collected packages: retrying, numpy, narwhals, plotly, pandas, dash
Successfully installed dash-4.1.0 narwhals-2.21.0 numpy-2.4.4 pandas-3.0.3 plotly-6.7.0 retrying-1.4.2

[notice] A new release of pip is available: 25.3 -> 26.1.1
[notice] To update, run: pip3 install --upgrade pip
--2026-05-13 05:12:36--  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv
Resolving cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)... 169.63.118.104, 169.63.118.104
Connecting to cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)|169.63.118.104|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2476 (2.4K) [text/csv]
Saving to: 'spacex_launch_dash.csv'

spacex_launc 100%   2.42K  --.-KB/s    in 0s      

2026-05-13 05:12:36 (800 MB/s) - 'spacex_launch_dash.csv' saved [2476/2476]

--2026-05-13 05:12:36--  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/t4-Vy4iOU19i8y6E3Px_ww/spacex-dash-app.py
Resolving cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)... 169.63.118.104, 169.63.118.104
Connecting to cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)|169.63.118.104|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2075 (2.0K) [application/x-python]
Saving to: 'spacex-dash-app.py'

spacex-dash- 100%   2.03K  --.-KB/s    in 0s      

2026-05-13 05:12:37 (649 MB/s) - 'spacex-dash-app.py' saved [2075/2075]

Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'spacex-dash-app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8050
Press CTRL+C to quit
 dcc.Dropdown( id='site-dropdown', options=[ {'label': 'All Sites', 'value': 'ALL'}, {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'}, {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}, {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'}, {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'} ], value='ALL', placeholder="Select a Launch Site here", searchable=True ),
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    
    if entered_site == 'ALL':
        # Si se seleccionan todos los sitios, se agrupa por 'Launch Site' 
        # y se calcula la suma o conteo de lanzamientos exitosos (class=1)
        fig = px.pie(
            filtered_df, 
            values='class', 
            names='Launch Site', 
            title='Total Success Launches by Site'
        )
        return fig
    else:
        # 1. Filtrar las filas correspondientes al sitio seleccionado
        site_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        
        # 2. Agrupar por la columna 'class' (0 y 1) para contar cuántos éxitos y fracasos hay
        site_df_counts = site_df['class'].value_counts().reset_index()
        site_df_counts.columns = ['class', 'count']
        
        # 3. Renderizar el gráfico de pastel mostrando la proporción de éxito vs fracaso
        fig = px.pie(
            site_df_counts, 
            values='count', 
            names='class', 
            title=f'Total Success Launches for Site {entered_site}'
        )
        return fig
dcc.RangeSlider(
    id='payload-slider',
    min=0,
    max=10000,
    step=1000,
    marks={
        0: '0 kg',
        2500: '2500 kg',
        5000: '5000 kg',
        7500: '7500 kg',
        10000: '10000 kg'
    },
    value=[min_payload, max_payload]
),

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
low, high = payload_range
mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]
    
    if entered_site == 'ALL':
        # Si se seleccionan todos los sitios, se muestran todos los registros filtrados por peso
        fig = px.scatter(
            filtered_df, 
            x='Payload Mass (kg)', 
            y='class',
            color='Booster Version Category',
            title='Correlation between Payload and Success for all Sites'
        )
        return fig
    else:
        # Si se selecciona un sitio específico, se aplica un filtro adicional por 'Launch Site'
        site_mask = filtered_df['Launch Site'] == entered_site
        fig = px.scatter(
            filtered_df[site_mask], 
            x='Payload Mass (kg)', 
            y='class',
            color='Booster Version Category',
            title=f'Correlation between Payload and Success for site {entered_site}'
        )
        return fig
1.      ¿Qué sitio tiene la mayor cantidad de lanzamientos exitosos?
o       KSC LC-39A
o       Evidencia: Al seleccionar "ALL" en el menú desplegable, el gráfico de pastel (success-pie-chart) muestra que este sitio de lanzamiento abarca la porción más grande del total de misiones exitosas registradas en el dataset.
2.      ¿Qué sitio tiene la mayor tasa de éxito de lanzamientos?
o       KSC LC-39A
o       Evidencia: Al filtrar de manera individual cada instalación en el dropdown, la gráfica de pastel revela que este sitio tiene el mayor porcentaje de éxitos (proporción de la clase 1) frente a fallos (0), superando el 76% de efectividad.
3.      ¿Qué rango(s) de carga útil (payload) tiene la mayor tasa de éxito?
o       Rango entre 2,000 kg y 4,000 kg (además del segmento de alta capacidad entre ~8,000 kg y 10,000 kg).
o       Evidencia: En la gráfica de dispersión (suestas zonas muestran una alta densidad y concentra de puntos alineados estrictamente en el valor superior de éxito (class=1).
4.	¿Qué rango(s) de carga útil (payload) tiene la menor tasa de éxito?
o	Rango entre 4,000 kg y 5,500 kg.
o	Evidencia: El gráfico de dispersión revela un vacío casi absoluto de puntos en la zona de éxito para ese intervalo, concentrándose la inmensa mayoría de las marcas de lanzamientos sobre el valor inferior de fracaso (class=0).
5.	¿Qué versión del Booster F9 (v1.0, v1.1, FT, B4, B5, etc.) tiene la mayor tasa de éxito?
o	B5
o	Evidencia: Al examinar las etiquetas codificadas por colores en el gráfico de dispersión, los puntos correspondientes a la categoría de booster B5 se posicionan exclusivamente en la franja superior de éxito (1), demostrando una fiabilidad perfecta dentro de las muestras del dataset. [1, 2, 3, 4, 5]
