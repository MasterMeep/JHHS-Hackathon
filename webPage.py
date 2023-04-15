import streamlit as st 
import datetime
from streamlit_option_menu import option_menu
st.title("Mental Health")
import json 
import openai
from nlp import generate_matplotlib_graph
selected = option_menu(
    menu_title = None,
    options = ["Journaling", "Improvement", "Donate"], 
    icons = ["calender", "book", "envelope"],
    menu_icon="cast",
    default_index = 0, 
    orientation="horizontal"
)

if 'savedResponses' not in st.session_state:
    st.session_state.savedResponses = {
        
    }
if 'dates' not in st.session_state:
    st.session_state.dates = set()
if 'answers' not in st.session_state:
    st.session_state.answers = []

question = ["How are you feeling: ", "Have you had negative thoughts recently: ", "Do you think you are feeling better than yesterday: "]
def save_data():
    st.session_state.savedResponses[st.session_state.date] = {"feeling": st.session_state.feeling, "thoughts": st.session_state.thoughts, "yesterday": st.session_state.yesterday} 

def load_data():
    if not st.session_state.date in st.session_state.savedResponses.keys():
        data = {"feeling": "None", "thoughts": "None", "yesterday": "None"}
    else:
        print("aaaa")
        data = st.session_state.savedResponses[st.session_state.date]
    st.session_state.feeling = data['feeling']
    st.session_state.thoughts = data['thoughts']
    st.session_state.yesterday = data['yesterday']

if selected == "Journaling":
    d =  st.date_input("Select a date", datetime.date(2023, 7, 6), key='date', on_change=load_data)
    st.session_state.dates.add(d)
    with st.form("my_form", clear_on_submit=False):
        feeling = st.text_area("How are you feeling: ", key='feeling')
        thoughts = st.text_area("Have you had negative thoughts recently: ", key='thoughts')
        yesterday = st.text_area("Do you think you are feeling better than yesterday: ", key='yesterday')
        checkBox = st.checkbox("Enable Therapist AI")
        submitted = st.form_submit_button("Submit")
    if submitted:
        st.session_state.answers.append(feeling+" " + thoughts + " " + yesterday)

        save_data()
        if checkBox:
            openai.api_key = "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"
            question1 = question[0]
            response1 = st.session_state.savedResponses[d]["feeling"]
            question2 = question[1]
            response2 = st.session_state.savedResponses[d]["thoughts"]
            question3 = question[2]
            response3 = st.session_state.savedResponses[d]["yesterday"]
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"You are an expert AI therapist, your patient is a veteran who is suffering with mental health issues, possibly depression, anxiety, or PTSD, they have answered some short answer questions and based on their responses give them some advice. Question #1: {question1}, Response #1: {response1}, Question #2: {question2}, Response #2: {response2}, Question#3: {question3}, Response #3: {response3}"}])
            st.divider()
            st.subheader("Advice from an AI therapist")
            st.write(completion.choices[0].message.content)



if selected == "Improvement":
    st.plotly_chart(generate_matplotlib_graph(st.session_state.answers,list(st.session_state.dates)))


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
def send_email(sender, password, receiver, smtp_server, 
smtp_port, email_message, subject, attachment=None):
  message = MIMEMultipart()
  message['To'] = Header(receiver)
  message['From']  = Header(sender)
  message['Subject'] = Header(subject)
  message.attach(MIMEText(email_message,'plain', 'utf-8'))
  if attachment:
    att = MIMEApplication(attachment.read(), _subtype="txt")
    att.add_header('Content-Disposition', 'attachment', filename=attachment.name)
    message.attach(att)
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    text = message.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()



from venmo import email

if selected == "Donate":
    with st.form("form"):
        name = st.text_input("What is your full name: ")
        emailAdress = st.text_input("What is your email adress")
        submitted =  st.form_submit_button("send email")
        if submitted:
            st.write(email(name, emailAdress))
