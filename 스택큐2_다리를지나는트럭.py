from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    bridgeweight = 0
    while bridge:
        answer += 1
        bridgeweight -= bridge.popleft()
        if trucks:
            if bridgeweight+trucks[0] <= weight:
                bridgeweight += trucks[0]
                bridge.append(trucks.popleft())
            else:
                bridge.append(0)
    return answer


bridge_length =2
weight=10
truck_weights=[7,4,5,6]
print(solution(bridge_length, weight, truck_weights))