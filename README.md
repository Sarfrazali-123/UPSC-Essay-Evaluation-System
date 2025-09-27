# 🚀 Parallel Workflow for UPSC Essay Evaluation 🚀

## Introduction

This project introduces a **Parallel Workflow for UPSC Essay Evaluation**, designed to assist UPSC aspirants in improving their essay writing skills. Leveraging **LangGraph**, the platform allows users to submit essays and receive detailed feedback across multiple dimensions, ensuring a comprehensive evaluation process. The workflow evaluates essays based on three key aspects: clarity of thought, depth of analysis, and language quality.

## How It Works

The evaluation process begins when the essay is submitted. The essay is then analyzed in parallel across three key aspects, ensuring that each aspect is reviewed independently. This parallel evaluation process enables more accurate and holistic feedback.

### 1. **Start Node**  
   - The workflow receives the essay and initiates the evaluation process.

### 2. **Evaluation on Key Aspects**  
The essay is evaluated in the following three areas:
   - **Clarity of Thought**: This evaluates how clear and coherent the essay’s arguments and ideas are.  
     **Score**: 0-10
   - **Depth of Analysis**: This measures how deeply the topic is explored and the analysis presented.  
     **Score**: 0-10
   - **Language**: This assesses the quality of language, including grammar, vocabulary, and fluency.  
     **Score**: 0-10

### 3. **Final Evaluation**  
   - After the independent assessments for each aspect, the results are merged and summarized using a **Large Language Model (LLM)**. This results in:
     - **Final Evaluation Score**: The average score based on the three key aspects.
     - **Comprehensive Feedback Report**: Detailed suggestions to help candidates improve their essays.


## Demo
![Demo Image 1](https://github.com/Sarfrazali-123/UPSC-Essay-Evaluation-System/blob/511bc5cd4b4508a0efad07f8c3ae26c41ca42c3c/Capture-145.PNG) 
![Demo Image 1](https://github.com/Sarfrazali-123/UPSC-Essay-Evaluation-System/blob/511bc5cd4b4508a0efad07f8c3ae26c41ca42c3c/Capture-7.PNG) 
![Demo Image 1](https://github.com/Sarfrazali-123/UPSC-Essay-Evaluation-System/blob/511bc5cd4b4508a0efad07f8c3ae26c41ca42c3c/Capture-60.PNG) 
## Technology Behind the Scenes

This workflow is built using **LangGraph**, a powerful tool that enables efficient design and management of parallel processes. LangGraph facilitates the independent evaluation of different essay aspects while merging the results seamlessly for a cohesive final assessment.

## Features

- Parallel evaluation of key essay aspects: **Clarity of Thought**, **Depth of Analysis**, and **Language**.
- Automatic merging and summarization of feedback for a final comprehensive report.
- Designed specifically for UPSC aspirants to provide valuable insights into essay writing.

## Use Cases

- **UPSC Aspirants**: Ideal for candidates preparing for the UPSC Civil Services Examination, allowing them to assess the quality of their essay writing.
- **General Essay Improvement**: Perfect for anyone looking to improve their essay writing by receiving structured feedback.

## How to Use

1. **Submit Your Essay**: Provide the essay that you want to have evaluated.
2. **Wait for Evaluation**: The essay will undergo parallel evaluation on the three key aspects.
3. **Receive Feedback**: Once the evaluation is complete, you'll receive a detailed feedback report, including scores and suggestions for improvement.

## Future Improvements

- Integration with additional scoring mechanisms and AI-driven tips for specific essay improvement.
- Additional metrics for evaluating writing style, creativity, and originality.
- Continuous enhancement of the evaluation algorithm for more accurate feedback.

## Contributing

Feel free to contribute to this project! If you have suggestions or improvements, open an issue or submit a pull request.

### Technologies Used:
- **LangGraph** for managing parallel workflows.
- **Large Language Models (LLMs)** for summarizing feedback and scoring.
- **Python** for backend processing and automation.



Happy Learning and Writing! ✍️
