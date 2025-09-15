from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from tools.diagnosis_tool import ai_diagnos
from tools.symptom_checker import check_symptom


class DiagnosticState(TypedDict):
    input: str
    symptom_area: str
    diagnosis: str


def build_graph():
    """Build and return the diagnostic workflow graph."""
    graph = StateGraph(DiagnosticState)

    def symptom_step(state):
        """Process symptoms to determine affected body area."""
        return {
            "input": state["input"],
            "symptom_area": check_symptom.invoke(state["input"]),
            "diagnosis": state.get("diagnosis", "")
        }

    def diagnosis_step(state):
        """Generate AI diagnosis based on symptoms."""
        return {
            "input": state["input"],
            "symptom_area": state["symptom_area"],
            "diagnosis": ai_diagnos.invoke(state["input"])
        }

    # Add nodes to the graph
    graph.add_node("symptomcheck", RunnableLambda(symptom_step))
    graph.add_node("AIdiagnosis", RunnableLambda(diagnosis_step))
    
    # Add edges to define the workflow
    graph.add_edge("symptomcheck", "AIdiagnosis")
    graph.add_edge("AIdiagnosis", END)
    
    # Set the entry point
    graph.set_entry_point("symptomcheck")

    return graph.compile()


# Test function (optional)
if __name__ == "__main__":
    try:
        diagnostic_graph = build_graph()
        print("✓ Graph built successfully!")
    except Exception as e:
        print(f"✗ Error building graph: {e}")


# from typing import TypedDict
# from langgraph.graph import StateGraph, END
# from langchain_core.runnables import RunnableLambda
# # Change these absolute imports to relative imports
# from tools.diagnosis_tool import ai_diagnos
# from tools.symptom_checker import check_symptom


# class DiagnosticState(TypedDict):
#     input: str
#     symptom_area: str
#     diagnosis: str

#     def build_graph():
#         graph = StateGraph(DiagnosticState)

#         def symptom_step(state):
#                 return {
#                         "input":state["input"],
#                         "symptom_area" : check_symptom.invoke(state["input"]),
#                         "diagnosis" : state.get("diagnosis")
#                 }
            
#         graph.add_node("symptomcheck", RunnableLambda(symptom_step))
                        
#         def diagnosis_step(state):
#             return {
#                     "input":state["input"],
#                     "symptom_area" : state["symptom_area"],
#                     "diagnosis" : ai_diagnos.invoke(state["input"])
#             }
        

#         graph.add_node("AIdiagnosis", RunnableLambda(diagnosis_step))
#         graph.add_edge("symptomcheck", "AIdiagnosis")
#         graph.add_edge("AIdiagnosis", END)

#         return graph.compile()
    


