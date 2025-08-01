import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Alireza Babazadeh Zarei - AI Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .skill-badge {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-weight: bold;
    }
    
    .project-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .contact-info {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    
    .section-header {
        color: #667eea;
        border-bottom: 2px solid #667eea;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    .achievement-highlight {
        background: linear-gradient(45deg, #ffeaa7, #fab1a0);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        font-weight: bold;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🚀 Navigation")
sections = ["Home", "About", "Skills", "Projects", "Education", "Achievements", "Contact"]
selected_section = st.sidebar.selectbox("Go to:", sections)

# Main Header
st.markdown("""
<div class="main-header">
    <h1>🤖 Alireza Babazadeh Zarei</h1>
    <h3>LLM Engineer & Creative Problem Solver</h3>
    <p>"A creative person passionate about learning more and developing artificial intelligence models"</p>
</div>
""", unsafe_allow_html=True)

if selected_section == "Home":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image("https://media.licdn.com/dms/image/v2/D4D03AQFi91Qj6Gy0cQ/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1725458495114?e=1756944000&v=beta&t=j_puxo5YtRi0csnyVTWpGscA6qiWNq-H7789A5yW2c4")
    with col2:
        st.markdown("## 🎯 Welcome to My AI Portfolio")
        st.write("""
        I'm a passionate LLM engineer with expertise in creating most creative RAG's, Finetuning and developing cutting-edge machine learning models 
        and innovative solutions. With experience in deep learning, computer vision, and natural language 
        processing, I'm dedicated to pushing the boundaries of artificial intelligence.
        """)
        
        st.markdown("### 🏆 Quick Highlights")
        highlights = [
            "🥇 Gold Medal Winner in International Competitions",
            "🥈 2 Silver Medals in AI Competitions", 
            "🤖 Expert in Deep Learning & Neural Networks",
            "💬 RAG & Chatbot Specialist",
            "🔬 Focused on ML Model Development & Optimization"
        ]
        
        for highlight in highlights:
            st.markdown(f'<div class="achievement-highlight">{highlight}</div>', unsafe_allow_html=True)

elif selected_section == "About":
    st.markdown('<h2 class="section-header">👨‍💻 About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        I am a creative and passionate engineer dedicated to learning and developing artificial intelligence models. 
        My journey in AI has been marked by continuous learning, innovative projects, and competitive achievements.
        
        My expertise spans across various domains of machine learning and deep learning, with a particular focus on:
        - **RAG Creation**: Creating and optimizing different RAG Services for real-world applications
        - **Model Development**: Creating and optimizing ML models for real-world applications
        - **Deep Learning**: Implementing state-of-the-art neural network architectures
        - **Competition Success**: Proven track record in international AI competitions
        - **Innovation**: Developing creative solutions to complex problems
        """)
    
    with col2:
        st.markdown("""
        <div class="contact-info">
            <h4>📊 Profile Stats</h4>
            <p><strong>Kaggle:</strong> kaggle.com/inv-alizare</p>
            <p><strong>Location:</strong> Iran</p>
            <p><strong>Focus:</strong> AI/ML Research</p>
            <p><strong>Experience:</strong> Multiple Projects</p>
        </div>
        """, unsafe_allow_html=True)

elif selected_section == "Skills":
    st.markdown('<h2 class="section-header">🛠️ Technical Skills</h2>', unsafe_allow_html=True)
    
    # Programming Languages
    st.subheader("💻 Programming Languages")
    prog_langs = ["Python", "C++", "Java (Basic)", "English"]
    cols = st.columns(len(prog_langs))
    for i, lang in enumerate(prog_langs):
        with cols[i]:
            st.markdown(f'<div class="skill-badge">{lang}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Machine Learning Models
    st.subheader("🤖 Machine Learning Expertise")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Traditional ML Models:**")
        traditional_ml = [
            "Linear Regression", "Random Forest", "Classification & Regression Trees",
            "Support Vector Machine (SVM)", "K-Nearest Neighbors (KNN)",
            "Supervised Learning", "Unsupervised Learning", "Reinforcement Learning"
        ]
        for skill in traditional_ml:
            st.markdown(f"• {skill}")
    
    with col2:
        st.markdown("**Deep Learning Models:**")
        deep_learning = [
            "Different Large Language Models (LLM's)","Group Relation Policy Optimization(GRPO)", "Convolutional Neural Networks (CNNs)", "Long Short Term Memory (LSTMs)",
            "Recurrent Neural Networks (RNNs)", "Generative Adversarial Networks (GANs)",
            "Multilayer Perceptrons (MLPs)", "Transformer", "Vision Transformer (ViT)"
        ]
        for skill in deep_learning:
            st.markdown(f"• {skill}")
    
    st.markdown("---")
    
    # Soft Skills with visualization
    st.subheader("🎯 Soft Skills")
    soft_skills = ["Problem Solving", "Creativity", "Negotiation", "Critical Thinking", "Management Skills"]
    
    # Create a radar chart for soft skills
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=[9, 10, 8, 9, 8],  # Skill levels (out of 10)
        theta=soft_skills,
        fill='toself',
        name='Skill Level',
        line_color='#667eea'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10])
        ),
        showlegend=False,
        title="Soft Skills Assessment",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif selected_section == "Projects":
    st.markdown('<h2 class="section-header">🚀 Projects & Experience</h2>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "🤖 Ravansha App",
            "competition": "GenX Competitions 2023",
            "description": "Developed an innovative AI application for the GenX competition, showcasing advanced machine learning capabilities."
        },
        {
            "title": "💼 Catalyst Careers Chatbot",
            "competition": "Seeds4Future Competitions",
            "description": "Created an intelligent career guidance chatbot using RAG (Retrieval-Augmented Generation) technology to help users with career decisions."
        },
        {
            "title": "❤️ ECG/AI System",
            "competition": "GenX Competitions 2024",
            "description": "Developed an AI-powered ECG analysis system for medical diagnostics, combining deep learning with healthcare applications."
        },
        {
            "title": "🏥 Cervical Cancer Advisor",
            "competition": "KeyvanLabs",
            "description": "Built an AI advisory system for cervical cancer screening and diagnosis, contributing to healthcare AI solutions."
        },
        {
            "title": "🎭 Character.ai Series",
            "competition": "Personal Project",
            "description": "Created multiple AI characters including Chandler Bing-SagGpt and AliZare AI, accessible at inv-Acw, demonstrating expertise in conversational AI."
        }
    ]
    
    for project in projects:
        st.markdown(f"""
        <div class="project-card">
            <h4>{project['title']}</h4>
            <p><strong>Competition/Platform:</strong> {project['competition']}</p>
            <p>{project['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # RAG & Chatbot Experience Section
    st.markdown("### 💬 RAG & Chatbot Specialization")
    st.write("""
    I have extensive experience in developing Retrieval-Augmented Generation (RAG) systems and chatbots:
    - **Advanced NLP**: Implementation of state-of-the-art language models
    - **Context Retrieval**: Efficient information retrieval systems
    - **Conversational AI**: Creating engaging and helpful AI assistants
    - **Domain Adaptation**: Customizing chatbots for specific industries and use cases
    """)

elif selected_section == "Education":
    st.markdown('<h2 class="section-header">🎓 Education & Courses</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏫 Formal Education")
        st.markdown("""
        <div class="project-card">
            <h4>🖥️ Computer Engineering - Software</h4>
            <p><strong>Institution:</strong> Azad University - Rasht</p>
            <p>Comprehensive education in software engineering with focus on computer science fundamentals and programming.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📚 Professional Courses")
        courses = [
            {
                "title": "Machine Learning Expertise",
                "provider": "Coursera",
                "description": "Advanced machine learning concepts and practical applications"
            },
            {
                "title": "AI from the Neurosurgeon's Perspective",
                "provider": "Shahid Beheshti University",
                "description": "Unique perspective on AI applications in medical field"
            },
            {
                "title": "Artificial Intelligence Hackathon",
                "provider": "Irancell Labs",
                "description": "Intensive hands-on experience in AI development"
            }
        ]
        
        for course in courses:
            st.markdown(f"""
            <div class="project-card">
                <h5>{course['title']}</h5>
                <p><strong>By:</strong> {course['provider']}</p>
                <p>{course['description']}</p>
            </div>
            """, unsafe_allow_html=True)

elif selected_section == "Achievements":
    st.markdown('<h2 class="section-header">🏆 Achievements & Recognition</h2>', unsafe_allow_html=True)
    
    st.markdown("### 🥇 Competition Medals")
    st.markdown("""
    <div class="achievement-highlight">
        🥇 1 Gold Medal - International Inventions Competition 2024
    </div>
    <div class="achievement-highlight">
        🥈 2 Silver Medals - International Inventions Competition 2023-2021
    </div>
    <div class="achievement-highlight">
        🥈 1 special creativity award - Idea-ara Azad university Competitions 2019
    </div>
    <div class="achievement-highlight">
         Finalist - GenX RAG creating Competition 2023
    </div>
    """, unsafe_allow_html=True)
    
    
    st.markdown("### 🌟 Professional Recognition")
    st.write("""
    - **International Recognition**: Multiple medals in international invention competitions
    - **Innovation Leadership**: Proven track record of creating award-winning AI solutions
    - **Technical Excellence**: Demonstrated expertise across multiple AI domains
    - **Community Impact**: Contributions to healthcare and career guidance through AI
    """)

elif selected_section == "Contact":
    st.markdown('<h2 class="section-header">📬 Get In Touch</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h4>📧 Email</h4>
            <p>inv.alirezababazadehzarei@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-info">
            <h4>📱 Phone</h4>
            <p>+98-9034101611</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="contact-info">
            <h4>🔗 Social</h4>
            <p>
                <a href="https://www.linkedin.com/in/inv-alizare" target="_blank" style="color:white;">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="linkedin" width="25" height="25"/>
                    linkedin.com/in/inv-alizare
                </a>
            </p>
            <p>
                <a href="https://t.me/baaabaei" target="_blank" style="color:white;">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/telegram/telegram-original.svg" alt="telegram" width="25" height="25"/>
                    @baaabaei
                </a>
            </p>
            <p>
                <a href="https://www.kaggle.com/inv-alizare" target="_blank" style="color:white">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kaggle/kaggle-original.svg" alt="kaggle" width="25" height="25"/>
                    kaggle.com/inv-alizare
                </a>
            </p>
            <p>
                <a href="https://github.com/baaabaei" target="_blank" style="color:white;">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="github" width="25" height="25"/>
                    github.com/baaabaei
                </a>
            </p>
        </div>
        """, unsafe_allow_html=True)        


    st.markdown("---")
    
    st.markdown("### 🤝 Let's Collaborate!")
    st.write("""
    I'm always interested in discussing new opportunities, innovative projects, and collaborations in AI/ML. 
    Whether you're looking for:
    - **AI Model Development**
    - **Chatbot & RAG Solutions**
    - **Research Collaboration**
    - **Consulting Services**
    
    Feel free to reach out! I'm passionate about applying AI to solve real-world problems and would love to 
    discuss how we can work together.
    """)
    
    # Contact form
    st.markdown("### 📝 Quick Contact Form")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        subject = st.selectbox("Subject", ["General Inquiry", "Project Collaboration", "Job Opportunity", "Research Collaboration"])
        message = st.text_area("Message")
        
        if st.form_submit_button("Send Message"):
            st.success("Thank you for your message! I'll get back to you soon.")
            st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🤖 Alireza Babazadeh Zarei | AI/ML Engineer | Passionate about Innovation</p>
    <p>Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)