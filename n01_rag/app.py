import gradio as gr
import random

retrieval_results = [
    {"text": "빠른 갈색 여우가 게으른 개를 뛰어넘습니다. 이 문장은 여우의 활동성과 개의 게으름을 대조적으로 보여줍니다.", "file": "file01.txt"},
    {"text": "게으른 개는 에너지 넘치는 여우를 지켜봅니다. 이 문장은 개의 무관심과 여우의 에너지를 대조적으로 보여줍니다.", "file": "file02.txt"},
    {"text": "여우는 개를 민첩하게 뛰어넘습니다. 이 문장은 여우의 민첩성을 강조하고 있습니다.", "file": "file03.txt"},
    {"text": "개는 게으르게 점프하는 여우를 무시합니다. 이 문장은 개의 게으름과 여우의 활동성을 대조적으로 보여줍니다.", "file": "file04.txt"}
]

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            with gr.Group():
                retrieval01_chunk = gr.Textbox(label="Chunk 1")
                with gr.Row():
                    retrieval01_file = gr.Textbox(scale=2, label="File containing chunk 1")
                    retrieval01_feedback = gr.Radio(choices=["Good", "Bad"], value="Good", label="Feedback for chunk 1")
            with gr.Group():
                retrieval02_chunk = gr.Textbox(label="Chunk 2")
                with gr.Row():
                    retrieval02_file = gr.Textbox(scale=2, label="File containing chunk 2")
                    retrieval02_feedback = gr.Radio(choices=["Good", "Bad"], value="Good", label="Feedback for chunk 2")
                    
            with gr.Group():
                retrieval03_chunk = gr.Textbox(label="Chunk 3")
                with gr.Row():
                    retrieval03_file = gr.Textbox(scale=2, label="File containing chunk 3")
                    retrieval03_feedback = gr.Radio(choices=["Good", "Bad"], value="Good", label="Feedback for chunk 3")

            with gr.Group():
                retrieval04_chunk = gr.Textbox(label="Chunk 4")
                with gr.Row():
                    retrieval04_file = gr.Textbox(scale=2, label="File containing chunk 4")
                    retrieval04_feedback = gr.Radio(choices=["Good", "Bad"], value="Good", label="Feedback for chunk 4")

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
    
    def respond(message, chat_history, *args):
        chunks = args[:4]
        feedback = args[4:]
        valid_results = []
        for feedback, chunk in zip(feedback, chunks):
            if feedback == "Good":
                valid_results.append(chunk)
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"]) + '\n' + '\n'.join(valid_results)
        chat_history.append((message, bot_message))
        return message, chat_history
    
    btn_answer.click(respond,
                    inputs=[msg, chatbot,
                            retrieval01_chunk, retrieval02_chunk, retrieval03_chunk, retrieval04_chunk,
                            retrieval01_feedback, retrieval02_feedback, retrieval03_feedback, retrieval04_feedback],
                    outputs=[msg, chatbot])
    
if __name__ == "__main__":
    demo.queue().launch()