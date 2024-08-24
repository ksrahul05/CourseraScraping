# Coursera Dataset Scraper and AI Predictor

## Project Overview
This project focuses on scraping course data from Coursera and building an AI model to predict course-related outcomes based on the extracted features. The goal is to automate the extraction of course information and utilize machine learning to derive insights that could guide users in selecting courses that meet their specific needs.

### Dataset Attributes
The following attributes are scraped from Coursera for each course:
- **Course Name**: The title of the course.
- **Link**: The URL to the course page on Coursera.
- **Rating**: The average user rating of the course.
- **Duration**: The estimated time to complete the course.
- **Course Level**: The difficulty level of the course (e.g., Beginner, Intermediate, Advanced).
- **Course Type**: The type of course (e.g., Specialization, Professional Certificate).
- **Number of Reviews**: The total number of reviews submitted by learners.
- **Skills Gained**: The key skills that the course aims to impart.

## Objective
The primary objective of this project is to use machine learning to predict the potential success of a course based on its attributes. This could include predicting user ratings, determining the likelihood of a course being highly reviewed, or identifying courses that provide valuable skills for career advancement.

### AI Concept Used
To achieve this objective, we employ supervised learning algorithms, such as regression models or classification models, depending on the specific prediction task. The AI model will be trained on the dataset to learn the relationships between the course attributes and the outcomes we aim to predict.

### Dependent and Independent Variables
- **Independent Variables (Features)**:
  - Course Name
  - Rating
  - Duration
  - Course Level
  - Course Type
  - Number of Reviews
  - Skills Gained

- **Dependent Variable (Target)**:
  - This could vary depending on the specific prediction task. Examples include:
    - **Predicting Course Rating**: The rating could be the dependent variable, with the other attributes serving as independent variables.
    - **Predicting Number of Reviews**: The number of reviews could be the dependent variable.

## How to Use
1. **Setup Environment**: Ensure you have Python and necessary libraries installed (`selenium`, `beautifulsoup4`, `pandas`, etc.).
2. **Scrape Data**: Run the provided scraper script to collect course data from Coursera.
3. **Data Preprocessing**: Clean and prepare the data for machine learning.
4. **Train Model**: Use the prepared dataset to train a machine learning model.
5. **Predict Outcomes**: Use the trained model to make predictions on new course data.

## Requirements
- Python 3.x
- Selenium
- BeautifulSoup4
- Pandas
- Scikit-learn
- Flask (if deploying the model as a web application)

## Future Enhancements
- Expanding the dataset to include more courses.
- Implementing additional AI models to improve prediction accuracy.
- Integrating the model into a web-based platform for real-time predictions.

## Contribution
Contributions are welcome. Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
