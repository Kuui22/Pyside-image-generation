import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
import gc,torch,string,random,os,asyncio
import accelerate
from diffusers import StableDiffusionPipeline
from PIL import Image

localmodel:str = '../static/stable1-5/'
modelurl:str = "runwayml/stable-diffusion-v1-5" #https://huggingface.co/runwayml/stable-diffusion-v1-5
directory:str = '../media/images'


def FlushPipe(pipe,image=None):
    try:
        pipe.maybe_free_model_hooks()
        del pipe
        del image
        gc.collect()
        torch.cuda.empty_cache()
    except Exception as e:
        print(f"Failed to clear: {e}")
        
        

def generate_random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def SaveImage(image,prompt):
    try:
        base_filename:str = f"{prompt[:10].replace(' ', '_')}"
        image_path:str = os.path.join(directory,f"{base_filename}.png").replace("\\", "/")
    
        while os.path.exists(image_path):
            random_suffix:str = generate_random_string()
            image_path = os.path.join(directory, f"{base_filename}_{random_suffix}.png").replace("\\", "/")

        image.save(image_path)
    except Exception as e:
        print(f"Error saving: {e}")

def GenerateImage(prompt):
    try:
        pipe:StableDiffusionPipeline = StableDiffusionPipeline.from_pretrained(localmodel, torch_dtype=torch.float16, safety_checker=None)
        pipe.enable_model_cpu_offload()
    except Exception as e:
        print(f"Error setting model: {e}")
    try:
        image:Image = pipe(
            prompt,
            negative_prompt="",
            num_inference_steps=56,
            guidance_scale=7.0,
            height=512,
            width=512,
        ).images[0]   
        SaveImage(image,prompt)
        FlushPipe(pipe,image)
    except Exception as e:
        print(f"Error generating: {e}")
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self) 
        self._ui.okButton.clicked.connect(self.ExecutePrompt)
        self._ui.actionExit.triggered.connect(self.close)

    @Slot()
    def ExecutePrompt(self):
        text:str = self._ui.promptText.toPlainText()
        if(text):
            GenerateImage(text)
            print("Done!")
        else:
            print("No text found")
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

