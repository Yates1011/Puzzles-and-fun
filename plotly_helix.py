"""
A script to plot a helix using plotly.

I have just discovered plotly and in the process of converting some scripts to see how they end up. 

https://plotly.com/
"""
import plotly.graph_objects as go
import numpy as np

# Create an array of values 
t = np.linspace(0, 10*np.pi, 500)

# Calculate helix coordinates
x = np.sin(t)
y = np.cos(t)
z = t

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers',
                                   marker=dict(size=5, color=z, colorscale='sunset'))])


# Ugly way of creating a "play" button 
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                  updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                  method='animate', args=[None, dict(frame=dict(duration=50, redraw=True),
                  fromcurrent=True,transition=dict(duration=0))])])])

frames = [go.Frame(data=[go.Scatter3d(x=x[:k], y=y[:k], z=z[:k], mode='markers',
          marker=dict(size=5, color=z[:k], colorscale='sunset'))])
          for k in range(1, len(t))]

fig.frames = frames

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 50

fig.show()
