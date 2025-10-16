import matplotlib.pyplot as plt
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
    startTime,endTime  = [],[]
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
            startTime.append(currentTime)
            endTime.append(currentTime+1)

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

    return CT, TAT, WT, order, startTime, endTime

def XuatDuLieu(n, AT, BT, CT, TAT, WT, order):
    print("Process | Arrival | Burst | Completion | TurnAround | Waiting")
    for i in range(n):
        print(f"P{i+1:7}| {AT[i]:7} | {BT[i]:5} | {CT[i]:10} | {TAT[i]:10} | {WT[i]:7}")

    print("Excuted order:")
    print(" -> ".join(order))

def importGanttChart(order,start,end):
    fig,gnt = plt.subplots()
    gnt.set_xlabel("TIME")
    gnt.set_ylabel("PROCESS")
    gnt.set_title("Gantt Chart")

    #Tao list cac tien trinh duy nhat
    processes = list(sorted(set(order)))

    y_pos = {p:(i+1)*10 for i,p in enumerate(processes)}

    # Draw
    for i in range (len(order)):
        gnt.broken_barh([(start[i], end[i] - start[i])],
                        (y_pos[order[i]], 8),
                        facecolors=('tab:blue'))
        gnt.text(start[i] + (end[i] - start[i]) / 2,
                 y_pos[order[i]] + 4,
                 order[i],
                 ha='center', va='center', color='white', fontsize=9)

    gnt.set_yticks(list(y_pos.values()))
    gnt.set_yticklabels(processes)
    gnt.grid(True)
    plt.show()

def main():
    n,AT,BT= NhapDuLieu()   
    CT,TAT,WT,order,startTime,endTime = sjfNonPreemptive(n,AT,BT)
    XuatDuLieu(n,AT,BT,CT,TAT,WT,order)
    importGanttChart(order,startTime,endTime)

if __name__ == "__main__":
    main()
