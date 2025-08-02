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
        # Education
        st.header("🎓 Education")
        st.markdown("""  
        - **Bachelor of Technology**   
          **National Institute of Technology Silchar** | 07/2019 - 05/2023           
          CGPA: 8.68/10
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
    - SQL, Azure Cosmos DB, Azure Databricks
    ##### 🤖 **GenAI Technologies**
    - Prompt Engineering, LLMs, RAG, Langchain, Agentic AI (BrowserUse + Playwright)
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

    # Certifications  
    st.header("🏆 Certifications")  
    st.markdown("""  
    - **Microsoft Azure AI Engineer Associate Certification** | [AI-102](https://learn.microsoft.com/api/credentials/share/en-us/RajashriDeka/B79DC6EFCDC958D4?sharingId=D27E7EB37FE3D980)  
    Microsoft | June 2025
    
    - **Microsoft Azure AI Fundamentals Certification** | [AI-900](https://learn.microsoft.com/api/credentials/share/en-us/RajashriDeka/902DB6264E1A83D9?sharingId=D27E7EB37FE3D980)        
    Microsoft | Feb 2025
    
    - **Microsoft Azure Fundamentals Certification** | [AZ-900](https://learn.microsoft.com/api/credentials/share/en-us/RajashriDeka/86A307FEE136E4EE?sharingId=D27E7EB37FE3D980)          
    Microsoft | Sept 2024
                
    - **Google Data Analytics Professional Certificate** | [Google Data Analytics Certificate](https://www.credly.com/badges/49031355-8f5e-4ffd-9c19-fca6734edfc2/linked_in_profile)     
    Coursera | Aug 2022
                
    - **SQL Certificate**
    [HackerRank](https://www.hackerrank.com/certificates/b9373c15e527) | July 2022
    
    - **Python Certificate**
    [HackerRank](https://www.hackerrank.com/certificates/b632db330fa8) | June 2021
    """) 
    
    # Get In Touch section  
    st.header("📞 Get In Touch")   
    st.markdown("""
    - 📱 Phone: +91-6000797881 
    - 📧 Email: [rajashrideka07@gmail.com](mailto:rajashrideka07@gmail.com)  
    - 💼 LinkedIn: [https://www.linkedin.com/in/rajashrideka](https://www.linkedin.com/in/rajashrideka)
    - 💼 GitHub: [https://github.com/rshdeka](https://github.com/rshdeka)
    """)
    # Email button styled as a link
    st.markdown(  
        f'<a href="mailto:rajashrideka07@gmail.com" style="display:inline-block; padding: 0.5em 1em; color: white; background-color: #007BFF; text-decoration: none; border-radius: 4px;">📧 Email Me</a>',  
        unsafe_allow_html=True  
    )  
    

def experience_page():  
    # Work Experience  
    st.title("💼 Work Experience")  
    st.markdown("""
    ### 🧑‍💻 Software Engineer 
    #### 🏢 Optum (UnitedHealth Group) | *Sept 2023 – Present* 

    #### 🧬 PROJECT: Contact Insights | 09/2023 – 10/2024  
     
    ##### Automated Data Flow pipeline
    - **Tech Stack**: Python, SQL, Prompt Engineering, Azure Cosmos DB, Azure Databricks.
    - **Description**: Automated the data flow pipeline for Optum Bank's Customer Support data. The automated system consisted of loading
    Customer Support chats from Azure Databricks, extraction of key information using Python, SQL, and Prompt Engineering (e.g., Product,
    Category, Sub-Category, Sentiment, Root Cause, Responsible Party, Prevention Method), and storage to Cosmos DB for further analysis.
    Scheduled a Databricks job to run at regular intervals, to ensure that Cosmos DB is consistently updated with latest data.
    - **Benefit**: Enhanced operational efficiency by automating data processing and reducing manual workload for analysis. 
    - **Accuracy**: Achieved an accuracy rate of approx. 96.7% in aligning with the manual entries.

    ##### Automated real-time Chatbot Evaluation workflow
    - **Tech Stack**: Python, Prompt Engineering, Azure Functions, Azure Cosmos DB, Azure Event Grid.  
    - **Description**: Implemented a real-time automated Evaluation Workflow using Python for calculating evaluation metrics (e.g., similarity, 
    fluency, relevance scores, etc.) to assess individual chatbot interactions as well as entire conversations, triggered via Azure Functions 
    and Azure Event Grid for event-driven processing, with results stored in Cosmos DB to enhance the quality of our chatbot responses.
    - **Benefit**: Enhanced the quality of chatbot responses, improving customer satisfaction.
    
   ##### Automated on-demand Newsletter Generation
    - **Tech Stack**: Python, Prompt Engineering, Azure Functions.
    - **Description**: Developed an automated, on-demand Newsletter Generation system using Azure Functions, Python APIs and Prompt Engineering
    to provide summarized insights into Customer Support issues, evaluate resolution effectiveness, propose strategies to address root 
    causes, and incorporated visualizations (e.g., pie charts, bar graphs). Enabled dynamic update of Newsletter with selected chats to 
    provide dynamic insights.
    - **Benefit**: Increased stakeholder engagement by approx. 80%, facilitating better decision-making with timely insights.
                
    ##### Automated data migration
    - **Tech Stack**: Python, Azure Cosmos DB, Azure Databricks, Power BI
    - **Description**: Facilitated seamless data migration across various platforms (Azure Cosmos DB, Azure Databricks, Power BI) using Python APIs.
    - **Benefit**: Maintained 100% data integrity during migrations, ensuring reliable data for operations.

                
    #### 🧬 PROJECT: AI Advancements | 11/2024 – Present
                
    ##### Automated Code Documentation Generation for GitHub
    - **Tech Stack**: Python, Prompt Engineering, Azure Functions, GitHub Actions.  
    - **Description**: Automated Code Documentation Generation for GitHub repositories via GitHub Action to trigger on new PRs, utilizing Python, 
    Azure Functions, and Prompt Engineering to generate documentation on existing files, as well as newly added files within the PR, which is 
    then committed back to the repository.
    - **Benefit**: Ensures 100% up-to-date documentation, and aiding new joiners in understanding the codebase efficiently.
    - [Dummy Project](https://github.com/rshdeka/GenAI-Code-Documentation-Generation)
    
    ##### Automated FHIR Test Data creation API
    - **Tech Stack**: Python, Prompt Engineering, Azure Functions. 
    - **Description**: Automated FHIR Test Data Creation by developing a solution using Python, Azure Functions, and Prompt Engineering to 
    generate FHIR bundles including key healthcare resource-types (Patient, Condition, Encounter, Appointment, Observation, Service Request, 
    Medication Request, Allergy Intolerance). The API allows test data creation with dynamic customization by providing the ability to 
    override any desired parameter with user-provided values.
    - **Benefit**: Reduced manual test data creation time by approx. 95% (from 45 minutes to 3 minutes per patient), speeding up test cycles and enhancing productivity.
    - [Dummy Project](https://github.com/rshdeka/GenAI-FHIR-Test-Data-Generation)

    ##### Agentic Framework for UI Browser Testing
    - **Tech Stack**: Prompt Engineering, Langchain, BrowserUse, Playwright.
    - **Description**: Automated UI Browser Testing by utilizing an Agentic AI framework with Langchain, BrowserUse, and Playwright. 
    Leveraged Prompt Engineering to dynamically generate Playwright automation functions (requiring only slight modifications to accommodate 
    specific UI elements) based on test cases, and integrated with the Langchain model (AzureChatOpenAI). Utilized BrowserUse to instruct the 
    AI Agent on executing test cases, with Playwright serving as a fallback mechanism to extend the agent and facilitate custom function calls.
    - **Benefit**: Increased automated test coverage by approx. 60%, reducing manual testing efforts significantly.
    - [Dummy Project](https://github.com/rshdeka/UI-Testing-Automation-PoC)

                
    ### 🤖 Data Science intern
    #### 🏢 SarvM.AI System Private Limited | *July 2022 – Jan 2023*
    [Internship Certificate](https://drive.google.com/file/d/1AKUyz2zN6XlKy-Aq9A4iLXnTn3qHEuZI/view)
                
    ##### Recommendation Algorithms
    - **Description**: Analyzed and optimized recommendation algorithms for food commodities.
    - **Benefit**: Improved recommendation accuracy, enhancing user experience.  
    
    ##### Delivery Route Optimization
    - **Techniques**: Implemented K-Means clustering and the 2-Opt algorithm.  
    - **Description**: Determined the proper order in which packages should be allocated for delivery. Implemented K-Means clustering to group
    delivery points based on geographical proximity, and utilized the 2-Opt algorithm to iteratively improve delivery routes and find the most
    efficient routes for deliveries, and finally re-ordering the delivery data according to the optimized routes.
    - **Benefit**: Minimized total travel distance, optimizing delivery schedules. 
    - [Dummy Project](https://github.com/rshdeka/Delivery-Order-Allocation)
    
    ##### Market Basket Analysis
    - **Description**: Identified relationships between items in transactions and constructed recommendations based on these relationships.
    - **Benefit**: Boosted related item sales by approx. 30%.
    
    ##### Customer Order Data Analysis
    - **Models Used**: Logistic Regression, Random Forest, XGBoost Classifier, and LightGBM Classifier.
    - **Description**: Predicted user re-orders by employing Machine Learning models, and deployed the model using Flask.
    - **Benefit**: Enabled better inventory management leading to customer satisfaction.
    - **Accuracy**: Achieved a re-order prediction accuracy of approx. 96% with XGBoost Classifier model. 
    - [Dummy Project](https://github.com/rshdeka/Instacart-Analysis)
                
    ##### Item Pricing Prediction
    - **Models Used**: Linear Regression, Random Forest Regressor, and XGBoost Regressor.  
    - **Description**: Predicts prices of food items in India using historical data for appropriate item pricing.  
    - **Accuracy**: Utilized RandomizedSearchCV for hyperparameter tuning, and achieved approx. 98% accuracy with XGBoost Regressor model.  
    - [Dummy Project](https://github.com/rshdeka/Sales-predict)

                
    ### 🤖 Data Science intern
    #### 🏢 Motlay Innovation Pvt Ltd | *May 2022 – July 2022*
    [Internship Certificate](https://drive.google.com/file/d/1eYOKlux5mLjn340XIwWRBFj7no91AnT_/view)
                
    ##### Web Scraping
    - **Tech Stack**: Python, BeautifulSoup.
    - **Description**: Extracted data from various websites utilizing libraries such as BeautifulSoup.
    - **Benefit**: Provided clean and structured datasets for analysis.
    
    ##### Automated OCR Data Extraction
    - **Tech Stack**: Python, OpenCV OCR.
    - **Description**: Automated data extraction from Government ID cards (like Voter-ID card, Aadhar card, PAN card) using OpenCV OCR.
    - **Benefit**: Efficiently processed ID data, facilitating faster data retrieval.
    - [Dummy Project](https://github.com/rshdeka/VoterID-OCR)
    
    ##### Company Data Analysis using SQL
    - **Tech Stack**: Python, SQL, Power BI.
    - **Description**: Analyzed data using SQL queries to gain insights into company sales statistics, and created an informative dashboard on Power BI.
    - **Benefit**: Supported data-driven decision-making with informative dashboard providing quick sales insights.
    - [Dummy Project](https://github.com/rshdeka/Sales-Insights)
                
    ##### Report Generation using Power BI
    - **Description**: Generated insightful reports and visualizations using Power BI.
    - **Benefit**: Enabled quick and informed decision-making through visual reports.  
    """)


def project_page():  
    # Personal projects
    st.title("🚀 Personal Projects")  
    button_style = "display:inline-block; padding: 0.5em 1em; color: white; background-color: #007BFF; text-decoration: none; border-radius: 4px;"
    st.markdown("""
    #### 🧪 **Heart Disease Prediction**
    - **Models Used**: Logistic Regression, SVM, Random Forest Classifier, XGBoost Classifier, LightGBM Classifier, and Ensemble Models.  
    - **Description**: Predicts if a person is affected by heart disease using Machine Learning models.  
    - **Accuracy**: Utilized RandomizedSearchCV for hyperparameter tuning, and achieved approx. 87% accuracy with XGBoost/LightGBM Classifier models.
    """) 
    st.markdown(f'<a href="https://github.com/rshdeka/Heart-disease-prediction" style="{button_style}">Source Code</a>', unsafe_allow_html=True)  
    st.markdown(f'<a href="https://heart-disease-prediction-vp0396.streamlit.app/" style="{button_style}">Website</a>', unsafe_allow_html=True)  

    st.markdown("""         
    #### 📈 **Item Pricing Prediction**
    - **Models Used**: Linear Regression, Random Forest Regressor, and XGBoost Regressor.  
    - **Description**: Predicts prices of food items in India using historical data for appropriate item pricing.  
    - **Accuracy**: Utilized RandomizedSearchCV for hyperparameter tuning, and achieved approx. 98% accuracy with XGBoost Regressor model.  
    """) 
    st.markdown(f'<a href="https://github.com/rshdeka/Sales-predict" style="{button_style}">Source Code</a>', unsafe_allow_html=True)  
                
    st.markdown("""
    #### 🤖 **Agentic Framework for UI Browser Testing**
    - **Framework**: Utilizes an Agentic AI framework with Langchain (AzureChatOpenAI), BrowserUse, and Playwright.  
    - **Description**: Automates UI Browser Testing through dynamically generated Playwright functions (requiring only slight modifications 
    to accommodate specific UI elements) based on test cases.  
    - **Integration**: Integrated with Langchain model (AzureChatOpenAI), using BrowserUse for AI Agent test execution, and Playwright 
    serving as a fallback mechanism to extend the agent and facilitate custom function calls.
    """) 
    st.markdown(f'<a href="https://github.com/rshdeka/UI-Testing-Automation-PoC" style="{button_style}">Source Code</a>', unsafe_allow_html=True)  
                
    st.markdown("""
    #### 🔄 **Delivery Route Optimization**
    - **Techniques**: Implemented K-Means clustering and the 2-Opt algorithm.  
    - **Description**: Optimizes delivery routes, by implementing K-Means clustering to group delivery points based on geographical proximity,
    and utilized the 2-Opt algorithm to iteratively improve delivery routes and find the most efficient routes for deliveries, minimizing the 
    total travel distance and re-ordering the delivery data according to the optimized routes.
    """) 
    st.markdown(f'<a href="https://github.com/rshdeka/Delivery-Order-Allocation" style="{button_style}">Source Code</a>', unsafe_allow_html=True)


# Top navigation bar 
tab1, tab2, tab3 = st.tabs(["# **Main Page**", "# **Experience Page**", "# **Personal Projects Page**"])  
# Render the selected page  
with tab1:  
    main_page()  
with tab2:  
    experience_page()  
with tab3:

    project_page()
