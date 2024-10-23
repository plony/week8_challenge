# import dash
# from dash import html

# app = dash.Dash(__name__)

# app.layout = html.Div(children=[
#     html.P('Hello, Dash!'),
#     html.Div('Dash: A web application framework for Python.')
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)


from app_instance import app  # Import the app instance
from layout import create_layout  # Import the layout
import callbacks  # Import callbacks to register them


# Assign the layout from layout.py
app.layout = create_layout(app)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
