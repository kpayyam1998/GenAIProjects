"""
    This is main page which will intract with helper.py and store_index.py as well
"""

import os
from dotenv import load_dotenv

from flask import Flask,render_template,jsonify,request
from langchain.vectorstores import Chroma
from src.helper import load_embedding,repo_ingestion
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

app=Flask(__name__)

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

embeddings=load_embedding()
persist_directory="db"

#Now we can load persisted database from disk,and use it as normal

vectordb=Chroma(persist_directory=persist_directory,embedding_function=embeddings)

llm=ChatOpenAI()

memory=ConversationSummaryMemory(llm=llm,memory_key="chat_history",return_messages=True)
qa=ConversationalRetrievalChain.from_llm(llm,retriever=vectordb.as_retriever(search_type="mmr",search_kwargs={"k":3}),memory=memory)



# Coonect with front end
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/chatbot',methods=["GET","POST"])
def git_repo():
    if request.method=="POST":
        user_input=request.form['question']
        repo_ingestion(user_input)
        os.system("python store_index.py")
    return jsonify({"response":str(user_input)})

@app.route("/get",methods=["GET","POST"])
def chat():
    msg=request.form["msg"]
    input=msg
    print(input)

    if input=="clear":
        os.system("rm -rf repo")
    result=qa(input)
    print(result['answer'])
    return str(result['answer'])        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)