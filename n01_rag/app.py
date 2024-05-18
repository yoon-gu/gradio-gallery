import gradio as gr
import random

retrieval_results = [
    {"text": "The quick brown fox jumps over the lazy dog.", "file": "file01.txt"},
    {"text": "The quick brown fox jumps over the lazy dog.", "file": "file02.txt"},
    {"text": "The quick brown fox jumps over the lazy dog.", "file": "file03.txt"},
    {"text": "The quick brown fox jumps over the lazy dog.", "file": "file04.txt"}
]

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            with gr.Group():
                retrieval01_chunk = gr.Textbox(label="Chunk 1")
                with gr.Row():
                    retrieval01_file = gr.Textbox(scale=2, label="File containing chunk 1")
                    retrieval01_feedback = gr.Radio(choices=["Good", "Bad"], label="Feedback for chunk 1")
            with gr.Group():
                retrieval02_chunk = gr.Textbox(label="Chunk 2")
                with gr.Row():
                    retrieval02_file = gr.Textbox(scale=2, label="File containing chunk 2")
                    retrieval02_feedback = gr.Radio(choices=["Good", "Bad"], label="Feedback for chunk 2")
                    
            with gr.Group():
                retrieval03_chunk = gr.Textbox(label="Chunk 3")
                with gr.Row():
                    retrieval03_file = gr.Textbox(scale=2, label="File containing chunk 3")
                    retrieval03_feedback = gr.Radio(choices=["Good", "Bad"], label="Feedback for chunk 3")

            with gr.Group():
                retrieval04_chunk = gr.Textbox(label="Chunk 4")
                with gr.Row():
                    retrieval04_file = gr.Textbox(scale=2, label="File containing chunk 4")
                    retrieval04_feedback = gr.Radio(choices=["Good", "Bad"], label="Feedback for chunk 4")

        with gr.Column():
            chatbot = gr.Chatbot(show_copy_button=True, likeable=True, show_share_button=True)
            with gr.Row():
                msg = gr.Textbox(scale=4, label="Message")
                btn_search = gr.Button("Search")
                btn_answer = gr.Button("Answer")
            gr.Examples(examples=["Hello", "Hi"], inputs=msg, label="Chat History")
                
    
    def update_on_load(msg):
        return [result['text'] for result in retrieval_results] + [result['file'] for result in retrieval_results]
    
    btn_search.click(update_on_load, inputs=msg, outputs=[retrieval01_chunk, retrieval02_chunk,
                                                    retrieval03_chunk, retrieval04_chunk,
                                                    retrieval01_file, retrieval02_file,
                                                    retrieval03_file, retrieval04_file])
    
    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        return "", chat_history
    
    btn_answer.click(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    
if __name__ == "__main__":
    demo.queue().launch()