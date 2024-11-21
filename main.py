import streamlit as st
import pandas as pd
import os

# Function to save form data to a CSV file
def save_response(name, user_email, model_name, user_insta):
    response_data = {'Name': [name], 'Email': [user_email], 'Model': [model_name], 'Insta': [user_insta]}
    df = pd.DataFrame(response_data)

    # Check if the CSV file already exists
    if os.path.exists('responses.csv'):
        # If the file exists, append the new data to it
        df_existing = pd.read_csv('responses.csv')
        df = pd.concat([df_existing, df], ignore_index=True)

    # Save the data to CSV
    df.to_csv('responses.csv', index=False)


# Page configuration
st.set_page_config(page_title="Clothing Main", page_icon=":tshirt:", layout="wide")

# Add stylish fonts and CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bellefair&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@400&display=swap');

    .title {
        font-family: 'Bellefair', serif;
        color: #000000;
        font-size: 4em;
        text-align: center;
    }

    .subtitle {
        font-family: 'Fraunces', serif;
        color: #000000;
        font-size: 1.5em;
        text-align: center;
        
    }
        .cut-corner-img {
        clip-path: polygon(0 0, 100% 0%, 100% 90%, 10% 100%, 0% 100%);
        width: 100%;
        height: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Page content
st.markdown('<div class="title">Columbian Family</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AW2025</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle"></div>', unsafe_allow_html=True)
# Display images
image_paths = [
    'im1.png',
    'im2.png',
    'im3.png',
    'im4.png',
    'im5.png'
]
# '/Users/andaks/PycharmProjects/Columbia_clo/im5.png'
st.markdown(
    '''
    <div class="title" style="background-color: #6CACE4; color: white;">
        Made in love with Columbia and its style
    </div>
    ''', unsafe_allow_html=True
)
st.markdown('<div class="subtitle"></div>', unsafe_allow_html=True)



# Create 2 columns
col1, col2 = st.columns([1, 2])

# Display image in the first column (1/3 of the screen)
with col1:
    st.image(image_paths[0], use_container_width=True)  # The image will take up 1/3 of the screen width

with col2:
    st.write('<div class="title">STRIPED</div>', unsafe_allow_html=True)

    st.markdown(
        '''
        <div class="title" style="text-align: left;">
            <ul>
                <li>70$</li>
                <li>Loose-fitting longsleeve in 100% cotton</li>
                <li>Breathability, lightness, durability</li>
                <li>Hypoallergenic</li>
                <li>One size</li>
                <li>Unisex</li>
                <li>Sewn label in front</li>
                <li>Delicate washing</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True
    )

col1, col2 = st.columns([2, 1])

with col1:
    st.write('<div class="title">FUNDAMENTAL</div>', unsafe_allow_html=True)

    st.markdown(
        '''
        <div class="title" style="text-align: left;">
            <ul>
                <li>75$</li>
                <li>Loose-fitting longsleeve in 100% cotton</li>
                <li>Breathability, lightness, durability</li>
                <li>Hypoallergenic</li>
                <li>One size</li>
                <li>Unisex</li>
                <li>Sewn label on the back</li>
                <li>Delicate washing</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True
    )

with col2:
    st.image(image_paths[1], use_container_width=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.image(image_paths[2], use_container_width=True)  # The image will take up 1/3 of the screen width

with col2:
    st.write('<div class="title">RUNNERS</div>', unsafe_allow_html=True)

    st.markdown(
        '''
        <div class="title" style="text-align: left;">
            <ul>
                <li>80$</li>
                <li>Loose-fitting longsleeve in 100% cotton</li>
                <li>Breathability, lightness, durability</li>
                <li>Hypoallergenic</li>
                <li>One size</li>
                <li>Unisex</li>
                <li>Sewn label on the back</li>
                <li>Delicate washing</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True
    )

col1, col2 = st.columns([2, 1])

with col1:
    st.write('<div class="title">LOGO CHEST</div>', unsafe_allow_html=True)

    st.markdown(
        '''
        <div class="title" style="text-align: left;">
            <ul>
                <li>65$</li>
                <li>Loose-fitting longsleeve in 100% cotton</li>
                <li>Breathability, lightness, durability</li>
                <li>Hypoallergenic</li>
                <li>One size</li>
                <li>Unisex</li>
                <li>Sewn label in front</li>
                <li>Delicate washing</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True
    )

with col2:
    st.image(image_paths[3], use_container_width=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.image(image_paths[4], use_container_width=True)  # The image will take up 1/3 of the screen width

with col2:
    st.write('<div class="title">We see the light</div>', unsafe_allow_html=True)

    st.markdown(
        '''
        <div class="title" style="text-align: left;">
            <ul>
                <li>60$</li>
                <li>Loose-fitting longsleeve in 100% cotton</li>
                <li>Breathability, lightness, durability</li>
                <li>Hypoallergenic</li>
                <li>One size</li>
                <li>Unisex</li>
                <li>Sewn label on the back</li>
                <li>Delicate washing</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True
    )

# User request form
st.markdown('<div class="title">Pre-order only | Limited number</div>', unsafe_allow_html=True)
st.markdown('<div class="title">We will contact you in 24 hours to confirm your order</div>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stLinkButton>a {
        background-color: white;  /* White background */
        color: #0033A0;  /* Columbia University Blue text */
        font-size: 16px;
        text-decoration: none;  /* Removes underline */
        font-weight: bold;
        padding: 10px 20px;  /* Adds padding for a button-like feel */
        border-radius: 5px;  /* Rounded corners */
        border: 2px solid #0033A0;  /* Blue border */
    }
    .stLinkButton>a:hover {
        background-color: #005B99;  /* Darker blue background on hover */
        color: white;  /* White text on hover */
        border: 2px solid #005B99;  /* Darker blue border on hover */
    }
    </style>
    """, unsafe_allow_html=True)

st.link_button("Button to order", "https://forms.gle/FBHewzUTo1Y7tqQ38", type="primary", use_container_width = True)

st.markdown(
    '''
    <div class="subtitle" style="background-color: #6CACE4; color: white;">
        Made by anonymous designers | Columbian Family 2024
    </div>
    ''', unsafe_allow_html=True
)

#st.markdown('<div class="subtitle">Made by anonymous designers | Columbian Family 2024</div>', unsafe_allow_html=True)
