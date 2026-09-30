# NanoGPT

A character-level GPT language model built from scratch with PyTorch. The project demonstrates token encoding, causal self-attention, transformer blocks, training, validation, and text generation from custom prompts.

## Project Structure

- `nanoV1.ipynb`: Main notebook containing the model and training workflow.
- `dev.ipynb`: Development notebook.
- `train.py`: Loads and reports the training text from `DATA/input.txt`.
- `DATA/input.txt`: Training corpus.
- `requirements.txt`: Python dependencies.

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the Notebook

Start Jupyter from the project directory:

```bash
jupyter notebook
```

Open `nanoV1.ipynb` and run the cells in order. The notebook builds a character-level vocabulary, creates train and validation splits, defines the transformer model, trains it, and generates text.

## Device Selection

The notebook supports Apple Silicon GPU acceleration through MPS and falls back to CPU:

```python
device = 'mps' if torch.backends.mps.is_available() else 'cpu'
```

Check the active device with:

```python
print("Selected device:", device)
print("Model device:", next(m.parameters()).device)
```

## Generate Text from a Prompt

After training, provide a prompt that uses characters present in `DATA/input.txt`:

```python
prompt = "Once upon a time"
context = torch.tensor([encode(prompt)], dtype=torch.long, device=device)

model.eval()
with torch.no_grad():
    generated = m.generate(context, max_new_tokens=200)

print(decode(generated[0].tolist()))
```

This is a character-level language model, so it predicts one character at a time rather than answering questions with a chat-style instruction format.

## License

No license has been specified yet.
