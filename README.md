# LLM Amharic
The best Amharic Large language model! Our goal is to help African businesses by using new technology in AI. By using advanced AI, this project aims to provide smooth, Amharic support across different platforms.

This repository contains scripts and instructions to fine-tune the LLaMA-2-7b-chat model for Amharic customer support using data stored in a PostgreSQL database.


## Project Structure
```
llm-amharic/
├── api/
│ └──  app.py
├── docker/
│ ├── Dockerfile
│ └── docker-compose.yml
├── scripts/
│ └── inference_script.py
├── scripts/
│ └── finetuning
│   └─ finetuning.py
├── pretrain/
│ └── pretrain.py
├── utils/
│ ├── data_preprocessing.py
│ └── fetch_data_from_db.py
├── .gitignore
└── README.md
```


## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- CUDA-enabled GPU (optional but recommended for training)


### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/10-academy-w5-group-2/llm-amharic.git
    cd llm-amharic
    ```

2. **Set up a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install Requirements:**
    ```sh
    pip install -r requirements.txt
    ```

## Database Setup
Ensure your PostgreSQL database is set up with the required data. The table should have a column containing the Amharic text data for training.

### Usage

To test the inference of the model being used you'll need to follow this steps:

1. Accept Llama2 license on huggingface and download it like this:

 - git lfs install
 - git clone https://huggingface.co/meta-llama/Llama-2-7b-hf

2. Download the amharic finetune from huggingface like this:

 - git lfs install
 - git clone https://huggingface.co/iocuydi/llama-2-amharic-3784m

3. Clone https://github.com/iocuydi/amharic-llama-llava repository

4. Then inside inference/run_inf.py:

    - change the MAIN_PATH to the path to folder you downloaded from step 1
    - change the peft_model to the path you cloned in the step 2
    - Go to your llama2 folder(from step 1) and replace the tokenizer related files with the one you find from the 2nd step
    - set quanitzation=True inside the main function before the load_model function call

5. Finally run the inference/run_inf.py file

    
## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License.


## Contributors

- [@abyt101](https://github.com/AbYT101) - Abraham Teka
- [@nyutu-grace](https://github.com/nyutu-grace) - Grace Nyutu

<br>

## Challenge by

![10 Academy](https://static.wixstatic.com/media/081e5b_5553803fdeec4cbb817ed4e85e1899b2~mv2.png/v1/fill/w_246,h_106,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/10%20Academy%20FA-02%20-%20transparent%20background%20-%20cropped.png)
