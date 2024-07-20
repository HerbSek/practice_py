# import pymupdf
# from sklearn.model_selection import train_test_split
# from transformers import pipeline
# import numpy as np

# doc = pymupdf.open("Sekpey_Herbert.pdf")
# out = open("output.txt", "wb")

# for page in doc:
#     text = page.get_text().encode('utf8') 
#     out.write(text)
#     # out.write(bytes((12,)))
# out.close()

# # Read your text file
# with open('output.txt', 'r',  encoding='utf-8') as file:
#     data = file.readlines()


# train_data, test_data = train_test_split(data,test_size = 0.2,)

# my_data = ""
# for i in train_data:
#     my_data += i + ""
# # print(my_data ,end = " ")
# extracted_text = my_data
# # Preprocess the text: clean up whitespace
# extracted_text = extracted_text.replace("\n", " ").strip()

# # Step 2: Set up the transformer model for question answering
# qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# # Step 3: Ask questions based on the extracted text
# def answer_question(question, context):
#     result = qa_model(question=question, context=context)
#     return result['answer']



# # If you want to interactively ask questions, you can use the input function
# while True:
#     user_question = input("Ask a question (or type 'exit' to quit): ")
#     if user_question.lower() == 'exit':
#         break
#     user_answer = answer_question(user_question, extracted_text)
#     print(f"Answer: {user_answer}")
#     print()

