## Example when Django API start to use function call to X_Action
from AI_source.AI_Services_Manger import AI_Services_Manager
from module.text_module.Text_Action import Text_Action

def main():
    ### Django implementation here, start to pass request through function call to X_Action
    all_services = AI_Services_Manager()
    demo_request = {}
    demo_request["text"] = "demo_text"
    demo_action = Text_Action(demo_request)
    ### start to use AI_Services
    results_search = demo_action.process_search(all_services)
    results_refine = demo_action.process_refine(all_services)
    print(results_search)
    print(results_refine)

if __name__ == "__main__":
    main()