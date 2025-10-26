# =============== SJF preemptive ================
# CPU luon chon tien trinh  co thoi gian xu ly (burst time) nho nhat trong cac tien trinh da den (arrival time <= current time)
# Khi CPU da chon mot tien trinh thi no se xu ly cho den khi hoan tat hoac bi ngat
import matplotlib.pyplot as plt      # thu vien ve chart

def NhapDuLieu():
    n = int(input("Nhap so process: "))                    # nhap so tien trinh
    AT, BT = [], []                                        # tao danh sach ArrivalTime, BurstTime
    # nhap thoi gian den (at) va thoi gian xu ly(bt) cho tung tien trinh
    for i in range(n):
        at = int(input(f"Arrival Time P{i+1}: "))
        bt = int(input(f"Burst Time P{i+1}: "))
        AT.append(at)
        BT.append(bt)
    return n, AT, BT           # tra ve so tien trinh va danh sach AT, BT

# HAM THUC THI SJF (SRTF)
def sjfPreemptive(n, AT, BT):
    completed = [False] * n                # danh dau tien trinh da hoan thanh hay chua
    CT = [0] * n  # Completion Time        # complete time: thoi gian hoan thanh
    TAT = [0] * n # Turn Around Time       # TurnAroundTime: thoi gian ma tien trinh o trong he thong = CT - AT
    WT = [0] * n  # Waiting Time           # WaitingTime: thoi gian cho = TAT - BT
    RT = BT.copy()                         # RemainingTime = BurstTime 
    currentTime = 0                        # thoi gian hien tai
    completedCount = 0                     # so tien trinh hoan thanh
    order = []                             # dung de luu thu tu tien trinh duoc CPU xu ly
    startTime,endTime  = [],[]             # luu thoi diem bat dau va ket thuc cho tung buoc xu ly  (dung cho bieu do)

    # chay cho toi khi tat ca tien trinh hoan tat
    while completedCount < n:
        index = -1                         # lưu vị trí tien trinh dc chon
        minRT = float('inf')               # d(minTime): gia tri nho nhat TAM THOI de tim RT nho nhat

        # tim tien trinh san sang (da den va co RT nho nhat)
        for i in range(n):
            if (AT[i] <= currentTime and not completed[i] and RT[i]<minRT):
                minRT = RT[i]
                index = i
                
        # Neu co P san sang thi giam thoi gian di 1 don vi
        if index != -1:
            RT[index] -= 1 
            order.append(f"P{index+1}")       # them tien trinh duoc chay vao thu tu
            startTime.append(currentTime)     # luu lai thoi gian (dung cho bieu do)
            endTime.append(currentTime+1)     # luu lai thoi gian (dung cho bieu do)

            # Neu P chay xong
            if(RT[index]==0):
                completed[index] = True        # danh dau hoan thanh
                completedCount +=1             # tang so luong P hoan thanh len 1
                CT[index] = currentTime+1      # ghi lai thoi gian hoan thanh cua P do
        else:
            order.append(f"IDLE")              # khong co tien trinh nao san sang
        
        currentTime +=1       # tang 1  don vi thoi gian

    # tinh toan / dung cho bieu do
    for i in range(n):
        TAT[i] = CT[i] - AT[i]
        WT[i] = TAT[i] - BT[i]

    # tra ket qua ve
    return CT, TAT, WT, order, startTime, endTime

def XuatDuLieu(n, AT, BT, CT, TAT, WT, order):
    print("Process | Arrival | Burst | Completion | TurnAround | Waiting")
    for i in range(n):
        print(f"P{i+1:7}| {AT[i]:7} | {BT[i]:5} | {CT[i]:10} | {TAT[i]:10} | {WT[i]:7}")

    print("Excuted order:")
    print(" -> ".join(order))
    
# HAM VE BIEU DO
def importGanttChart(order,start,end):
    fig,gnt = plt.subplots()
    gnt.set_xlabel("TIME")
    gnt.set_ylabel("PROCESS")
    gnt.set_title("Gantt Chart")

    #Tao list cac tien trinh duy nhat (bao gom "IDLE")
    processes = list(sorted(set(order)))

    # gan tung vi tri tren truc Y cho moi tien trinh
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
    gnt.set_xticks(range(0, end[-1] + 1))
    gnt.set_xticklabels([f"{i}s" for i in range(0, end[-1] + 1)])  
    plt.show()

def main():
    n,AT,BT= NhapDuLieu()   
    CT,TAT,WT,order,startTime,endTime = sjfNonPreemptive(n,AT,BT)
    XuatDuLieu(n,AT,BT,CT,TAT,WT,order)
    importGanttChart(order,startTime,endTime)

if __name__ == "__main__":
    main()
