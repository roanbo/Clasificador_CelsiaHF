import re
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import chardet
import pandas as pd


# Validador de texto
class TextValidator:
    def validate(self, text):
        if len(text.strip()) < 3:
            return False
        if not re.match(r"^[a-zA-Z0-9ñÑ\s.,!?]+$", text):
            return False
        if text.strip().isdigit():
            return False
        return True


# Modelo de Hugging Face
class HuggingFaceModel:
    def __init__(self, model_name="jcortizba/modelo18", validator=None):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.label_mapping = {0: "ejecutar", 1: "cancelar"}
        self.validator = validator or TextValidator()

    def predict(self, text):
        if not self.validator.validate(text):
            return "Entrada inválida. Por favor, ingrese un texto coherente."

        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_index = torch.argmax(probabilities, dim=1).item()
        return self.label_mapping[predicted_index]


# Procesador de archivos CSV
class CSVProcessor:
    def __init__(self, model):
        self.model = model

    def process_file(self, file):
        try:
            with open(file.name, 'rb') as f:
                raw_data = f.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']

            df = pd.read_csv(file.name, encoding=encoding)

            if 'daño' not in df.columns:
                return "Error: El archivo no tiene una columna llamada 'daño'.", None

            df['Predicción'] = df['daño'].apply(self.model.predict)
            output_file = "resultado_predicciones.csv"
            df.to_csv(output_file, index=False, encoding='utf-8')
            return "Archivo procesado exitosamente.", output_file
        except Exception as e:
            return f"Error al procesar el archivo: {e}", None


# Interfaz Gradio
class GradioInterface:
    def __init__(self, model, processor):
        self.model = model
        self.processor = processor

    def launch(self):
        with gr.Blocks() as demo:
            gr.Markdown("# Modelo Hugging Face - Predicción desde archivo CSV o Texto")

            gr.Markdown("## Predicción desde archivo CSV")
            file_input = gr.File(label="Sube un archivo .csv", file_types=[".csv"])
            output_message = gr.Textbox(label="Estado del proceso", interactive=False)
            result_file = gr.File(label="Archivo con predicciones")
            submit_btn = gr.Button("Procesar archivo")

            submit_btn.click(
                fn=lambda file: self.processor.process_file(file),
                inputs=[file_input],
                outputs=[output_message, result_file],
            )

            gr.Markdown("## Predicción desde texto")
            text_input = gr.Textbox(label="Escribe el texto para predecir")
            text_output = gr.Textbox(label="Predicción", interactive=False)
            predict_btn = gr.Button("Predecir texto")

            predict_btn.click(
                fn=lambda text: self.model.predict(text),
                inputs=[text_input],
                outputs=[text_output],
            )

        demo.launch()


# Main
if __name__ == "__main__":
    validator = TextValidator()
    model = HuggingFaceModel(validator=validator)
    processor = CSVProcessor(model=model)
    interface = GradioInterface(model=model, processor=processor)
    interface.launch()
