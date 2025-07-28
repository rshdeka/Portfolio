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
    ### 🧑‍💻 Software Engineer 
    #### 🏢 Optum (UnitedHealth Group) | *Sept 2023 – Present* 

    ##### 🧬 PROJECT: Contact Insights | 09/2023 – 10/2024  
     
    1. **Automated Data Flow pipeline**
    - Automated the data flow pipeline for Optum Bank's Customer Support data. The automated system consisted of loading Customer 
    Support chats from Azure Databricks, extraction of key information using Python, SQL, and Prompt Engineering (e.g., Product, 
    Category, Sub-Category, Sentiment, Root Cause, Responsible Party, Prevention Method), and storage to Cosmos DB for further 
    analysis, which achieved an accuracy rate of approx. 96.7% in aligning with the manual entries. Scheduled a Databricks job to run at 
    regular intervals, to ensure that Cosmos DB is consistently updated with latest data.

    2. **Automated real-time Chatbot Evaluation workflow**
    - Implemented a real-time automated Evaluation Workflow using Python for calculating evaluation metrics (e.g., similarity, fluency, 
    relevance scores, etc.) to assess individual chatbot interactions as well as entire conversations, triggered via Azure Functions and 
    Azure Event Grid for event-driven processing, with results stored in Cosmos DB to enhance the quality of our chatbot responses.
    
   3. **Automated on-demand Newsletter Generation**
    - Developed an automated, on-demand Newsletter Generation system using Azure Functions, Python APIs and Prompt Engineering
    to provide summarized insights into Customer Support issues, evaluate resolution effectiveness, propose strategies to address root 
    causes, and incorporated visualizations (e.g., pie charts, bar graphs). Enabled dynamic update of Newsletter with selected chats to 
    provide dynamic insights, thus increasing stakeholder engagement by approx. 80%.
                
    4. **Automated data migration**
    - Facilitated seamless data migration across various platforms (Azure Cosmos DB, Azure Databricks, Power BI) using Python APIs, 
    ensuring 100% data integrity across platforms.

                
    ##### 🧬 PROJECT: AI Advancements | 11/2024 – Present
                
    1. **Automated Code Documentation Generation for GitHub**
    - Automated Code Documentation Generation for GitHub repositories via GitHub Action to trigger on new PRs, utilizing Python, 
    Azure Functions, and Prompt Engineering to generate documentation on existing files, as well as newly added files within the PR, 
    which is then committed back to the repository. This system ensures that the documentation for repositories is kept 100% updated, 
    while also helping new joiners understand the code within the repository.
    - Dummy Project: [https://github.com/rshdeka/GenAI-Code-Documentation-Generation](https://github.com/rshdeka/GenAI-Code-Documentation-Generation)
    
    2. **Automated FHIR Test Data creation API**
    - Automated FHIR Test Data Creation by developing a solution using Python, Azure Functions, and Prompt Engineering to generate 
    FHIR bundles including key healthcare resource-types (Patient, Condition, Encounter, Appointment, Observation, Service Request, 
    Medication Request, Allergy Intolerance). The API allows test data creation with dynamic customization by providing the ability to 
    override any desired parameter with user-provided values. This solution significantly accelerated QE test cycles by reducing manual 
    efforts for test data creation by approx. 95% (from 45 minutes to 3 minutes per patient).
    - Dummy Project: [https://github.com/rshdeka/GenAI-FHIR-Test-Data-Generation](https://github.com/rshdeka/GenAI-FHIR-Test-Data-Generation)

    3. **Agentic Framework for UI Browser Testing**
    - Automated UI Browser Testing by utilizing an Agentic AI framework with Langchain, BrowserUse, and Playwright. Leveraged
    Prompt Engineering to dynamically generate Playwright automation functions (requiring only slight modifications to accommodate 
    specific UI elements) based on test cases, and integrated with the Langchain model (AzureChatOpenAI). Utilized BrowserUse to 
    instruct the AI Agent on executing test cases, with Playwright serving as a fallback mechanism to extend the agent and facilitate 
    custom function calls. This solution increased automated test coverage by approx. 60%, reducing manual efforts by the QE team.
    - Dummy Project: [https://github.com/rshdeka/UI-Testing-Automation-PoC](https://github.com/rshdeka/UI-Testing-Automation-PoC)

                
    ### 🤖 Data Science intern
    #### 🏢 SarvM.AI System Private Limited | *July 2022 – Jan 2023*
    - Internship Certificate: [https://drive.google.com/file/d/1AKUyz2zN6XlKy-Aq9A4iLXnTn3qHEuZI/view](https://drive.google.com/file/d/1AKUyz2zN6XlKy-Aq9A4iLXnTn3qHEuZI/view)
                
    1. **Recommendation Algorithms** 
    - Analyzed and optimized recommendation algorithms for food commodities.
    
    2. **Delivery Route Optimization**
    - Determined the proper order in which packages should be allocated for delivery. Implemented K-Means 
    clustering to group delivery points based on geographical proximity, and utilized the 2-Opt algorithm to 
    iteratively improve delivery routes and find the most efficient routes for deliveries, minimizing the total 
    travel distance and re-ordering the delivery data according to the optimized routes.
    - Dummy Project: [https://github.com/rshdeka/Delivery-Order-Allocation](https://github.com/rshdeka/Delivery-Order-Allocation)
    
    3. **Market Basket Analysis**
    - Identified relationships between items in transactions and constructed recommendations based on these 
    relationships. Implemented the recommendations, leading to a 30% increase in sales from related items.
    
    4. **Customer Order Data Analysis**
    - Predicted user re-orders by employing machine learning models like: Logistic Regression, Random Forest, 
    XGBoost Classifier, and LightGBM Classifier. Achieved a re-order prediction accuracy of approx. 96% with 
    XGBoost Classifier model. Deployed the model using Flask, enabling better inventory management and customer satisfaction.
    - Dummy Project: [https://github.com/rshdeka/Instacart-Analysis](https://github.com/rshdeka/Instacart-Analysis)
                
    5. **Item Pricing Prediction**
    - Predicted prices of food items in India using historical price data for appropriate item pricing by employing 
    machine learning models like: Linear Regression, Random Forest Regressor, and XGBoost Regressor. Achieved an 
    accuracy of approx. 98% with XGBoost Regressor model.
    - Dummy Project: [https://github.com/rshdeka/Sales-predict](https://github.com/rshdeka/Sales-predict)

                
    ### 🤖 Data Science intern
    #### 🏢 Motlay Innovation Pvt Ltd | *May 2022 – July 2022*
    - Internship Certificate: [https://drive.google.com/file/d/1eYOKlux5mLjn340XIwWRBFj7no91AnT_/view](https://drive.google.com/file/d/1eYOKlux5mLjn340XIwWRBFj7no91AnT_/view)
                
    1. **Web Scraping**
    - Worked on Web Scraping in Python to extract data from various websites utilizing libraries such as BeautifulSoup, 
    ensuring clean and structured datasets for analysis.
    
    2. **Automated OCR Data Extraction**
    - Developed Python scripts to automate data extraction from Government ID cards (like Voter-ID card, Aadhar card, PAN card) 
    using OpenCV OCR, and stored the extracted information for further use.
    - Dummy Project: [https://github.com/rshdeka/VoterID-OCR](https://github.com/rshdeka/VoterID-OCR)
    
    3. **Company Data Analysis using SQL**
    - Analyzed data using SQL queries to gain insights into company sales statistics. Created an informative 
    dashboard on Power BI for providing quick sales insights to support data-driven decision making.
    - Dummy Project: [https://github.com/rshdeka/Sales-Insights](https://github.com/rshdeka/Sales-Insights)
                
    4. **Report Generation using Power BI**
    - Worked on generating insightful reports and visualizations using Power BI       
    """)


def project_page():  
    # Personal projects
    st.title("🚀 Personal Projects")  
    st.markdown("""
    🧪 **Heart Disease Prediction site**
    - Applied Machine Learning models: Logistic Regression, SVM, Random Forest Classifier, XGBoost Classifier, 
    LightGBM Classifier, and Ensemble Models to predict if a person is affected by a heart problem or not. 
    Utilized RandomizedSearchCV for hyperparameter tuning and achieved an accuracy of approx. 87% with 
    XGBoost/LightGBM Classifier models.
    - **Source code**: [https://github.com/rshdeka/Heart-disease-prediction](https://github.com/rshdeka/Heart-disease-prediction)
    - **Website**: [https://heart-disease-prediction-vp0396.streamlit.app/](https://heart-disease-prediction-vp0396.streamlit.app/)
                
    📈 **Item Pricing Prediction**
    - Applied Machine Learning models: Linear Regression, Random Forest Regressor, and XGBoost Regressor 
    to predict prices of food items in India using historical price data for appropriate item pricing. 
    Utilized RandomizedSearchCV for hyperparameter tuning and achieved an accuracy of approx. 98% with 
    XGBoost Regressor model.
    - **Source code**: [https://github.com/rshdeka/Sales-predict](https://github.com/rshdeka/Sales-predict)
                
    🤖 **Agentic Framework for UI Browser Testing**
    - Automated UI Browser Testing by utilizing an Agentic AI framework with Langchain, BrowserUse, and Playwright. 
    Leveraged Prompt Engineering to dynamically generate Playwright automation functions (requiring only slight
    modifications to accommodate specific UI elements) based on test cases, and integrated with the Langchain 
    model (AzureChatOpenAI). Utilized BrowserUse to instruct the AI Agent on executing test cases, with Playwright 
    serving as a fallback mechanism to extend the agent and facilitate custom function calls.
    - **Source code**: [https://github.com/rshdeka/UI-Testing-Automation-PoC](https://github.com/rshdeka/UI-Testing-Automation-PoC)
                
    🔄 **Delivery Route Optimization**
    - Determined the proper order in which packages should be allocated for delivery. Implemented K-Means 
    clustering to group delivery points based on geographical proximity, and utilized the 2-Opt algorithm to 
    iteratively improve delivery routes and find the most efficient routes for deliveries, minimizing the total 
    travel distance and re-ordering the delivery data according to the optimized routes.
    - **Source code**: [https://github.com/rshdeka/Delivery-Order-Allocation](https://github.com/rshdeka/Delivery-Order-Allocation)
    """)


# Sidebar for navigation  
st.sidebar.title("Navigation")  
page_selection = st.sidebar.radio("Go to", ["Main Page", "Experience Page", "Personal Projects Page"])  

# Render the selected page  
if page_selection == "Main Page":  
    main_page()  
elif page_selection == "Experience Page":  
    experience_page()  
elif page_selection == "Personal Projects Page":
    project_page()