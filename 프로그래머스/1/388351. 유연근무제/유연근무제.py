def miniute(schedule):
    min = schedule%100
    hour= (schedule-min)//100
    return hour*60+min
def solution(schedules, timelogs, startday):
    
    people=len(schedules)
    answer=0
    
    for i in range(people):
        current_day=startday
        close_time=miniute(schedules[i])+10
        is_okay=True
        for timelog in timelogs[i]:
            if current_day not in (6,7):
                if miniute(timelog)>close_time:
                    is_okay=False
            current_day=(current_day%7)+1
        if is_okay:
            answer+=1
            
      
    return answer