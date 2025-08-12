AI Portfolio with Streamlit

This repository contains the source code for my personal AI portfolio website, built using Python and the Streamlit framework. The application is designed to be a clean, interactive, and single-page web app that showcases my skills, projects, achievements, and contact information in the field of Artificial Intelligence and Machine Learning.

(Note: You should replace the URL above with a real screenshot of your running application.)

🚀 Features

Interactive UI: A modern and responsive user interface built entirely in Streamlit.

Single-Page Layout: All information is organized into sections accessible from a persistent sidebar navigation menu.

Dynamic Sections: The portfolio includes the following sections:

Home: A welcoming introduction with a profile picture and key highlights.

About Me: A detailed professional summary and stats.

Technical Skills: A categorized list of programming languages, ML models, and soft skills.

Projects & Experience: A showcase of key projects with descriptions and links.

Education & Courses: Information on formal education and professional certifications.

Achievements: A list of awards and recognitions.

Contact: Contact details, social media links, and a functional contact form.

Custom Styling: Uses custom CSS to enhance the visual appeal and create a unique, professional look.

Easy to Customize: The code is well-structured, making it simple to update with your own personal information.

🛠️ Built With

Python: The core programming language.

Streamlit: The open-source app framework for building the web application.

HTML/CSS: For custom styling and layout enhancements.

⚙️ Getting Started

To get a local copy up and running, follow these simple steps.

Prerequisites

Make sure you have Python (3.7+) and pip installed on your system.

Installation

Clone the repository:

code
Sh
download
content_copy
expand_less

git clone https://github.com/Baaabaei/your-repo-name.git
cd your-repo-name

Create a requirements.txt file:
Create a new file named requirements.txt in the root of your project directory and add the following line:

code
Code
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
streamlit

Install the required packages:

code
Sh
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
pip install -r requirements.txt
Running the Application

Navigate to your project directory in your terminal.

Run the Streamlit app:

code
Sh
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
streamlit run your_app_file_name.py

(Replace your_app_file_name.py with the actual name of your Python script.)

The application will open automatically in your default web browser at http://localhost:8501.

✨ How to Customize

This portfolio is designed to be easily customized. To add your own information, simply edit the Python script:

Personal Information: Update variables in the "About Me" and header sections with your details.

Profile Picture: Change the URL in the st.image() call within the "Home" section.

Skills: Modify the Python lists (prog_langs, traditional_ml, deep_learning, etc.) in the "Skills" section.

Projects: Edit the projects list of dictionaries in the "Projects" section to reflect your work.

Education & Achievements: Update the corresponding st.markdown() blocks with your credentials and awards.

Contact Information: Replace the email, phone number, and social media links in the "Contact" section.

📫 Contact

Alireza Babazadeh Zarei

Email: inv.alirezababazadehzarei@gmail.com

LinkedIn: linkedin.com/in/inv-alizare

GitHub: github.com/Baaabaei

Kaggle: kaggle.com/inv-alizare
