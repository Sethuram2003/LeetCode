class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        nprocessor=len(processorTime)
        ntasks=len(tasks)
        processorTime.sort(reverse=True)
        tasks.sort()
        num1=[]
        highest=0
        for i in range(ntasks):
            num1.append(tasks[i]+processorTime[int((i)/4)])
        highest=max(num1)
    

        return (highest)




        