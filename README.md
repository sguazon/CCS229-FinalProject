## FeelingsDecoded
**by Shina Guazon - BSCS 3B**

This serves as a guide to explore the functionalities and usage of a Python application built with Streamlit. The application, FeelingsDecoded, leverages Google's powerful AI model, Gemini, to analyze the sentiment hidden within provided text input.

**Architectural Overview:**

The application is built upon the following essential tools:

1. Streamlit: A Python library used for crafting the user interface.
2. Environment variables: Utilized for secure storage of API keys.
3. Google's generative AI library: Facilitates interaction with the Gemini model.

**API Key Setup:**

1. GEMINI_API_KEY: This key grants access to the specific Gemini model suited for the application's needs. 
2. API_KEY: Depending on the chosen service, a broader Google AI platform access key might be necessary. 

**Secure Key Storage (Environment Variables):**

For security reasons, it is crucial to store API keys securely. The code utilizes the `dotenv` library to load these keys from a hidden file named `.env`. This approach ensures that the keys are not directly embedded in the code, protecting them from unauthorized access.

**Core Functionalities:**

1. **Sentiment Analysis:** Decoding the Emotional Core of Text Input
Users can freely express themselves in the provided text area.
It is important to note that while Gemini is a powerful model, it might not be specifically trained for sentiment analysis, potentially leading to limitations in the accuracy of the classification (positive, negative, or neutral).

2. **Creative Text Generation** (Based on Identified Sentiment):
This feature adds a creative dimension to the analysis, potentially providing a new perspective on the user's thoughts or feelings.

3. **Conversation History**: Keeping Track of User-Gemini Interactions

**Application Usage:**

1. Execute the Python script using `python feeling_classification.py` to launch the Streamlit application.
2. Locate the text area labeled "Tell me how you're feeling" and express yourself freely.
3. Click the "Analyze My Feeling" button to trigger the sentiment analysis process using Gemini.
4. The application will display the classified sentiment of the input text (positive, negative, or neutral). Additionally, if the sentiment classification is successful, it might generate creative text that reflects the identified feeling, offering a unique perspective.
5. If available, the conversation history between the user and Gemini will be displayed, allowing users to revisit past interactions and gain insights.
6. To clear the conversation history and begin a new session with Gemini, click the "Reset Conversation" button.

**Additional Considerations:**

1. **Sentiment Analysis Limitations**: It is important to acknowledge that this is a basic example showcasing sentiment analysis. More advanced techniques might be required for highly accurate sentiment analysis in real-world scenarios.

2. **Creative Text Generation**: The creative text generation feature relies on Gemini's capabilities and might not always perfectly align with the sentiment of the user's input text. 

