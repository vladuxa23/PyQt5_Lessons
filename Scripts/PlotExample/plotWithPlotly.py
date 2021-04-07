from PySide2 import QtCore, QtWidgets, QtWebEngineWidgets
import plotly.graph_objects as go
import plotly.express as px
import math
import pandas as pd
import numpy as np


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QtWidgets.QPushButton('Plot', self)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)

        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)

        # self.button.clicked.connect(self.show_graph1)
        # self.button.clicked.connect(self.show_graph2)
        self.button.clicked.connect(self.show_graph3)
        self.resize(1000, 800)

    def show_graph1(self):
        data = px.data.gapminder()
        df_2007 = data[data['year'] == 2007]
        df_2007 = df_2007.sort_values(['continent', 'country'])

        hover_text = []
        bubble_size = []

        for index, row in df_2007.iterrows():
            hover_text.append(('Country: {country}<br>' +
                               'Life Expectancy: {lifeExp}<br>' +
                               'GDP per capita: {gdp}<br>' +
                               'Population: {pop}<br>' +
                               'Year: {year}').format(country=row['country'],
                                                      lifeExp=row['lifeExp'],
                                                      gdp=row['gdpPercap'],
                                                      pop=row['pop'],
                                                      year=row['year']))
            bubble_size.append(math.sqrt(row['pop']))

        df_2007['text'] = hover_text
        df_2007['size'] = bubble_size
        sizeref = 2. * max(df_2007['size']) / (100 ** 2)

        # Dictionary with dataframes for each continent
        continent_names = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
        continent_data = {continent: df_2007.query("continent == '%s'" % continent)
                          for continent in continent_names}

        # Create figure
        fig = go.Figure()

        for continent_name, continent in continent_data.items():
            fig.add_trace(go.Scatter(
                x=continent['gdpPercap'], y=continent['lifeExp'],
                name=continent_name, text=continent['text'],
                marker_size=continent['size'],
            ))

        # Tune marker appearance and layout
        fig.update_traces(mode='markers', marker=dict(sizemode='area',
                                                      sizeref=sizeref, line_width=2))

        fig.update_layout(
            title='Life Expectancy v. Per Capita GDP, 2007',
            xaxis=dict(
                title='GDP per capita (2000 dollars)',
                gridcolor='white',
                type='log',
                gridwidth=2,
            ),
            yaxis=dict(
                title='Life Expectancy (years)',
                gridcolor='white',
                gridwidth=2,
            ),
            paper_bgcolor='rgb(243, 243, 243)',
            plot_bgcolor='rgb(243, 243, 243)',
        )
        # fig.show()
        # df = px.data.tips()
        # fig = px.box(df, x="day", y="total_bill", color="smoker")
        # fig.update_traces(quartilemethod="exclusive")  # or "inclusive", or "linear" by default
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def show_graph2(self):
        t = np.linspace(0, 20, 100)
        x, y, z = np.cos(t), np.sin(t), t

        fig = go.Figure(data=[go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(
                size=12,
                color=z,  # set color to an array/list of desired values
                colorscale='Viridis',  # choose a colorscale
                opacity=0.8
            )
        )])

        # tight layout
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def show_graph3(self):
        url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
        dataset = pd.read_csv(url)

        years = ["1952", "1962", "1967", "1972", "1977", "1982", "1987", "1992", "1997", "2002",
                 "2007"]

        # make list of continents
        continents = []
        for continent in dataset["continent"]:
            if continent not in continents:
                continents.append(continent)
        # make figure
        fig_dict = {
            "data": [],
            "layout": {},
            "frames": []
        }

        # fill in most of layout
        fig_dict["layout"]["xaxis"] = {"range": [30, 85], "title": "Life Expectancy"}
        fig_dict["layout"]["yaxis"] = {"title": "GDP per Capita", "type": "log"}
        fig_dict["layout"]["hovermode"] = "closest"
        fig_dict["layout"]["updatemenus"] = [
            {
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 500, "redraw": False},
                                        "fromcurrent": True, "transition": {"duration": 300,
                                                                            "easing": "quadratic-in-out"}}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                          "mode": "immediate",
                                          "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }
        ]

        sliders_dict = {
            "active": 0,
            "yanchor": "top",
            "xanchor": "left",
            "currentvalue": {
                "font": {"size": 20},
                "prefix": "Year:",
                "visible": True,
                "xanchor": "right"
            },
            "transition": {"duration": 300, "easing": "cubic-in-out"},
            "pad": {"b": 10, "t": 50},
            "len": 0.9,
            "x": 0.1,
            "y": 0,
            "steps": []
        }

        # make data
        year = 1952
        for continent in continents:
            dataset_by_year = dataset[dataset["year"] == year]
            dataset_by_year_and_cont = dataset_by_year[
                dataset_by_year["continent"] == continent]

            data_dict = {
                "x": list(dataset_by_year_and_cont["lifeExp"]),
                "y": list(dataset_by_year_and_cont["gdpPercap"]),
                "mode": "markers",
                "text": list(dataset_by_year_and_cont["country"]),
                "marker": {
                    "sizemode": "area",
                    "sizeref": 200000,
                    "size": list(dataset_by_year_and_cont["pop"])
                },
                "name": continent
            }
            fig_dict["data"].append(data_dict)

        # make frames
        for year in years:
            frame = {"data": [], "name": str(year)}
            for continent in continents:
                dataset_by_year = dataset[dataset["year"] == int(year)]
                dataset_by_year_and_cont = dataset_by_year[
                    dataset_by_year["continent"] == continent]

                data_dict = {
                    "x": list(dataset_by_year_and_cont["lifeExp"]),
                    "y": list(dataset_by_year_and_cont["gdpPercap"]),
                    "mode": "markers",
                    "text": list(dataset_by_year_and_cont["country"]),
                    "marker": {
                        "sizemode": "area",
                        "sizeref": 200000,
                        "size": list(dataset_by_year_and_cont["pop"])
                    },
                    "name": continent
                }
                frame["data"].append(data_dict)

            fig_dict["frames"].append(frame)
            slider_step = {"args": [
                [year],
                {"frame": {"duration": 300, "redraw": False},
                 "mode": "immediate",
                 "transition": {"duration": 300}}
            ],
                "label": year,
                "method": "animate"}
            sliders_dict["steps"].append(slider_step)

        fig_dict["layout"]["sliders"] = [sliders_dict]

        fig = go.Figure(fig_dict)
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Widget()
    widget.show()
    app.exec_()