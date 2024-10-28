from llama_index.core.workflow import StartEvent,StopEvent,Workflow,step,Event
import asyncio
from llama_index.utils.workflow import draw_all_possible_flows

""" 
#### Basic Workflow where only 1 step is defined 

class MyWorkflow(Workflow):
    @step
    async def my_pavan(self,ev:StartEvent) -> StopEvent:
        return StopEvent(result="Hello, Pavan!")
    

async def main():
    w = MyWorkflow(timeout=10,verbose=False)
    result = await w.run()
    print(result)


draw_all_possible_flows(MyWorkflow, filename="basic_workflow.html")

if __name__ == "__main__":
    asyncio.run(main())


#### Basic workflow working with custom events.

class FirstEvent(Event):
    first_output : str
    
class SecondEvent(Event):
    second_output : str
    
class ThirdEvent(Event):
    third_output : str

class CustomWorkflow(Workflow):
    @step
    async def first_step(self , ev:StartEvent) -> FirstEvent:
        print(ev.first_input)
        return FirstEvent(first_output="First step complete.")
    
    @step
    async def second_step(self , ev : FirstEvent) -> SecondEvent:
        print(ev.first_output)
        return SecondEvent(second_output="Second Step Completed")
    
    @step
    async def third_step(self , ev:SecondEvent) -> ThirdEvent:
        print(ev.second_output)
        return ThirdEvent(third_output="Third Step Completed")
    
    @step
    async def last_step(self , ev:ThirdEvent) -> StopEvent:
        print(ev.third_output)
        return StopEvent(result="Workflow Completed")
    
async def main():
    w = CustomWorkflow()
    result = await w.run(first_input="Start the workflow.")
    print(result)
    
if __name__ == "__main__":
    asyncio.run(main())
"""

## This is an example for me in understanding in deep about workflows.
class FirstNumber(Event):
    first_output : int
    
class SecondNumber(Event):
    second_output : int
    
class ThirdNumber(Event):
    third_output : int
    
class Increment_Number(Workflow):
    @step
    async def first_num(self , ev:StartEvent) -> FirstNumber:
        print("First Input",ev.first_input)
        first_num = ev.first_input
        first_output = first_num + 1
        return FirstNumber(first_output=first_output)
    
    @step
    async def second_num(self , ev:FirstNumber) -> SecondNumber:
        print("Second Input",ev.first_output)
        second_num = ev.first_output
        second_output = second_num + 1
        return SecondNumber(second_output=second_output)
    
    @step
    async def third_num(self , ev : SecondNumber) -> ThirdNumber:
        print("Third Input",ev.second_output)
        third_num = ev.second_output
        third_output = third_num + 1
        return ThirdNumber(third_output=third_output)
    
    @step
    async def last_step(self,ev:ThirdNumber) -> StopEvent:
        print("Last Input",ev.third_output)
        last_num = ev.third_output
        last_output = last_num + 1
        print("",last_output)
        return StopEvent(result="WorkFlow Completed.")
    
async def main():
    w = Increment_Number()
    result = await w.run(first_input = int(input("Enter the Number")))
    print(result)
    
if __name__ == "__main__":
    asyncio.run(main())

draw_all_possible_flows(Increment_Number, filename="basic_workflow.html")