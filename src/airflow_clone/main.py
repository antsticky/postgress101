from airflow_clone.src.node import ExecutionNode
from airflow_clone.src.node_executor import Executor

from airflow_clone.steps.step1 import add_two_num
from airflow_clone.steps.step2 import multiply_my_sum
from airflow_clone.steps.step3 import add_up_two_result
from airflow_clone.steps.step4 import end_fn

def main():
    with Executor() as executor:               
        start_node = ExecutionNode("Initialization step", python_operator=add_two_num, configs={"a": 1, "b": 3})
        step_1a = ExecutionNode("Multiply 2a step", python_operator=multiply_my_sum, xargs=["my_sum"], configs={"node_id": "step_2a", "multiplier": 5})
        step_1b = ExecutionNode("Multiply 2b step", python_operator=multiply_my_sum, xargs=["my_sum"], configs={"node_id": "step_2b", "multiplier": 10})
        step_2 = ExecutionNode("Add Result 3 step", python_operator=add_up_two_result, xargs=["step_2a_result", "step_2b_result"])
        end_task = ExecutionNode("End step", python_operator=end_fn)

        start_node >> step_1a >> step_2
        start_node >> step_1b >> step_2
        step_2 >> end_task

        executor.execute(start_node)
        
if __name__ == "__main__":
    main()