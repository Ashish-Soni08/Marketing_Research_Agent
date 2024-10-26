import os

from gradio import ChatMessage
from gradio_pdf import PDF
import gradio as gr

from backend import llm_response

hf_writer = gr.HuggingFaceDatasetSaver()


inputs = [PDF(label="Upload a PDF", interactive=True),
          gr.Textbox(label="Ask a question", placeholder="What is the drug interaction between aspirin and ibuprofen?", lines=5)
          ]

outputs = []

examples = []

theme = gr.themes.Soft()

title = """<h1 id="title"> PillPal💊</h1>"""

description = """

"""

css = """h1#title {
    text-align: center;
    } 
"""

pillpal_bot = gr.Blocks(css=css, theme=theme)

with pillpal_bot:
    gr.Markdown(title)
    gr.Markdown(description)
    

    interface = gr.ChatInterface(
        fn=llm_response,
        type="messages",
        title="PillPal💊",
        inputs=inputs,
        outputs=outputs,
        examples=examples,
        cache_examples=True,
        retry_btn=None,
        undo_btn="Delete Previous"
        clear_btn="Clear",
        flagging_options=[],
        flagging_callback=hf_writer
    )

pillpal_bot.launch(debug=True)