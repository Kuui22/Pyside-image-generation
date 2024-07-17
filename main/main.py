import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
import gc,torch,string,random,os,asyncio
import accelerate
from diffusers import StableDiffusionPipeline
from PIL import Image
import asyncio,threading

localmodel:str = '../static/stable1-5/'
modelurl:str = "runwayml/stable-diffusion-v1-5" #https://huggingface.co/runwayml/stable-diffusion-v1-5
directory:str = '../media/images'



def async_setup(coroutine):
     async_loop = asyncio.new_event_loop()
     asyncio.set_event_loop(async_loop)
     async_loop.run_until_complete(coroutine)
     
def FlushPipe(pipe,image=None):
    try:
        pipe.maybe_free_model_hooks()
        del pipe
        del image
        gc.collect()
        torch.cuda.empty_cache()
        gc.collect()
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

def GenerateImage(prompt,negative_prompt="",height=512,width=512,guidance_scale=7.0,num_inference_steps=35,button=None):
    try:
        button.setEnabled(False)
        pipe:StableDiffusionPipeline = StableDiffusionPipeline.from_pretrained(localmodel, torch_dtype=torch.float16, safety_checker=None)
        pipe.enable_model_cpu_offload()
    except Exception as e:
        print(f"Error setting model: {e}")
    try:
        print(f"Generating image: Prompt={prompt} \n Height/Width={height}/{width} \n Guidance scale/Steps={guidance_scale}/{num_inference_steps}" )
        image:Image = pipe(
            prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            height=height,
            width=width,
        ).images[0]   
        SaveImage(image,prompt)
        FlushPipe(pipe,image)
        button.setEnabled(True)
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
        prompt:str = self._ui.promptText.toPlainText()
        negativeprompt:str = ""
        height:int = int(self._ui.heightBox.currentText())
        width:int = int(self._ui.widthBox.currentText())
        guidance_scale:float = float(self._ui.editGuidance.text())
        num_inference_steps:int = int(self._ui.editInference.text())
        if(prompt):
            
            coroutine = GenerateImage(prompt,negativeprompt,height,width,guidance_scale,num_inference_steps,self._ui.okButton)
            async_thread = threading.Thread(target=async_setup,daemon=True,args=(coroutine,))
            async_thread.start()
            #GenerateImage(prompt,negativeprompt,height,width,guidance_scale,num_inference_steps)
            print("Done!")
        else:
            print("No prompt found")
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec())
    finally:
        #async_loop.call_soon_threadsafe(async_loop.stop)
        #async_thread.join()
        torch.cuda.empty_cache()
        gc.collect()
        print("Goodbye")
