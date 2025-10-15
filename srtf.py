def NhapDuLieu():
    n = int(input("Nhap so process: "))
    AT, BT = [], []
    for i in range(n):
        at = int(input(f"Arrival Time P{i+1}: "))
        bt = int(input(f"Burst Time P{i+1}: "))
        AT.append(at)
        BT.append(bt)
    return n, AT, BT


def sjfNonPreemptive(n, AT, BT):
    completed = [False] * n
    CT = [0] * n  # Completion Time
    TAT = [0] * n # Turn Around Time
    WT = [0] * n  # Waiting Time
    RT = BT.copy()
    currentTime = 0
    completedCount = 0
    order = []

    while completedCount < n:
        
        index = -1
        minRT = float('inf')

        for i in range(n):
            if (AT[i] <= currentTime and not completed[i] and RT[i]<minRT):
                minRT = RT[i]
                index = i

        if index != -1:
            RT[index] -= 1
            order.append(f"P{index+1}")

            if(RT[index]==0):
                completed[index] = True
                completedCount +=1
                CT[index] = currentTime+1
        else:
            order.append(f"IDLE")
        
        currentTime +=1


    for i in range(n):
        TAT[i] = CT[i] - AT[i]
        WT[i] = TAT[i] - BT[i]

    return CT, TAT, WT, order

def XuatDuLieu(n, AT, BT, CT, TAT, WT, order):
    print("Process | Arrival | Burst | Completion | TurnAround | Waiting")
    for i in range(n):
        print(f"P{i+1:7}| {AT[i]:7} | {BT[i]:5} | {CT[i]:10} | {TAT[i]:10} | {WT[i]:7}")

    print("Excuted order:")
    print(" -> ".join(order))

def main():
    n,AT,BT= NhapDuLieu()
    CT,TAT,WT,order = sjfNonPreemptive(n,AT,BT)
    XuatDuLieu(n,AT,BT,CT,TAT,WT,order)

if __name__ == "__main__":
    main()
