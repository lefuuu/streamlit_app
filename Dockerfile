FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
EXPOSE 8502
CMD ["sh", "-c", "streamlit run streamlit_apple.py --server.port=8501 & streamlit run tips_visual.py --server.port=8502"]
