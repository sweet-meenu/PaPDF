import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import os

import google.generativeai as genai

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
