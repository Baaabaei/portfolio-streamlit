import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Alireza Babazadeh Zarei - AI/ML Engineer",
    page_icon=":material/psychology:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS styling
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }
    
    .professional-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 3rem 2rem;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .professional-header h1 {
        font-size: 2.5rem;
        font-weight: 300;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }
    
    .professional-header h3 {
        font-weight: 300;
        opacity: 0.9;
        margin-bottom: 1rem;
    }
    
    .professional-header p {
        font-size: 1.1rem;
        opacity: 0.8;
        max-width: 800px;
        margin: 0 auto;
    }
    
    .section-container {
        background: white;
        padding: 2rem;
        margin: 1rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #2a5298;
    }
    
    .section-title {
        color: #1e3c72;
        font-size: 1.8rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #e0e6ed;
        padding-bottom: 0.5rem;
    }
    
    .skill-category {
        background: #f8f9fa;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 6px;
        border: 1px solid #e9ecef;
    }
    
    .skill-category h4 {
        color: #495057;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .skill-item {
        background: #2a5298;
        color: white;
        padding: 0.4rem 0.8rem;
        margin: 0.3rem 0.3rem 0.3rem 0;
        border-radius: 4px;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    .project-card {
        background: #f8f9fa;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 6px;
        border: 1px solid #dee2e6;
        transition: all 0.2s ease;
    }
    
    .project-card:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }
    
    .project-title {
        color: #1e3c72;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .project-meta {
        color: #6c757d;
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 0.8rem;
    }
    
    .project-description {
        color: #495057;
        line-height: 1.6;
    }
    
    .achievement-card {
        background: linear-gradient(135deg, #ffc107, #ff8f00);
        color: white;
        padding: 1.5rem;
        border-radius: 6px;
        text-align: center;
        margin: 1rem 0;
        font-weight: 600;
    }
    
    .contact-card {
        background: #1e3c72;
        color: white;
        padding: 1.5rem;
        border-radius: 6px;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .contact-card h4 {
        margin-bottom: 0.5rem;
        opacity: 0.9;
    }
    
    .stats-card {
        background: white;
        padding: 1.5rem;
        border-radius: 6px;
        text-align: center;
        border: 2px solid #e9ecef;
        margin: 0.5rem 0;
    }
    
    .stats-number {
        font-size: 2rem;
        font-weight: 700;
        color: #2a5298;
        display: block;
    }
    
    .stats-label {
        color: #6c757d;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .sidebar .sidebar-content {
        background: white;
    }
    
    .education-item {
        background: white;
        padding: 1.5rem;
        border-radius: 6px;
        border: 1px solid #dee2e6;
        margin: 1rem 0;
    }
    
    .education-title {
        color: #1e3c72;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .education-institution {
        color: #6c757d;
        font-weight: 500;
        margin-bottom: 0.8rem;
    }
    
    .language-bar {
        background: #e9ecef;
        height: 8px;
        border-radius: 4px;
        margin: 0.5rem 0;
    }
    
    .language-fill {
        background: linear-gradient(90deg, #2a5298, #1e3c72);
        height: 100%;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("### :material/menu: Navigation")
    sections = [
        ("Overview", ":material/dashboard:"),
        ("About", ":material/person:"),
        ("Skills", ":material/code:"),
        ("Experience", ":material/work:"),
        ("Projects", ":material/rocket_launch:"),
        ("Education", ":material/school:"),
        ("Achievements", ":material/emoji_events:"),
        ("Contact", ":material/contact_mail:")
    ]
    
    selected_section = st.selectbox(
        "Select Section:",
        [section[0] for section in sections],
        format_func=lambda x: f"{next(icon for name, icon in sections if name == x)} {x}"
    )

# Professional Header
st.markdown("""
<div class="professional-header">
    <h1>Alireza Babazadeh Zarei</h1>
    <h3>AI/ML Engineer & Research Scientist</h3>
    <p>Specializing in Deep Learning, Neural Networks, and Artificial Intelligence Innovation</p>
</div>
""", unsafe_allow_html=True)

if selected_section == "Overview":
    # Key Statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stats-card">
            <span class="stats-number">3+</span>
            <div class="stats-label">Competition Medals</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stats-card">
            <span class="stats-number">15+</span>
            <div class="stats-label">AI Models</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stats-card">
            <span class="stats-number">5+</span>
            <div class="stats-label">Major Projects</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stats-card">
            <span class="stats-number">3</span>
            <div class="stats-label">Programming Languages</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Professional Summary
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/analytics: Professional Summary</h2>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #495057;">
        Accomplished AI/ML Engineer with extensive experience in developing cutting-edge artificial intelligence solutions. 
        Proven track record of success in international competitions with multiple medal achievements. Expertise spans across 
        deep learning architectures, natural language processing, computer vision, and innovative AI applications in healthcare 
        and business domains.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Core Competencies
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/star: Core Competencies</h2>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        competencies_1 = [
            "Deep Learning & Neural Networks",
            "Machine Learning Model Development",
            "Natural Language Processing",
            "Computer Vision Applications",
            "RAG & Chatbot Development"
        ]
        for comp in competencies_1:
            st.markdown(f"• **{comp}**")
    
    with col2:
        competencies_2 = [
            "AI Research & Innovation",
            "Competition Strategy & Execution",
            "Healthcare AI Solutions",
            "Advanced Analytics",
            "Technical Leadership"
        ]
        for comp in competencies_2:
            st.markdown(f"• **{comp}**")
    
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_section == "About":
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/person: Professional Profile</h2>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #495057; margin-bottom: 2rem;">
        I am a dedicated AI/ML Engineer with a passion for pushing the boundaries of artificial intelligence. 
        My career is defined by continuous learning, innovative problem-solving, and a commitment to developing 
        AI solutions that make a meaningful impact. With a strong foundation in computer engineering and 
        extensive hands-on experience, I specialize in creating sophisticated machine learning models and 
        AI systems that address real-world challenges.
        </p>
        
        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 6px; margin: 1.5rem 0;">
            <h4 style="color: #1e3c72; margin-bottom: 1rem;">:material/psychology: Research Philosophy</h4>
            <p style="color: #495057; line-height: 1.6;">
            "Innovation in AI comes from understanding both the theoretical foundations and practical applications. 
            My approach combines rigorous research methodologies with creative problem-solving to develop AI solutions 
            that are not just technically sound, but also ethically responsible and practically valuable."
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional Interests
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section-container">
            <h3>:material/interests: Research Interests</h3>
            <ul style="line-height: 2;">
                <li><strong>Generative AI:</strong> GANs, Transformers, and Novel Architectures</li>
                <li><strong>Healthcare AI:</strong> Medical Diagnostics and Treatment Optimization</li>
                <li><strong>Conversational AI:</strong> Advanced Chatbots and RAG Systems</li>
                <li><strong>Computer Vision:</strong> Medical Imaging and Pattern Recognition</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section-container">
            <h3>:material/language: Languages</h3>
        """, unsafe_allow_html=True)
        
        languages = [("English", 85), ("Persian (Native)", 100)]
        
        for lang, proficiency in languages:
            st.markdown(f"""
            <div style="margin: 1rem 0;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                    <span style="font-weight: 500;">{lang}</span>
                    <span style="color: #6c757d;">{proficiency}%</span>
                </div>
                <div class="language-bar">
                    <div class="language-fill" style="width: {proficiency}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

elif selected_section == "Skills":
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/code: Technical Expertise</h2>
    """, unsafe_allow_html=True)
    
    # Programming Languages
    st.markdown("""
    <div class="skill-category">
        <h4>:material/terminal: Programming Languages</h4>
    """, unsafe_allow_html=True)
    
    prog_skills = ["Python", "C++", "Java"]
    for skill in prog_skills:
        st.markdown(f'<span class="skill-item">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Machine Learning
    st.markdown("""
    <div class="skill-category">
        <h4>:material/psychology: Machine Learning Models</h4>
    """, unsafe_allow_html=True)
    
    ml_skills = [
        "Linear Regression", "Random Forest", "Classification Trees", "Regression Trees",
        "Support Vector Machine", "K-Nearest Neighbors", "Supervised Learning",
        "Unsupervised Learning", "Reinforcement Learning"
    ]
    
    for skill in ml_skills:
        st.markdown(f'<span class="skill-item">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Deep Learning
    st.markdown("""
    <div class="skill-category">
        <h4>:material/neurology: Deep Learning Architectures</h4>
    """, unsafe_allow_html=True)
    
    dl_skills = [
        "Convolutional Neural Networks", "Long Short Term Memory Networks",
        "Recurrent Neural Networks", "Generative Adversarial Networks",
        "Multilayer Perceptrons", "Transformer Models", "Vision Transformers"
    ]
    
    for skill in dl_skills:
        st.markdown(f'<span class="skill-item">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Professional Skills
    st.markdown("""
    <div class="skill-category">
        <h4>:material/group: Professional Skills</h4>
    """, unsafe_allow_html=True)
    
    soft_skills = ["Problem Solving", "Creativity", "Negotiation", "Critical Thinking", "Management Skills"]
    
    for skill in soft_skills:
        st.markdown(f'<span class="skill-item">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Skills Visualization
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/analytics: Skills Assessment</h2>
    """, unsafe_allow_html=True)
    
    # Create professional skills radar chart
    skills_data = {
        'Skill': ['Machine Learning', 'Deep Learning', 'Programming', 'Problem Solving', 'Research', 'Innovation'],
        'Proficiency': [95, 90, 85, 95, 88, 92]
    }
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=skills_data['Proficiency'],
        theta=skills_data['Skill'],
        fill='toself',
        name='Proficiency Level',
        line_color='#2a5298',
        fillcolor='rgba(42, 82, 152, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10)
            )
        ),
        showlegend=False,
        title={
            'text': "Technical Proficiency Assessment",
            'x': 0.5,
            'font': {'size': 16, 'color': '#1e3c72'}
        },
        height=500,
        font=dict(size=12)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_section == "Experience":
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/work: Professional Experience</h2>
        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 6px; margin-bottom: 2rem;">
            <h4 style="color: #1e3c72;">:material/chat: RAG & Chatbot Specialist</h4>
            <p style="color: #495057; line-height: 1.6; margin-bottom: 1rem;">
            Extensive experience in developing sophisticated Retrieval-Augmented Generation systems and 
            conversational AI solutions. Specialized in creating intelligent chatbots that combine natural 
            language understanding with domain-specific knowledge retrieval.
            </p>
            <div style="margin-top: 1rem;">
                <strong style="color: #2a5298;">Key Technologies:</strong>
                <span style="color: #6c757d;"> Large Language Models, Vector Databases, NLP Pipelines, Conversational AI Frameworks</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected_section == "Projects":
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/rocket_launch: Featured Projects</h2>
    """, unsafe_allow_html=True)
    
    projects = [
        {
            "title": "Ravansha Application Platform",
            "competition": "GenX Competitions 2023",
            "description": "Developed an innovative AI-powered application platform leveraging advanced machine learning algorithms for intelligent user interaction and automated decision-making processes.",
            "technologies": ["Deep Learning", "Neural Networks", "Python", "AI Algorithms"],
            "icon": ":material/psychology:"
        },
        {
            "title": "Catalyst Careers Intelligence System",
            "competition": "Seeds4Future Competitions",
            "description": "Engineered a sophisticated career guidance chatbot utilizing RAG technology to provide personalized career recommendations and professional development insights.",
            "technologies": ["RAG", "NLP", "Chatbot Framework", "Machine Learning"],
            "icon": ":material/work:"
        },
        {
            "title": "ECG Analysis & AI Diagnostics",
            "competition": "GenX Competitions 2024",
            "description": "Created an advanced AI system for electrocardiogram analysis, implementing deep learning models for automated cardiac abnormality detection and medical diagnostics.",
            "technologies": ["Computer Vision", "Medical AI", "CNN", "Signal Processing"],
            "icon": ":material/monitor_heart:"
        },
        {
            "title": "Cervical Cancer Advisory System",
            "competition": "KeyvanLabs",
            "description": "Developed a comprehensive AI-powered advisory system for cervical cancer screening, utilizing machine learning for risk assessment and treatment recommendations.",
            "technologies": ["Healthcare AI", "Classification Models", "Medical Imaging", "Risk Assessment"],
            "icon": ":material/health_and_safety:"
        },
        {
            "title": "Advanced Character AI Development",
            "competition": "Character.ai Platform",
            "description": "Created multiple sophisticated AI characters including Chandler Bing-SagGpt and AliZare AI, demonstrating expertise in personality modeling and conversational AI development.",
            "technologies": ["Conversational AI", "Personality Modeling", "NLP", "Character Development"],
            "icon": ":material/smart_toy:"
        }
    ]
    
    for project in projects:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{project['icon']} {project['title']}</div>
            <div class="project-meta"><strong>Platform:</strong> {project['competition']}</div>
            <div class="project-description">{project['description']}</div>
            <div style="margin-top: 1rem;">
                <strong style="color: #2a5298;">Technologies:</strong>
                <span style="color: #6c757d;">{' • '.join(project['technologies'])}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_section == "Education":
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/school: Education & Certifications</h2>
    """, unsafe_allow_html=True)
    
    # Formal Education
    st.markdown("""
    <div class="education-item">
        <div class="education-title">:material/computer: Bachelor of Computer Engineering - Software</div>
        <div class="education-institution">Azad University - Rasht</div>
        <p style="color: #495057; line-height: 1.6;">
        Comprehensive education in software engineering principles, computer science fundamentals, 
        and advanced programming methodologies. Specialized coursework in algorithms, data structures, 
        and software architecture design.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### :material/card_membership: Professional Certifications")
    
    certifications = [
        {
            "title": "Machine Learning Expertise",
            "provider": "Coursera",
            "description": "Advanced certification covering comprehensive machine learning methodologies, algorithms, and practical implementation strategies.",
            "icon": ":material/psychology:"
        },
        {
            "title": "AI from the Neurosurgeon's Perspective",
            "provider": "Shahid Beheshti University",
            "description": "Specialized program exploring artificial intelligence applications in medical neuroscience and surgical procedures.",
            "icon": ":material/medical_services:"
        },
        {
            "title": "Artificial Intelligence Hackathon",
            "provider": "Irancell Labs",
            "description": "Intensive hands-on program focused on rapid AI solution development and innovative problem-solving methodologies.",
            "icon": ":material/code:"
        }
    ]
    
    for cert in certifications:
        st.markdown(f"""
        <div class="education-item">
            <div class="education-title">{cert['icon']} {cert['title']}</div>
            <div class="education-institution">Certified by: {cert['provider']}</div>
            <p style="color: #495057; line-height: 1.6;">{cert['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_section == "Achievements":
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/emoji_events: Awards & Recognition</h2>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="achievement-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">:material/workspace_premium:</div>
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">Gold Medal Winner</div>
            <div>International Inventions Competition</div>
        </div>
        
        <div class="achievement-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">:material/military_tech:</div>
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">2× Silver Medal Winner</div>
            <div>International Inventions Competition</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Medal distribution chart
        medals_data = pd.DataFrame({
            'Medal': ['Gold', 'Silver'],
            'Count': [1, 2],
            'Color': ['#FFD700', '#C0C0C0']
        })
        
        fig = px.pie(medals_data, values='Count', names='Medal', 
                     title="Competition Medal Distribution",
                     color_discrete_map={'Gold': '#FFD700', 'Silver': '#C0C0C0'})
        
        fig.update_layout(
            title={'font': {'size': 16, 'color': '#1e3c72'}},
            height=300,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### :material/trending_up: Professional Recognition")
    
    recognition_items = [
        "International competition medalist with proven excellence in AI innovation",
        "Recognition for outstanding contributions to artificial intelligence research",
        "Leadership in developing cutting-edge machine learning solutions",
        "Demonstrated expertise in healthcare AI and medical diagnostics",
        "Innovation in conversational AI and chatbot development"
    ]
    
    for item in recognition_items:
        st.markdown(f"• **{item}**")
    
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_section == "Contact":
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/contact_mail: Professional Contact</h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="contact-card">
            <h4>:material/email: Email</h4>
            <p>inv.alirezababazadehzarei@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-card">
            <h4>:material/phone: Phone</h4>
            <p>+98 903-410-1611</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="contact-card">
            <h4>:material/link: Professional Network</h4>
            <p>LinkedIn: /inv-alizare</p>
            <p>Kaggle: /inv-alizare</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Professional Inquiry Form
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">:material/contact_support: Professional Inquiry</h2>
    """, unsafe_allow_html=True)
    
    with st.form("professional_contact"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name", placeholder="Enter your full name")
            email = st.text_input("Professional Email", placeholder="your.email@company.com")
        
        with col2:
            company = st.text_input("Organization", placeholder="Company/Institution")
            inquiry_type = st.selectbox(
                "Inquiry Type",
                ["Research Collaboration", "Consulting Services", "Project Partnership", "Speaking Engagement", "Employment Opportunity"]
            )
        
        message = st.text_area("Message", placeholder="Please describe your inquiry in detail...", height=120)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.form_submit_button("Send Professional Inquiry", use_container_width=True):
                if name and email and message:
                    st.success("Thank you for your professional inquiry. I will respond within 24-48 hours.")
                    st.balloons()
                else:
                    st.error("Please fill in all required fields.")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Collaboration Interests
    st.markdown("""
    <div class="section-container">
        <h3>:material/handshake: Collaboration Interests</h3>
        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 6px; margin: 1rem 0;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                <div>
                    <h4 style="color: #1e3c72; margin-bottom: 1rem;">:material/science: Research Areas</h4>
                    <ul style="line-height: 1.8; color: #495057;">
                        <li>Advanced Neural Network Architectures</li>
                        <li>Medical AI and Healthcare Solutions</li>
                        <li>Conversational AI and NLP Systems</li>
                        <li>Computer Vision Applications</li>
                        <li>Generative AI and Creative Applications</li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: #1e3c72; margin-bottom: 1rem;">:material/business: Professional Services</h4>
                    <ul style="line-height: 1.8; color: #495057;">
                        <li>AI/ML Consulting and Strategy</li>
                        <li>Custom Model Development</li>
                        <li>Technical Leadership and Mentoring</li>
                        <li>Research Paper Collaboration</li>
                        <li>Conference Speaking Engagements</li>
                    </ul>
                </div>
            </div>
        </div>
        <div style="text-align: center; margin-top: 2rem; padding: 1.5rem; background: linear-gradient(135deg, #1e3c72, #2a5298); color: white; border-radius: 6px;">
            <h4 style="margin-bottom: 1rem;">Ready to Innovate Together?</h4>
            <p style="margin-bottom: 0; opacity: 0.9;">
            I'm passionate about collaborative projects that push the boundaries of AI technology 
            and create meaningful impact in healthcare, business, and society.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Professional Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 6px;">
    <div style="color: #1e3c72; font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;">
        Alireza Babazadeh Zarei
    </div>
    <div style="color: #6c757d; margin-bottom: 1rem;">
        AI/ML Engineer | Research Scientist | Innovation Leader
    </div>
    <div style="color: #adb5bd; font-size: 0.9rem;">
        Built with Streamlit | Professional Portfolio © 2024
    </div>
</div>
""", unsafe_allow_html=True)