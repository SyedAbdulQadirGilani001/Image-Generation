import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

# Set the title of the Streamlit app
st.title("Simple Image Generator")

# Add a sidebar for user inputs
st.sidebar.header("Settings")

# User input for the number of shapes
num_shapes = st.sidebar.slider("Number of Shapes", min_value=1, max_value=10, value=5)

# User input for the shape type
shape_type = st.sidebar.selectbox("Shape Type", ["Circle", "Square", "Triangle"])

# User input for the color
color = st.sidebar.color_picker("Pick a Color", "#00f900")

# Function to generate random shapes
def generate_shapes(num_shapes, shape_type, color):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    for _ in range(num_shapes):
        x = random.uniform(1, 9)
        y = random.uniform(1, 9)
        size = random.uniform(0.5, 1.5)

        if shape_type == "Circle":
            circle = plt.Circle((x, y), size, color=color)
            ax.add_patch(circle)
        elif shape_type == "Square":
            square = plt.Rectangle((x - size / 2, y - size / 2), size, size, color=color)
            ax.add_patch(square)
        elif shape_type == "Triangle":
            triangle = plt.Polygon([(x, y), (x + size, y), (x + size / 2, y + size)], color=color)
            ax.add_patch(triangle)

    return fig

# Generate the shapes based on user input
fig = generate_shapes(num_shapes, shape_type, color)

# Display the generated image
st.pyplot(fig)

# Add a button to regenerate the image
if st.button("Generate New Image"):
    fig = generate_shapes(num_shapes, shape_type, color)
    st.pyplot(fig)