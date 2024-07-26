import os
from openai import OpenAI
import fitz  # PyMuPDF
import requests
from transformers import pipeline
from dotenv import load_dotenv
from bs4 import BeautifulSoup

#load_dotenv()

#client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def generate_questions(text):
    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": "You are a tutor."},
    #         {"role": "user", "content": f"Generate four questions about the following text: {text}."
    #                                     f" The questions should assess if the student understands the material, "
    #                                     f"understands their own thought process, and if they implement self-regulated learning when studying the material. "
    #                                     f"Provide one question for each of these areas:" 
    #                                     f" 1. Understanding the Material"
    #                                     f" 2. Understanding Their Own Thought Process"
    #                                     f" 3. Self-Regulated Learning - Comprehension Monitoring"
    #                                     f" 4. Self-Regulated Learning - Goal Setting"},
    #     ],
    #     max_tokens=300
    # )
    # question = [message['content'].strip() for message in response.choices[0]['message']['content']]
    question = """Alright, here are some questions to assess your understanding 
    of the material, your thought process, and your self-regulated 
    learning strategies:

    Understanding the Material:

    What is the significance of the war between Britain and Zanzibar 
    mentioned in the text?

    Understanding Your Own Thought Process:

    How do you personally make sense of the fact that Cleopatra 
    lived closer in time to the moon landing than to the construction of 
    the Great Pyramid of Giza?
    Self-Regulated Learning - Comprehension Monitoring:

    While reading about the various intriguing facts, 
    what strategies did you use to ensure you remembered 
    details like the longevity of honey or the number of hearts an octopus has?

    Self-Regulated Learning - Goal Setting:

    What specific goals did you set for yourself when studying the facts in this text, 
    and how did you plan to achieve them to ensure a thorough understanding?"""
    return question

def compare_question_and_answer(question, answer):
    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": "You are a tutor evaluating responses."},
    #         {"role": "user", "content": f"Start by saying kay then, here's my evaluation. Compare the following question and answer based on the way the user responded. Evaluate if the answer demonstrates an understanding of the material, the student's thought process, and the use of self-regulated learning strategies. Provide feedback on each aspect. Here is the question and answer:"
    #                                     f"\n\nQuestion: {question}"
    #                                     f"\n\nAnswer: {answer}"
    #                                     f"\n\nProvide feedback on whether the answer addresses the following:"
    #                                     f" 1. Understanding of the material"
    #                                     f" 2. Understanding of their own thought process"
    #                                     f" 3. Self-regulated learning - Comprehension monitoring"
    #                                     f" 4. Self-regulated learning - Goal setting"},
    #     ],
    #     max_tokens=500
    # )
    
    # feedback = response.choices[0].message['content'].strip()
    feedback = """Okay then, here's my evaluation.
    Understanding of the Material:
    Your answer correctly identifies the significance of the war as 
    the shortest in recorded history and highlights Britain's 
    military power. You also mention the broader context of 19th-century 
    geopolitics, which demonstrates a solid understanding of the material.

    Understanding of Their Own Thought Process:
    You provided a clear and logical explanation, 
    showing that you understand the historical significance and 
    can articulate the impact of the event. This indicates a good 
    grasp of your own thought process in interpreting the material.

    Self-Regulated Learning - Comprehension Monitoring:
    While you have understood the key points, 
    it would be beneficial to include specific strategies you 
    used to remember and process this information. For example, 
    did you create any mental associations or summaries?

    Self-Regulated Learning - Goal Setting:
    Your answer does not mention any specific goals you set 
    while studying this text. In future, try to articulate your 
    learning objectives and the methods you plan to use to achieve 
    them. For instance, setting a goal to understand the broader 
    impacts of colonial wars on global history and reviewing related materials.

    Overall, your answer demonstrates a good understanding of 
    the material and thought process. However, incorporating more 
    explicit self-regulated learning strategies would 
    further strengthen your response.
    """
    return feedback

