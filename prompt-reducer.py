# Importing the necessary libraries/modules
import streamlit as st  # For creating a web-based UI
import nltk  # Natural Language Toolkit for text processing
from nltk.corpus import stopwords  # Stopwords dataset for filtering common words
from nltk.stem import WordNetLemmatizer  # Lemmatization for word normalization
import string  # Provides a collection of punctuation characters
from PIL import Image
import tiktoken

@st.cache_data(show_spinner=False)
def open_image(filename):
    return Image.open(filename)

favicon = Image.open("./assets/favicon.png")

st.set_page_config(
    page_title="GPT Prompt Reducer",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state='collapsed',
)

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

# Download required NLTK resources
nltk.download('stopwords')  # Download stopwords dataset
nltk.download('punkt')  # Download punkt tokenizer
nltk.download('wordnet')  # Download WordNet dataset for lemmatization

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# Function for text preprocessing
def preprocess_text(text):
    # Create a lemmatizer object for English
    lemmatizer = WordNetLemmatizer()
    
    # Load the stopwords dataset for English
    stop_words = set(stopwords.words('english'))    

    # Split the input text into words (tokenization)
    words = text.split()

    # Apply lemmatization, remove stopwords, strip whitespace, and remove special characters
    filtered_words = [lemmatizer.lemmatize(word) for word in words if word.lower() not in stop_words and word.strip() != '']
    
    # Remove single quotes, hyphens, and punctuation marks
    filtered_words = [word.replace("'", "").replace("-", "") for word in filtered_words]
    filtered_words = [''.join(char for char in word if char not in string.punctuation) for word in filtered_words]

    # Reconstruct the processed text from the filtered words
    processed_text = ' '.join(filtered_words)
    
    return processed_text

# Columns for the layout
colunhead, colundhead2 = st.columns([0.06, 0.99])

# Image for the first column
with colunhead:
    st.image(open_image("./assets/robozin2.png"))

# Informations on the second column
with colundhead2:
    st.header("GPT Prompt Reducer")
    st.markdown('<p class="minha-classe">By <a href="https://viniciusstanula.com/en/">Vinicius Stanula</a>, made in Streamlit 🎈</p>', unsafe_allow_html=True)
    
with st.expander('ℹ️ - About the App'):
    st.markdown("""
                Easily minimize token usage in your prompts for OpenAI's ChatGPT. This app streamlines the process by removing stop words and lemmatizing verbs, reducing tokens by up to 42.86%. Simplify your prompts and save on token costs effortlessly.
                \nSimply insert your prompt/text and see the results.""")

col1, col2 = st.columns(2)

with col1:
    st.subheader('Insert your prompt here:')
    text = st.text_area('Insert your prompt here:', label_visibility="collapsed", height=300)
    button = st.button('Reduce Prompt ✨')

with col2:
    st.subheader('Here is your result:')
    if button:
        count_before = num_tokens_from_string(text, "gpt-3.5-turbo")
        processed_text = preprocess_text(text)  # Replace with your text preprocessing logic
        count_after = num_tokens_from_string(processed_text, "gpt-3.5-turbo")

        # Calculate the percentage reduction
        percentage_reduction = ((count_before - count_after) / count_before) * 100
        percentage_reduction = round(percentage_reduction, 2)

        st.write(processed_text)
        st.write("Token Count Before Processing:", count_before)
        st.write("Token Count After Processing:", count_after)
        st.write("Percentage Reduction:", str(percentage_reduction), "%")      