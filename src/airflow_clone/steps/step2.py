def multiply_my_sum(my_sum, node_id, multiplier, set_xargs):
    result = my_sum * multiplier
    
    print(f"Result of {node_id} is {result}")
    set_xargs(name=f"{node_id}_result", value=result)