import os
import shutil
import re
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

class FileSorter:
    def __init__(self, file_names, categories):
        # Verify that the number of file names matches the number of categories
        if len(file_names) != len(categories):
            raise ValueError(f"Number of filenames ({len(file_names)}) does not match number of categories ({len(categories)})")

        self.file_names = file_names
        self.categories = categories

        # Initialize CountVectorizer to convert filenames to feature vectors
        self.vectorizer = CountVectorizer(tokenizer=lambda x: re.split(r'[_\-.]', x ),token_pattern=None)  # Split by underscores, hyphens, or periods
        self.X = self.vectorizer.fit_transform(file_names)

        # Convert categories to numerical labels
        self.category_to_index = {cat: idx for idx, cat in enumerate(set(categories))}
        self.y = np.array([self.category_to_index[cat] for cat in categories])

        # Train a Decision Tree Classifier
        self.clf = DecisionTreeClassifier(random_state=42)
        self.clf.fit(self.X, self.y)

    def predict_category(self, file_name):
        """Predict category for a single file name."""
        features = self.vectorizer.transform([file_name])
        predicted_label = self.clf.predict(features)
        return list(self.category_to_index.keys())[predicted_label[0]]

    def sort_files_by_category(self, file_dir, output_dir='./sorted_files'):
        """Sort files from the input directory into subdirectories by predicted categories."""
        os.makedirs(output_dir, exist_ok=True)
        file_names = [f for f in os.listdir(file_dir) if os.path.isfile(os.path.join(file_dir, f))]

        predictions = {}

        # Predict the categories for each file
        for file_name in file_names:
            category = self.predict_category(file_name)
            predictions[file_name] = category
            print(f"Predicted category for '{file_name}': {category}")

        # Ask once if the user wants to move all files
        while True:
            move_all = input("Do you want to move all files to their predicted categories? (yes/no): ").strip().lower()
            if move_all in ['yes', 'no']:
                break
            print("Please answer with 'yes' or 'no'.")

        if move_all == 'yes':
            # Move all files at once if the user confirms
            for file_name, category in predictions.items():
                category_path = os.path.join(output_dir, category)
                os.makedirs(category_path, exist_ok=True)
                source = os.path.join(file_dir, file_name)
                destination = os.path.join(category_path, file_name)
                shutil.move(source, destination)
                print(f"Moved '{file_name}' to '{category_path}'")
        else:
            print("No files were moved.")

def ai_based_sort(root_directory):
    # Example file names and categories
    file_names = [
        "personal_finance.xlsx", "finance_report_2023.xlsx", "data_analysis_script.py",
        "presentation_archive_2023.zip", "html_basics_tutorial.txt", "python_basics_course.txt",
        "project_image.jpg", "meeting_notes.docx", "SIH2024-Disaster-Management.pdf",
        "SIH2024_IDEA_Presentation_Format.pptx", "monthly_budget.xlsx", "project_proposal.docx",
        "marketing_strategy_2024.pptx", "sales_report_Q1.pdf", "meeting_minutes.txt",
        "financial_analysis_report.pdf", "presentation_overview_final.pptx", "web_dev_basics_notes.txt",
        "business_plan_2024.docx", "data_visualization_tool.py", "2024_event_schedule.pdf",
        "user_guide_v2.pdf", "contract_template.docx", "research_notes.txt",
        "annual_report_2023.pdf", "quarterly_review.pptx", "budget_summary.xlsx",
        "image_processing_script.py", "inventory_list.xlsx", "api_documentation.docx",
        "press_release_template.docx", "team_meeting_schedule.txt", "financial_statement_2024.pdf",
        "sales_forecast.xlsx", "data_cleaning_script.py", "event_planning_template.pptx",
        "project_timeline.xlsx", "case_study_analysis.pdf", "marketing_materials.pptx",
        "presentation_template.pptx", "web_dev_overview.txt", "Screenshot 2024.png",
    ]

    categories = [
        'Spreadsheet', 'Spreadsheet', 'Python Script', 'Archive', 'Text', 'Text',
        'Image', 'Document', 'PDF', 'Presentation', 'Spreadsheet', 'Document',
        'Presentation', 'PDF', 'Text', 'PDF', 'Presentation', 'Text', 'Document',
        'Python Script', 'PDF', 'PDF', 'Document', 'Text', 'PDF', 'Presentation',
        'Spreadsheet', 'Python Script', 'Spreadsheet', 'Document', 'Document',
        'Text', 'PDF', 'Spreadsheet', 'Python Script', 'Presentation', 'Spreadsheet',
        'Presentation', 'Presentation', 'Text', 'Text', 'Image',
    ]
    # Create an instance of FileSorter
    file_sorter = FileSorter(file_names, categories)

    # Call the sorting function
    sorted_output_directory = r"C:\Users\reals\Desktop\test2"
    file_sorter.sort_files_by_category(root_directory, sorted_output_directory)