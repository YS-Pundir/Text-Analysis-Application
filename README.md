# Text Analysis Application in Python

A comprehensive Python-based text processing tool that analyzes text input and provides detailed statistics, frequency analysis, and visualization.

## 📋 Features

### Input Methods
- **Direct Text Input**: Type or paste text directly into the program
- **File Input**: Load text from `.txt` files
- **Flexible Data Handling**: Text processed as list data structures

### Text Processing Statistics
- **Character Count**: Total characters (with and without spaces)
- **Word Count**: Total words (punctuation-aware)
- **Sentence Count**: Based on punctuation marks (., !, ?)
- **Paragraph Count**: Based on empty line separation
- **Data Storage**: All statistics stored in key-value dictionary format

### Advanced Analysis
- **Unique Word Frequency**: Count occurrences of each unique word
- **Case Normalization**: All words converted to lowercase
- **Punctuation Removal**: Clean text for accurate word counting
- **Top 10 Words**: Display most frequent words with their counts

### Visualization
- **Bar Chart Generation**: Visual representation using matplotlib
- **Key Metrics Display**: Words, sentences, paragraphs, and unique words

## 🏗️ Project Structure

The project includes two implementations:

1. **Modular Version** (`text_analyzer_modular.py`)
   - Function-based approach
   - Clean, reusable functions
   - Straightforward procedural flow

2. **Object-Oriented Version** (`text_analyzer_oop.py`)
   - `TextAnalyzer` class implementation
   - Encapsulated methods and properties
   - Object-oriented design patterns

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Required libraries:
  ```bash
  pip install matplotlib
Installation
Clone the repository:

bash
git clone (https://github.com/YS-Pundir/Text-Analysis-Application.git)
cd text-analysis-app
Run the program:

Modular version:

bash
python text_analyzer_modular.py
Object-Oriented version:

bash
python text_analyzer_oop.py
📊 Usage Examples
Sample Output
text
Total characters (with spaces): 1450
Total characters (without spaces): 1203
Total words: 250
Total sentences: 15
Total paragraphs: 3

---

Top 10 Most Common Words:
the: 25
and: 18
python: 15
text: 12
analysis: 10
program: 8
words: 8
count: 7
sentences: 6
paragraphs: 5
Visualization
The program generates a bar chart visualizing:

Total words

Total sentences

Total paragraphs

Total unique words

🧪 Testing
The program includes sample text for testing. You can also:

Type your own text when prompted

Load from text files in the samples/ directory

Test with various text formats and lengths

📁 Project Files
text_analyzer_modular.py - Modular/functional implementation

text_analyzer_oop.py - Object-oriented implementation

samples/ - Sample text files for testing

requirements.txt - Python dependencies

output_examples/ - Sample outputs and charts

📝 Code Quality Features
Modular Version
Separation of Concerns: Each function handles a specific task

Reusability: Functions can be imported and reused

Readability: Clear function names and documentation

Object-Oriented Version
Encapsulation: Data and methods bundled in a class

Extensibility: Easy to add new features

Maintainability: Organized class structure

🎯 Learning Outcomes
This project demonstrates:

Text processing and manipulation in Python

Data structure usage (lists, dictionaries)

Statistical analysis implementation

Data visualization with matplotlib

Both functional and object-oriented programming paradigms

File I/O operations

User interface design for console applications

🤝 Contributing
Feel free to fork this project and submit pull requests with enhancements such as:

Additional text analysis features

More visualizations

Web interface implementation

Performance optimizations

Additional language support

📄 License
This project is available for academic and learning purposes.

👨‍💻 Author
Your Name - Yuvraj Singh Pundir

⏰ Timeline
Project Start: december 23,2025

Project End: December 24, 2025
