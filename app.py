import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Recommender System App')
st.write("This app is based on the content from my Jupyter notebook.")
st.header("Data Example")
df = pd.DataFrame({
    'Column A': [1, 2, 3, 4],
    'Column B': [10, 20, 30, 40]
})
st.write(df)

# Example 2: Plotting data
st.header("Plot Example")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Example 3: Interactivity (input from the user)
st.header("User Input Example")
user_input = st.text_input("Enter some text", "Type here...")
st.write("You entered:", user_input)

# Example 4: Displaying a matplotlib plot
st.header("Matplotlib Plot Example")
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
st.pyplot(plt)

# Example 5: Running custom functions
def custom_function(x):
    return x ** 2

input_value = st.number_input("Enter a number to square:", min_value=0, max_value=100, value=10)
st.write("Squared value:", custom_function(input_value))
