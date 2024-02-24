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
        helper.save_data(formatted_data, 'data/interview_data_test.csv')
