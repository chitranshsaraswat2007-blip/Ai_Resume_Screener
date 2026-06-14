
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_resume_pdf(filename, text_content):
    """
    Creates a basic PDF file containing the specified text content line-by-line.
    """
    try:
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        y = height - 50 # Start near the top
        
        # Set font and size
        c.setFont("Helvetica", 10)
        
        # Write text line-by-line
        for line in text_content.split('\n'):
            # If we run out of vertical space, start a new page
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = height - 50
            c.drawString(50, y, line)
            y -= 15 # Move down for the next line
            
        c.save()
        print(f"Successfully generated: {filename}")
    except Exception as e:
        print(f"Error generating PDF {filename}: {e}")

def main():
    # Target directory for sample resumes
    target_dir = os.path.join(os.path.dirname(__file__), "sample_resumes")
    os.makedirs(target_dir, exist_ok=True)
    
    # 1. John Doe - Python Developer Resume Content
    python_resume = """John Doe
Email: john.doe@email.com | Phone: 123-456-7890 | GitHub: github.com/johndoe
Location: San Francisco, CA

Professional Summary:
Enthusiastic and results-driven Software Engineer with 4+ years of professional backend development experience.
Specialized in building scalable web applications and REST APIs using Python and associated frameworks.

Technical Skills:
- Programming Languages: Python, JavaScript, SQL, Bash
- Frameworks & Libraries: Django, Flask, FastAPI, NumPy, Pandas
- Databases: PostgreSQL, MySQL, Redis, SQLite
- Tools & DevOps: Git, Docker, GitHub Actions, AWS, Linux, RESTful Web Services
- Methodologies: Agile development, Scrum, Test-Driven Development (TDD)

Professional Experience:
Senior Software Engineer | Tech Corp (2022 - Present)
- Designed and built scalable web applications using Python and Django.
- Developed robust RESTful APIs for mobile and web clients, serving 10k+ daily active users.
- Integrated database storage with PostgreSQL and optimized complex SQL queries, improving load times by 30%.
- Containerized development and production environments using Docker and Docker Compose.
- Mentored junior python developers and conducted code reviews to maintain high quality standards.

Python Developer | Web Solutions Inc (2020 - 2022)
- Created backend services using Python, Flask, and SQLite.
- Collaborated with front-end developers to integrate client-side React code with backend APIs.
- Maintained CI/CD pipelines for automated testing and deployment.
- Wrote clean, readable, and maintainable code adhering to PEP 8 guidelines.

Education:
Bachelor of Science in Computer Science | State University (2016 - 2020)
"""

    # 2. Jane Smith - Data Scientist Resume Content
    ds_resume = """Jane Smith
Email: jane.smith@email.com | Phone: 987-654-3210 | LinkedIn: linkedin.com/in/janesmith
Location: New York, NY

Professional Summary:
Passionate Data Scientist with 3+ years of experience in data analysis, statistical modeling, and machine learning.
Skilled in transforming raw complex data into actionable business insights and predictive systems.

Technical Skills:
- Languages: Python, R, SQL, MATLAB
- Machine Learning & Deep Learning: Scikit-learn, TensorFlow, Keras, PyTorch, XGBoost
- Data Processing: Pandas, NumPy, SciPy, Apache Spark
- Visualization & BI: Tableau, Matplotlib, Seaborn, PowerBI
- Database: MySQL, MongoDB, PostgreSQL
- Environments: Jupyter Notebooks, Git, Docker, Google Colab

Professional Experience:
Data Scientist | Analytics Inc (2021 - Present)
- Developed and deployed predictive machine learning models (random forests, gradient boosting) using Python and Scikit-learn.
- Preprocessed, cleaned, and engineered features from large unstructured datasets of 1M+ records using Pandas and NumPy.
- Built interactive dashboards in Tableau to display model performance metrics and business KPIs to executives.
- Performed A/B testing and statistical analysis to evaluate product features, driving a 15% increase in user retention.
- Collaborated with software engineers to integrate ML models into production API endpoints.

Data Analyst | Retail Solutions Corp (2019 - 2021)
- Performed statistical analysis and created SQL queries to extract data insights from business databases.
- Created Python scripts for automated data cleaning, validation, and scheduled reporting.
- Visualized sales data using Seaborn and Matplotlib to identify market trends.

Education:
Master of Science in Data Science | Tech Institute (2017 - 2019)
Bachelor of Science in Mathematics | State College (2013 - 2017)
"""

    # 3. Robert Johnson - Sales Manager Resume Content (Should rank low for tech roles)
    sales_resume = """Robert Johnson
Email: robert.johnson@email.com | Phone: 555-019-2834
Location: Chicago, IL

Professional Summary:
High-performing Sales Manager with 7+ years of experience in B2B sales, account management, and strategic negotiations.
Proven track record of building successful sales teams, expanding customer bases, and exceeding revenue targets.

Skills & Core Competencies:
- Sales Strategy & Business Development
- B2B Sales & Account Management
- Lead Generation & Pipeline Management
- Client Relationship Management (CRM)
- Contract Negotiation & Closing
- Team Leadership, Mentoring & Training
- Budgeting & Revenue Forecasting

Professional Experience:
Sales Manager | Global Traders Inc (2021 - Present)
- Led and mentored a team of 10 sales executives, increasing annual sales revenue by 25% ($1.2M growth).
- Managed key corporate accounts, ensuring high customer satisfaction and a 95% client retention rate.
- Negotiated high-value B2B contracts with corporate partners and distributors.
- Utilized CRM software (Salesforce) to track leads, pipeline stages, conversion rates, and forecasts.
- Conducted regular market research to identify new product opportunities and competitor activities.

Senior Sales Executive | Market Masters Corp (2018 - 2021)
- Generated new business leads through cold calling, email campaigns, and industry networking.
- Exceeded personal sales quotas by 15-20% consecutively for 6 quarters.
- Conducted product demonstrations and delivered persuasive sales presentations to C-level executives.

Education:
Bachelor of Business Administration (BBA) | Business School (2014 - 2018)
"""

    # Generate the valid PDFs
    create_resume_pdf(os.path.join(target_dir, "resume_john_doe_python_dev.pdf"), python_resume)
    create_resume_pdf(os.path.join(target_dir, "resume_jane_smith_data_scientist.pdf"), ds_resume)
    create_resume_pdf(os.path.join(target_dir, "resume_robert_sales_manager.pdf"), sales_resume)
    
    # 4. Generate Corrupted PDF (a plain text file containing garbage, disguised as a PDF)
    corrupted_path = os.path.join(target_dir, "resume_corrupted.pdf")
    try:
        with open(corrupted_path, "w", encoding="utf-8") as f:
            f.write("This is a corrupted PDF file. It does not follow PDF formatting rules and should raise a PdfReadError when processed.")
        print(f"Successfully generated: {corrupted_path} (intended corrupted file)")
    except Exception as e:
        print(f"Error generating corrupted file: {e}")

if __name__ == "__main__":
    main()
