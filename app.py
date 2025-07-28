import streamlit as st
from PIL import Image

def main_page():
    # Page config
    st.set_page_config(page_title="Rajashri Deka | Portfolio", page_icon="🧠", layout="centered")

    # Header
    st.title("👩‍💻 Rajashri Deka")
    st.subheader("Python Developer | Gen AI & ML Enthusiast")

    col1, col2 = st.columns([1, 3])
    with col1:
        # Profile image
        image_path = 'IMG_3580.jpeg'
        image = Image.open(image_path)
        st.image(image, width=150)
    with col2:
        # Contact
        st.header("📫 Contact")
        st.markdown("""
        - 📧 Email: [rajashrideka07@gmail.com](mailto:rajashrideka07@gmail.com)  
        - 💼 LinkedIn: [https://www.linkedin.com/in/rajashrideka](https://www.linkedin.com/in/rajashrideka)
        - 💼 GitHub: [https://github.com/rshdeka](https://github.com/rshdeka)
        """)

    # About Me
    st.header("🧬 About Me")
    st.markdown("""
    I'm a Python Developer working at **Optum**, focusing on Python, AI/ML, Gen AI, and Azure Cloud services.  
    I'm passionate about building intelligent systems, automating workflows, and solving real-world problems with Python and Gen AI.
    """)

    # Projects
    st.header("🚀 Projects")
    st.markdown("""
    - 🧪 **FHIR Resource Generation API**  
    Built a FastAPI-based microservice to auto-generate realistic FHIR bundles for testing. Supports patient, encounter, and condition data creation.
    - 🤖 **Gen AI UI Test Agent**  
    Combined **LangChain**, **Azure OpenAI**, and **Playwright** to automate UI testing via BrowserUse Agent. Handles both positive and negative test case execution.
    - 📊 **Support Chat Classifier (XGBoost)**  
    Created a model to classify support conversations by intent and urgency using XGBoost. Added regression to predict conversation resolution time.
    - 📈 **Sales Forecast Dashboard (Streamlit)**  
    Built an interactive Streamlit dashboard to forecast product sales using a trained regression model.
    - 🔄 **FHIR Validator + Corrector**  
    Developed a validator using **Pydantic FHIR models** inside an Azure Function to clean and auto-correct invalid FHIR bundles.
    """)

    # Skills
    st.header("🛠️ Skills")
    st.markdown("""
    ##### 🧑‍💻 **Languages**
    - Python, C++
    ##### 🚀 **Frameworks**
    - FastAPI, Flask, Streamlit
    ##### 🗄️ **Data Management**
    - SQL, Azure Cosmos DB
    ##### 🤖 **GenAI Technologies**
    - Prompt Engineering, LLMs, Langchain, Agentic AI (BrowserUse + Playwright)
    ##### 📚 **Machine Learning**
    - **Supervised:** Linear/Logistic Regression, Decision Tree, Random Forest, SVM, KNN  
    - **Unsupervised:** K-Means Clustering, Market Basket Analysis  
    - **Ensemble Models:** XGBoost, LightGBM, VotingClassifier, StackingClassifier
    ##### ☁️ **Cloud Services**
    - Azure Functions, Azure Cosmos DB, Azure Databricks, Azure Event Grid, Azure Logic Apps, Power Automate
    ##### 🔢 **Data & Processing**
    - PySpark, NumPy, Pandas, Matplotlib, Seaborn, scikit-learn
    ##### 🧪 **Model Optimization & Evaluation**
    - GridSearchCV, RandomizedSearchCV, Cross-Validation, Confusion Matrix, ROC-AUC
    ##### ⚙️ **Automation & Tools**
    - Power BI, GitHub, GitHub Actions, Postman
    ##### 🕵️‍♀️ **OCR & Web Scraping**
    - OpenCV, BeautifulSoup
    """)

    # Resume download
    st.header("📄 Resume")
    with open("resume.pdf", "rb") as file:
        btn = st.download_button(
            label="📥 Download My Resume",
            data=file,
            file_name="Rajashri_Deka_Resume.pdf",
            mime="application/pdf"
        )


def experience_page():  
    # Work Experience  
    st.title("💼 Work Experience")  
    st.markdown("""
    ### 🧑‍💻 Software Engineer | Optum (UnitedHealth Group) | *Sept 2023 – Present*  
    - Automated the data flow pipeline for Optum Bank's Customer Support data. The automated system consisted of loading Customer 
    Support chats from Azure Databricks, extraction of key information using Python, SQL, and Prompt Engineering (e.g., Product, 
    Category, Sub-Category, Sentiment, Root Cause, Responsible Party, Prevention Method), and storage to Cosmos DB for further 
    analysis, which achieved an accuracy rate of approx. 96.7% in aligning with the manual entries. Scheduled a Databricks job to run at 
    regular intervals, to ensure that Cosmos DB is consistently updated with latest data.
    """)


# Sidebar for navigation  
st.sidebar.title("Navigation")  
page_selection = st.sidebar.radio("Go to", ["Main Page", "Experience Page"])  

 
# Render the selected page  
if page_selection == "Main Page":  
    main_page()  
elif page_selection == "Experience Page":  
    experience_page()  