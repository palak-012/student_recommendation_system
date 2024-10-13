import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data for demonstration (replace with actual data as needed)
students_data = pd.DataFrame({
    'student_id': [1, 2, 3],
    'course': ['Computer Science', 'Mechanical Engineering', 'Environmental Science'],
    'year': [3, 2, 1],
    'interests': ['AI', 'Robotics', 'Sustainability'],
    'average_quiz_score': [85, 70, 90]
})

materials_data = pd.DataFrame({
    'material_id': [101, 102, 103, 104, 105],
    'subject': ['AI', 'Blockchain', 'Robotics', 'Environmental Science', 'Data Science'],
    'difficulty': ['Easy', 'Medium', 'Hard', 'Easy', 'Medium'],
    'popularity': [100, 200, 150, 120, 170]
})

engagement_data = pd.DataFrame({
    'student_id': [1, 2, 1, 3],
    'material_id': [101, 102, 103, 104],
    'views': [10, 20, 5, 15],
    'rating': [4, 5, 3, 4]
})

# Recommendation function (simplified version)
def calc_recommendation_score(row, interests_weight=0.3, performance_weight=0.3, popularity_weight=0.2, views_weight=0.2):
    interest_match = 1 if row['subject'] == row['interests'] else 0
    performance_fit = (1 if row['average_quiz_score'] > 70 else 0)  # Basic performance logic
    popularity_score = row['popularity'] / materials_data['popularity'].max()
    views_score = row['views'] / engagement_data['views'].max() if 'views' in engagement_data else 0

    final_score = (interests_weight * interest_match +
                   performance_weight * performance_fit +
                   popularity_weight * popularity_score +
                   views_weight * views_score)

    return final_score

# Streamlit app setup
st.title('Recommender System for Study Materials')
st.write("This app provides personalized study material recommendations based on student profiles.")

# User input for student profile
st.header("Enter Student Details")
student_id = st.selectbox("Select Student ID", students_data['student_id'].tolist())
student_info = students_data[students_data['student_id'] == student_id].iloc[0]

# Display selected student information
st.write(f"Selected Student ID: {student_info['student_id']}")
st.write(f"Course: {student_info['course']}, Year: {student_info['year']}, Interests: {student_info['interests']}, Average Quiz Score: {student_info['average_quiz_score']}")

# Calculate recommendation scores
materials_data['recommendation_score'] = materials_data.apply(calc_recommendation_score, axis=1, args=(student_info['interests'], student_info['average_quiz_score'],))

# Get top recommendations
recommendations = materials_data.sort_values(by='recommendation_score', ascending=False).head(5)

# Display recommendations
st.header("Top Recommendations")
for _, row in recommendations.iterrows():
    st.write(f"Material ID: {row['material_id']}, Subject: {row['subject']}, Difficulty: {row['difficulty']}, Score: {round(row['recommendation_score'], 2)}")

st.header("Popularity of Recommended Materials")
plt.bar(recommendations['material_id'], recommendations['popularity'], color='blue')
plt.xlabel('Material ID')
plt.ylabel('Popularity Score')
plt.title('Popularity of Top Recommended Materials')
st.pyplot(plt)

if st.button('Show Correlation Map'):
    # Placeholder for actual correlation data
    correlation_data = pd.DataFrame(np.random.rand(5, 5), columns=['A', 'B', 'C', 'D', 'E'])
    st.header("Correlation Map")
    st.write(correlation_data)
    st.line_chart(correlation_data)  # Replace with actual correlation heatmap if needed



