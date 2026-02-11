# **Hybrid Local & Cloud LLM Chat Application**

This project is a Streamlit web application that allows users to chat with a large language model (LLM). It's uniquely designed to run in two modes:

1. **Local Mode:** Uses a smaller, open-source model (like Google's gemma:2b) running on your own computer via Ollama for quick, private, and free responses.  
2. **Cloud Mode:** Uses a powerful, state-of-the-art model (like Google's gemini-1.5-flash) via a remote API for more complex and nuanced conversations.

This is the link to the live [App](https://simple-assistant.streamlit.app/)

## **Features**

* **Dual Model System:** Switch between a local and a cloud-based LLM with a simple checkbox.  
* **Persistent Chat History:** Remembers your conversation within a session.  
* **Dockerized Environment:** Fully containerized with Docker Compose for easy setup and consistent performance across different machines.  
* **Cloud-Ready:** Includes a separate, simplified version of the app ready for deployment to cloud services like Streamlit Community Cloud.

## **Local Development Setup**

Follow these steps to run the full application (with both local and cloud models) on your computer.

### **Prerequisites**

* **Docker Desktop:** Make sure Docker is installed and running on your machine.  
* **Google API Key:** You need an API key from [Google AI Studio](https://aistudio.google.com/) to use the Gemini model.

### **1\. Clone the Repository**

First, get the project files onto your machine (from the 'develop' branch).

git clone https://github.com/christian-freshness/Hybrid-Local-Cloud-LLM-Chat-Application.git  
cd Hybrid-Local-Cloud-LLM-Chat-Application

### **2\. Configure Environment Variables**

Create a .env file in the root of the project folder. This file will store your secret API key.

\# .env  
GOOGLE\_API\_KEY="your\_actual\_google\_api\_key\_goes\_here"

### **3\. Build and Run with Docker Compose**

This single command will build the necessary Docker images (including downloading the local gemma:2b model, which is \~1.7 GB) and start the application.

docker-compose up \--build

The first build will take some time. Subsequent startups will be much faster.

### **4\. Access the Application**

Once the containers are running, open your web browser and go to:

**http://localhost:8501**

You should now be able to chat with the models.

## **Deployment to the Cloud**

This project is configured for easy deployment to **Streamlit Community Cloud**. Note that the deployed version will **only use the remote Gemini model**, as cloud servers are not powerful enough to run local models.

### **1\. Prepare Your GitHub Repository**

* Make sure you have a .gitignore file that includes .env to keep your API key secret.  
* Push the following files to your public GitHub repository:  
  * app.py (from 'main' branch)  
  * requirements.txt (from 'main' branch)

### **2\. Deploy on Streamlit Community Cloud**

1. Log in to [Streamlit Community Cloud](https://share.streamlit.io/).  
2. Click "New app" and select your GitHub repository.  
3. In the "Advanced settings", add your Google API key as a secret:  
   \# secrets.toml  
   GOOGLE\_API\_KEY="your\_actual\_google\_api\_key\_goes\_here"

4. Click "Deploy\!". Your app will be live in a few minutes.
