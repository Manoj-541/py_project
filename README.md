# 🩺 HealthSense – Symptom-Based Disease Prediction System(Python)

## 📌 Overview

HealthSense is a full-stack web application that predicts potential diseases based on user-selected symptoms. The system dynamically extracts symptoms from a structured dataset and applies a similarity-based classification algorithm to determine the most likely disease.

The project demonstrates backend architecture, secure authentication, dynamic UI rendering, and scalable dataset-driven design using Flask.

---

## 🚀 Features

- 🔐 Secure User Authentication (Password Hashing + Sessions)
- 📊 Dynamic Symptom Extraction from Dataset (No Hardcoding)
- 🧠 Similarity-Based Disease Prediction Algorithm
- 🎨 Responsive Card-Based UI Design
- 🏗 Modular Architecture with Separation of Concerns
- 📁 Scalable Support for 100+ Diseases

---

## 🏗 System Architecture

HealthSense follows a layered architecture:

- **Presentation Layer** → HTML Templates (Jinja2)  
- **Application Layer** → Flask Routes  
- **Business Logic Layer** → Prediction Engine (`ml.py`)  
- **Data Layer** → SQLite Database + CSV Dataset  

This structure ensures maintainability, scalability, and clean code organization.

---

## 🧠 Prediction Algorithm

The disease prediction logic uses a set-intersection similarity approach:

1. Extract all unique symptoms from dataset
2. Compare selected symptoms with each disease’s symptom list
3. Count the number of matches
4. Return the disease with the highest similarity score

---

## ⏱ Time Complexity

**O(N × S)**

Where:

- **N** = Number of diseases  
- **S** = Number of symptoms per disease  

This lightweight approach allows efficient classification without requiring heavy ML models.

---

## 🛠 Tech Stack

- Python
- Flask
- SQLAlchemy
- Pandas
- SQLite
- HTML5 & CSS3
