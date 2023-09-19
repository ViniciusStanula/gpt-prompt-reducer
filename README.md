# GOOGLE SEARCH CONSOLE API

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gpt-prompt-reducer.streamlit.app/)

This code/streamlit app aims to reduce the number of tokens required in prompts, leading to cost savings.

## 🔧 How It Works:

The app operates in two main cleaning phases:
* Eliminating stop words, common language words like "the," "is," and "and," from the text.
* Lemmatizing verbs to simplify and standardize verb forms, enhancing comprehension for models like GPT.

Let's start with an example using the description of the game Baldur’s Gate 3, sourced from Wikipedia:

> Baldur’s Gate 3 is a captivating role-playing video game featuring both single-player and cooperative multiplayer modes. Players have the freedom to create one or more characters and assemble a party, including several pre-generated characters, to delve into the game's rich narrative.

When processed through the Tokenizer, this original text consumes 49 tokens.

After applying our prompt reduction, the text becomes:

> Baldur's Gate 3 role-playing video game, single-player, cooperative multiplayer element. Players create one character, form a party with pre-generated characters, explore the game's story.

With this transformation, we've successfully reduced the token count from 49 to 28 tokens, marking a remarkable 42.86% reduction in token usage.

## How to Use It

1. **Read the Blog Post**: Explore a detailed guide on how I reduced OpenAI costs and token usage by 40% with Python. [Read the Blog Post](https://viniciusstanula.com/en/blog/how-i-reduced-openai-costs-and-token-usage-by-40-with-python/)

2. **Streamlit App**: Easily reduce your prompts using the Streamlit web application. [Try the Streamlit App](https://gpt-prompt-reducer.streamlit.app/)

3. **Manual Integration**: If you prefer manual integration, you can copy the `preprocess_text` function from the `prompt-reducer.py` file and use it in your own projects.

Feel free to choose the method that suits your needs best and optimize your token usage with OpenAI!

## ☕Use Cases:

* Token reduction is particularly beneficial when using OpenAI's API, as it charges based on token count.
* This app finds application in scenarios like rewriting product descriptions efficiently, especially when dealing with a significant volume of content in the API.

### If you want to get in touch or be the first to know about my development ideas: ⤵️

<p align="left">
  <a href="https://viniciusstanula.com/en/" target="_blank" alt="Gmail">
  <img src="https://img.shields.io/badge/Website-006E93?style=flat-square&logo=wordpress&logoColor=white&link=LINK-DO-SEU-GMAIL" /></a>
  
  <a href="mailto:vinicius.stanula.seo@gmail.com" target="_blank" alt="Gmail">
  <img src="https://img.shields.io/badge/-Gmail-FF0000?style=flat-square&labelColor=FF0000&logo=gmail&logoColor=white&link=LINK-DO-SEU-GMAIL" /></a>

  <a href="https://www.linkedin.com/in/vinicius-stanula/" target="_blank" alt="LinkedIn">
  <img src="https://img.shields.io/badge/-Linkedin-0e76a8?style=flat-square&logo=Linkedin&logoColor=white&link=LINK-DO-SEU-LINKEDIN" /></a>

  <a href="https://www.instagram.com/viniciusstanula/" target="_blank" alt="Instagram">
  <img src="https://img.shields.io/badge/-Instagram-DF0174?style=flat-square&labelColor=DF0174&logo=instagram&logoColor=white&link=LINK-DO-SEU-INSTAGRAM"/></a>

  <a href="https://www.buymeacoffee.com/viniciusstanula" target="_blank" alt="Buy Me a Coffee">
    <img src="https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-FF813F?style=flat-square&labelColor=FF813F&logo=buy-me-a-coffee&logoColor=white" />
  </a>
  
</p>
