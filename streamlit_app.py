import streamlit as st

def custom_css():
    """
    Embeds custom CSS styles into the Streamlit app to enhance its appearance.
    Styles include changes to the background, text colors, buttons, and layout features.
    """
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
                background-color: #ffffff;  /* White for card elements */
                padding: 10px;
                border-radius: 10px;
                box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2);
            }
        </style>
    """, unsafe_allow_html=True)

# Initialize Streamlit application with custom styling
custom_css()

# Display the main title of the Streamlit application
st.title('HerGymPal')

# Section headers and selection options are used to collect user inputs through interactive GUI elements.
# Each selectbox corresponds to a different aspect of the user's fitness plan.

# Fitness Goals
st.header('Fitness Goals')
fitness_goal = st.selectbox(
    "Select your primary fitness goal:",  # Prompts the user to select their fitness goal.
    ('Bulking', 'Cutting', 'Toning')  # Options provided to the user.
)

# Diet Management
st.header('Diet Management')
diet_management = st.selectbox(
    "Select your diet management strategy:",  # Asks the user about their diet management preference.
    ('Tracking macronutrients', 'Eating intuitively', 'Following a set meal plan')  # Diet management options.
)

# Generate plan button: When clicked, it will process the inputs from selectboxes to generate a custom fitness plan.
if st.button('Generate Custom Fitness Plan'):
    st.subheader('Your Custom Fitness Plan')
    st.write(f"**Fitness Goal:** {fitness_goal}")
    st.write(f"**Diet Management Strategy:** {diet_management}")
