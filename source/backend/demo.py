## Example when Django API start to use function call to X_Action
from AI_source.AI_Services_Manger import AI_Services_Manager
from module.text_module.Text_Action import Text_Action

def main():
    ### Django implementation here, start to pass request through function call to X_Action
    all_services = AI_Services_Manager()
    demo_request_search = {}
    demo_request_refine = {}

    demo_request_search["text"] = "person dog skateboard"
    demo_request_search["type_request"] = "search"
    demo_request_search["limit_size"] = 10
    
    # demo_request_refine["text"] = "demo_text"
    # demo_request_refine["request_type"] = "refine"

    demo_action = Text_Action(demo_request_search)
    ### start to use AI_Services
    results_search = demo_action.process_request(all_services)

    # demo_action = Text_Action(demo_request_refine)
    # results_refine = demo_action.process_request(all_services)
    print(results_search)
    # print(results_refine)

if __name__ == "__main__":
    main()