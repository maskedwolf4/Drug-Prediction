# Drug-Prediction

**# Drug Prediction App**

**## Overview**

This application leverages a machine learning model to predict the most suitable drug for a patient based on their clinical characteristics. It's built with Python and Streamlit, offering a user-friendly interface for seamless interaction.

**## Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/maskedwolf4/Drug-Prediction.git
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # (Linux/macOS)
   venv\Scripts\activate.bat  # (Windows)
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

**## Usage**

1. **Run the app:**

   ```bash
   streamlit run dpapp.py
   ```

2. **Enter patient information:**
   - Age
   - Na_to_K ratio
   - Sex (M or F)
   - Blood pressure (LOW, NORMAL, or HIGH)
   - Cholesterol status (Yes or No)

3. **Click "Predict Drug" to view the recommended drug.**

**## Model Details**

- **Model type:** Random Forest Classifier
- **Features:**
   - Age
   - Na_to_K ratio
   - Sex (M or F)
   - Blood pressure (LOW, NORMAL, or HIGH)
   - Cholesterol status (Yes or No)
- **Performance metrics:** Accuracy = 1

**## Disclaimer**

- This app is intended for educational and demonstration purposes only.
- It should not be used for actual medical decision-making.
- Always consult with a qualified healthcare professional for medical advice.

**## Contribute**

- Feel free to contribute to this project by submitting issues or pull requests.

**## License**

- This project is licensed under (Specify the license type, e.g., MIT License).
