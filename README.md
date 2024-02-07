# Emotion_detection/face_recognition

# Problem Statement:
To mark attendance of employees of an organisation using face recognition technology and detect their emotion/expression and make efforts accordingly to keep them in the best of their mood

# Project Description:
This project focuses on identifying/recognising and then capturing the emotion of employees of an organisation on a daily basis when they log into their systems.
Various quotes based on their emotions are displayed in their screens the moment they login to better their mood along with a picture containing something personal to them. 
The UI has been made using python's streamlit and backend has been created in phpmyadmin using sql commands.

# Project Features:
Face Recognition- The attendance of employees is automatically updated in the database along with the time and date of login which will help in keeping a check on how regular an employee is.
Emotion Recognition- The emotion of an employee at the time of login is also recorded along with attendance on the basis of which an approprite quote is displayed on the employee's screen to motivate him/her and a personalized picture is displayed which has a positive visual impact on their mood and hence work performace.

# How to run
Install the streamlit,deepface,face_recognition,numpy,open-cv,datetime,mysql-connector-python and pillow libraries using the pip install commmand.
Start apache and mysql in Xampp control panel and import the database in the desired format into phpmyadmin. 
Run home.py by giving the command - streamlit run followed by location of the file in your device and you are good to go!!

# Project Application:
Using this data collected over a reasonable period of a month or so, any company/organisation can easily keep a check on the mental health of their employees which directly affects their productivity and performance at work and the benefit to the company.
A happy, Motivated and healthy work environment can help technology reach great heights and help you and me, or rather humanity as a whole to a great extent

# Few screenshots of the project-

![image (2)](https://github.com/kkumarsupraja/Emotion_detection/assets/77972491/02a32773-2157-4466-87aa-2583501720cf)
Screenshot where Person has been identified as Supraja correctly, Expression has been detected (happy) and a quote has been displayed according to emotion detected.

![image](https://github.com/kkumarsupraja/Emotion_detection/assets/77972491/17062a8b-7758-4938-ab84-ef71e1d51e24)
An image of the attendance database where attendance of employees has been marked along with date, time and emotion

![image (1)](https://github.com/kkumarsupraja/Emotion_detection/assets/77972491/c9a7a63b-0060-42c5-a3a2-cc070ada995f)
Database containing quotes that are to be displayed according to emotion of employee

Good Day!!


