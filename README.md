# PillPal💊

## Problem Statement

Have you ever come across the thin piece of folded paper that is part of every drug prescription box. Usually the text is in very small print and typically provides information about dosages, side effects, storage instructions and much more. They are hard to read and understand and requires some effort to get answers to common questions that you as a patient might have.

## Solution

Create a product that answers these questions and actually makes the medical information more accessible and easier to understand - enter PillPal💊

A Retrieval Augmented Generation (RAG) based chatbot that answers questions based on the PDF document.

## Environement Setup

```bash
python -V
# Output: Python 3.12.1
```

```bash
# create a environment named -> nvidia-ai
python -m venv nvidia-ai
```

```bash
# activate the environment
source nvidia-ai/bin/activate
```

```bash
# create a Jupyter Notebook kernel
pip install jupyter ipykernel
```

```bash
# add your virtual environment as a kernel
python -m ipykernel install --user --name=nvidia-ai --display-name="Py3.12-nvidia-ai"
```

```bash
# verify kernel installation
jupyter kernelspec list
```

## ARCHITETURE OF THE APPLICATION

### MODELS

#### RAG LLM

- [**Model Card**](https://build.nvidia.com/meta/llama-3.2-1b-instruct/modelcard)

#### EMBEDDING MODEL

- [**Model Card**](https://build.nvidia.com/nvidia/llama-3_2-nv-embedqa-1b-v1/modelcard)

#### RERANK MODEL

- [**Model Card**](https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v1/modelcard)

#### Llama Guard 3 8B

- **Model ID:** `llama-guard-3-8b`
- **Developed by:** `Meta`
- **Context Window:** `8,192 tokens`
- [**Model Card**](https://huggingface.co/meta-llama/Llama-Guard-3-8B)

## Built for

[NVIDIA and LlamaIndex Developer Contest](https://developer.nvidia.com/llamaindex-developer-contest)