import streamlit as st

# Custom CSS to style the Streamlit app
def custom_css():
    st.markdown("""
        <style>
            body {
                background-color: #ffe6f2;  /* Soft pink background */
            }
            .stSelectbox > div {
                background-color: #ffb3d9;  /* Light pink for input options background */
                border-radius: 10px;
                padding: 5px 10px;
                margin-bottom: 5px;
            }
            .stSelectbox > label {
                color: #cc0066;  /* Vibrant pink for text */
                font-weight: bold;
            }
            button {
                color: white;
                background-color: #ff66b2;  /* Vibrant pink for buttons */
                border: none;
                border-radius: 5px;
                padding: 10px 24px;
                margin: 10px 0;
                cursor: pointer;
            }
            .css-1d391kg, .css-18e3th9 {
                background-color: #ffffff;  /* White for cards */
                padding: 10px;
                border-radius: 10px;
                box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2);
            }
        </style>
    """, unsafe_allow_html=True)

custom_css()  # Call the function to inject CSS

st.title('HerGymPal')  # Updated app title

# Section 1: Fitness Goals and Strategies
st.header('Section 1: Fitness Goals and Strategies')
fitness_goal = st.selectbox(
    "What is your primary fitness goal right now?",
    ('Bulking', 'Cutting', 'Toning')
)

# Section 2: Diet Management
st.header('Section 2: Diet Management')
diet_management = st.selectbox(
    "How do you prefer to manage your diet for fitness?",
    ('Tracking macronutrients', 'Eating intuitively', 'Following a set meal plan')
)

# Section 3: Workout Preferences
st.header('Section 3: Workout Preferences')
exercise_type = st.selectbox(
    "What type of exercise do you enjoy the most?",
    ('Strength training', 'Cardiovascular activities', 'Flexibility and balance exercises')
)

# Section 4: Recovery and Rest
st.header('Section 4: Recovery and Rest Days')
recovery_management = st.selectbox(
    "How do you manage recovery and rest days?",
    ('I often feel sore or fatigued', 'I rarely feel sore or fatigued')
)

# Section 5: Challenges and Support
st.header('Section 5: Challenges and Support')
fitness_challenge = st.selectbox(
    "What are your biggest challenges in achieving your fitness goals?",
    ('Time constraints', 'Lack of motivation', 'Diet management')
)

# Dictionary to map selections to advice
advice_dict = {
    'Bulking': 'Increase your calorie intake by 10-20%, focusing on proteins and carbohydrates to fuel your workouts.',
    'Cutting': 'Decrease your calorie intake by 10-20% and increase your cardio exercises to create a calorie deficit.',
    'Toning': 'Maintain your current calorie intake but focus on high-rep, low-weight exercises to define your muscles.',
    'Tracking macronutrients': 'Consider using a food tracking app to maintain a balanced intake of proteins, fats, and carbohydrates.',
    'Eating intuitively': "Listen to your body’s hunger cues and focus on whole, nutrient-dense foods to meet your energy needs.",
    'Following a set meal plan': 'Consult with a nutritionist to create a meal plan that aligns with your fitness goals.',
    'Strength training': 'Schedule 3-4 days of weight training per week, focusing on major muscle groups.',
    'Cardiovascular activities': 'Incorporate a mix of high-intensity interval training (HIIT) and steady-state cardio sessions into your weekly routine.',
    'Flexibility and balance exercises': 'Add yoga or Pilates sessions to enhance your core strength and flexibility, crucial for overall fitness.',
    'I often feel sore or fatigued': 'Ensure you’re allowing enough recovery time between workouts; consider integrating more active recovery days focused on light activities like walking or gentle stretching.',
    'I rarely feel sore or fatigued': 'You might be ready to increase the intensity or frequency of your workouts to continue seeing progress.',
    'Time constraints': 'Explore shorter, more intense workouts like HIIT to get maximum results in minimal time.',
    'Lack of motivation': 'Join fitness groups or communities to find support and motivation from like-minded individuals.',
    'Diet management': 'Consider a consultation with a dietitian to help tailor your nutritional intake to your fitness needs.'
}

if st.button('Generate Custom Fitness Plan'):
    st.subheader('Your Custom Fitness Plan')
    st.write(f"**Primary Fitness Goal ({fitness_goal}):** {advice_dict[fitness_goal]}")
    st.write(f"**Diet Management Strategy ({diet_management}):** {advice_dict[diet_management]}")
    st.write(f"**Preferred Exercises ({exercise_type}):** {advice_dict[exercise_type]}")
    st.write(f"**Recovery Strategy ({recovery_management}):** {advice_dict[recovery_management]}")
    st.write(f"**Challenges ({fitness_challenge}):** {advice_dict[fitness_challenge]}")
