import gradio as gr
import analysers

#输入文本处理程序
def greet(ctdContent):
    return "Clinical Trial Data was received."

def ctdAnalyse(ctdContent) -> str:
    inst = analysers.Analyser()
    return str(inst.ctd_analyser(ctdContent))

#接口创建函数
#fn设置处理函数，inputs设置输入接口组件，outputs设置输出接口组件
#fn,inputs,outputs都是必填函数
demo = gr.Interface(fn=ctdAnalyse, 
                    title="Clinical Trial Data Submission",
                    description="CTD Submission App. Developed by Kozmosa",
                    inputs=gr.Textbox(lines=3, placeholder="Post Clinical Trial Data Here.",label="CTD Content"), 
                    outputs="text")

demo.launch()