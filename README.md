# EmotionAnalyzerWebApp

## Preview

![Example Image](images/preview.png)
![Example Image](images/preview2.png)


## Getting Started

Follow these steps to run the project locally:

1. **Clone the repository:**

   Open your terminal and run the following command to clone the repository:
   ```Shell
   git clone https://github.com/guhyun9454/EmotionAnalyzerWebApp
   ```

2. **Navigate to the project directory:**

   After cloning, change into the project directory:
   
   ```Shell
   cd [cloned directory]
   ```

3. **Start the application:**

   Run the following command in the terminal to start the application using Docker Compose:

   ***Make sure that you installed and run Docker Desktop or Docker Daemon***
   ```Shell
   docker compose up
   ```

4. **Access the application:**

   Open your web browser and go to "http://localhost:8501" to experience the application.

5. **Explore**
   
   Test with your own images or test image provided.
   
   ***Accuracy may be poor for faces that do not look forward.***

5. **Stop the application**

   To stop and remove all stuffs created by `docker compose up`, run the following command in the terminal:
   ```Shell
   docker compose down  
   ```

## Architecture

![Example Image](images/architecture.jpeg)

The system uses a microservice architecture orchestrated by Docker Compose.

## AI Model Details
- The emotion classification model is based on a CNN architecture optimized for detecting subtle facial features and expressions.
- The model was trained from the scratch on a dataset specifically designed for Korean facial features to ensure higher accuracy in the target demographic. You can find the dataset [here](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=83).

This repository deploys the previously trained model as a web application. The training process involved testing multiple models and fine-tuning the architecture for optimal performance. The data was preprocessed and analyzed to ensure high-quality inputs for training. For detailed information on the model training process and to view the full report, please visit the [training report repository](https://github.com/guhyun9454/VisionAssistEmotionAI).