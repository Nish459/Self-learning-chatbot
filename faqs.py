class FAQData:
    def __init__(self):
        self.faqs = [
            {
                "question": "How do I import API keys in bulk?",
                "answer": "You can bulk import keys from the portal's import section."
            },
            {
                "question": "What happens if I enter a wrong key?",
                "answer": "You will see an error. Please verify the key format."
            },
            {
                "question": "How to reset my password?",
                "answer": "Click on 'Forgot password' on the login page."
            },
            {
                "question": "How to reset my profile?",
                "answer": "Click on 'Edit profile' on the login page."
            },
            {
                "question": "How to reslove proxy error?",
                "answer": "Select correct IP's from proxy section."
            }
        ]
    
    def get_questions(self):
        return [faq["question"] for faq in self.faqs]
