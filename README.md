# Marketing_Research_Agent

[NVIDIA and LlamaIndex Developer Contest](https://developer.nvidia.com/llamaindex-developer-contest)

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