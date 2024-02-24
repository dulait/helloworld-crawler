import os.path

import pandas as pd


class Helper:

    @staticmethod
    def format_data(interview_data):
        formatted_data = []

        for interview in interview_data:
            company = interview['company']
            position = interview['position']
            questions = interview['questions']

            cleaned_questions = [question.replace('\n', ' ') for question in questions]

            formatted_data.append({
                'company': company,
                'position': position,
                'questions': ', '.join(cleaned_questions)
            })
        return formatted_data

    @staticmethod
    def save_data(data, file_path):
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False, encoding='utf-8')

    @staticmethod
    def format_and_save(data):
        helper = Helper()

        formatted_data = helper.format_data(data)

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        file_path = os.path.join(desktop_path, 'interview_data.csv')
        helper.save_data(formatted_data, file_path)

        print(f"\n✅Data successfully saved to {file_path}.\n🍀Good luck!")
