# 🎬 AI Movie Recommendation System

## 📌 Project Overview

The AI Movie Recommendation System is a simple recommendation application that provides movie suggestions based on user preferences.

The system takes user preferences such as genre, language, and movie type and matches them with available movie attributes using a similarity-based scoring logic.

## 🎯 Project Objective

The objective of this project is to demonstrate basic recommendation logic, preference matching, and similarity-based item recommendation.

## ⚙️ How It Works

1. The user selects a preferred genre.
2. The user selects a preferred language.
3. The user selects a preferred movie type.
4. The system compares the selected preferences with movie attributes.
5. A similarity score is calculated for each movie.
6. Movies are sorted based on similarity score and rating.
7. The top matching movies are displayed as recommendations.

## 🧠 Recommendation Logic

The system uses a simple rule-based similarity scoring approach.

- Genre match = +2 points
- Language match = +1 point
- Movie type match = +1 point

A movie can receive a maximum similarity score of 4 when all three preferences match.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- CSV Dataset

## 📂 Project Structure

```text
AI-Recommendation-System/
│
├── app.py
├── movies.csv
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    ├── home.png
    └── recommendation.png
