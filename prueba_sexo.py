from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/idivalsolorzano/mapa_cohorte_cantabria/main/prueba_sexo.csv')

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Sexo de los participantes por grupo de edad'),
    dcc.Dropdown(
        id="bar-chart-x-dropdown",
        options=['40-45', '46-50', '51-55', '56-60','61-65', '66-70'],
        value="40-45",
        clearable=False,
    ),
    dcc.Graph(id="bar-chart-x-graph"),
])


@app.callback(
    Output("bar-chart-x-graph", "figure"), 
    Input("bar-chart-x-dropdown", "value"))
def update_bar_chart(grupo_edad):
    #df = px.data.tips() # replace with your own data source
    mask = df["grupo_edad"] == grupo_edad
    fig = px.bar(df[mask], x="grupo_edad", y=["Hombres %", "Mujeres %"],
                 labels={'variable': 'Sexo', 
                     'value': 'Porcentaje',
                    'grupo_edad': 'Grupo de edad (años)' },
                 title='Sexo de los participantes por grupo de edad',
                 color_discrete_sequence=['#19D3F3', 'pink']) #color="smoker", barmode="group"
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)