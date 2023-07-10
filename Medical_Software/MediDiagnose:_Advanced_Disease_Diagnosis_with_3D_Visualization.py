# Please make sure to have the medical_data.db SQLite database file present in the same directory as the Python script.
# Additionally, update the code as per your specific data schema and requirements.

import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QComboBox, QPushButton

# Step 1: Data Collection and Management
def connect_to_database():
    conn = sqlite3.connect("medical_data.db")
    return conn

def create_medical_records_table():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS medical_records (
            record_id INTEGER PRIMARY KEY,
            feature1 FLOAT,
            feature2 FLOAT,
            feature3 FLOAT,
            disease TEXT,
            disease_code INTEGER
        )
    """)
    conn.commit()
    conn.close()

def fetch_medical_data():
    conn = connect_to_database()
    query = "SELECT * FROM medical_records"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

# Step 2: Disease Classification and Prediction
def train_classification_model():
    data = fetch_medical_data()
    features = data.drop(['disease'], axis=1)
    target = data['disease']
    model = RandomForestClassifier()
    model.fit(features, target)
    return model

# Step 3: 3D Visualization
def visualize_data(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data['feature1'], data['feature2'], data['feature3'], c=data['disease_code'], cmap='viridis')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Feature 3')
    plt.show()

# Step 4: User Interface Development
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Disease Diagnosis")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.label = QLabel("Select a medical record to diagnose:")
        self.combo_box = QComboBox()
        self.load_button = QPushButton("Load", self)
        self.load_button.clicked.connect(self.load_data_and_diagnose)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.label)
        layout.addWidget(self.combo_box)
        layout.addWidget(self.load_button)

    def load_data_and_diagnose(self):
        selected_record = self.combo_box.currentText()
        data = fetch_medical_data()
        record_data = data.loc[data['record_id'] == selected_record]
        diagnose_result = model.predict(record_data.drop(['disease'], axis=1))
        # Display diagnose_result or perform further actions

# Step 5: Integration and Deployment
if __name__ == '__main__':
    conn = connect_to_database()
    create_medical_records_table()
    model = train_classification_model()
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    conn.close()
