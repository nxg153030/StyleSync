# StyleSync

This project aims to bridge visual product attributes with customer-centric language. It consists of three main components: a Visual Attribute Extractor, a Semantic Mapper, and a Cross-Modal Fusion system. 

## Project Structure

- **src/**: Contains the source code for the project.
  - **visual_attribute_extractor/**: Implements the Visual Attribute Extractor using CNN/Transformer models.
  - **semantic_mapper/**: Implements the Semantic Mapper using fine-tuned language models.
  - **cross_modal_fusion/**: Contains logic for aligning visual and textual features.
  - **utils/**: Includes utility functions and helper methods.
  - **main.py**: The entry point for the application.

- **data/**: Contains directories for raw, processed, and sample data files.
  
- **models/**: Holds saved model files and configurations for each component.

- **tests/**: Contains unit tests for each component of the project.

- **requirements.txt**: Lists the dependencies required for the project.

- **.gitignore**: Specifies files and directories to be ignored by version control.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-attribute-harmonizer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare your data by placing raw files in the `data/raw` directory and processing them as needed.

## Usage Guidelines

To run the application, execute the following command:
```
python src/main.py
```

This will orchestrate the execution of the Visual Attribute Extractor, Semantic Mapper, and Cross-Modal Fusion components, generating customer-centric product descriptions based on visual attributes. 
 

## License

This project is licensed under the MIT License. See the LICENSE file for more details.