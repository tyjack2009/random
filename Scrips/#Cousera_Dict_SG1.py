#Coursera_Dict_SG1

def sum_server_use_time(server):
    
    total_use_time = 0.0
    
    for key,value in server.items():
        total_use_time += server[key]

    return round(total_use_time, 2)

Fileserver = {"EndUser1": 2.25, 
              "EndUser2": 4.5, 
              "EndUser3": 1, 
              "EndUser4": 3.75, 
              "EndUser5": 0.6, 
              "EndUser6": 8
              }

print(sum_server_use_time(Fileserver))