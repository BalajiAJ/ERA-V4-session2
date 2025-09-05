# TinyNLP Explorer – Tokenization & Word-Level One-Hot Visualization

## Overview

**TinyNLP Explorer** is a lightweight web application built with **Flask** and **Bootstrap** that allows users to explore **text tokenization** and **word-level one-hot encoding** interactively.  

It is designed for beginners, educators, and NLP enthusiasts who want to **visualize how different tokenization methods work** and understand **basic NLP concepts** like one-hot encoding and token metrics.

The app supports:

- **Tokenization Methods**:
  - **Character-based** – splits text into individual characters.
  - **Word-based** – splits text into words using whitespace and punctuation.
  - **Subword-based** – splits words into smaller subword chunks (for demonstration purposes).
  
- **One-Hot Encoding**:
  - Always computed at **word level**, showing how each word maps to a binary vector based on the vocabulary of the text.

- **Tokenization Metrics**:
  - **Number of tokens** – total tokens produced by the tokenizer.
  - **Number of words** – total words in the input text.
  - **Average token length** – average number of characters per token.
  - **Fertility Ratio** – **ratio of number of tokens to number of words**.  
    - **Definition**:  
      ```
      Fertility Ratio = Number of Tokens / Number of Words
      ```  
      - A high fertility ratio indicates finer tokenization (e.g., character-based), while a ratio close to 1 indicates word-level tokenization.

## Features

- Real-time tokenization based on selected method.
- Interactive visualization of tokens with color-coded highlights.
- Word-level one-hot encoding with a clear table display.
- Tokenization metrics including fertility ratio for quick analysis.
- Responsive **Bootstrap UI** with tabs for easy navigation between tokens and one-hot encoding.