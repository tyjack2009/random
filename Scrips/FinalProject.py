def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add((event.user,event.IP))
    elif event.type == "logout":
      machines[event.machine].remove((event.user,event.IP))
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(F"{user}: {ip}" for user, ip in users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user, IP_address=None):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user
    self.IP = IP_address

events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan', '10.133.24.1253'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan',),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane', '10.133.635.1234' ),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan','10.133.24.1253'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan',),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris', '10.133.222.6534'),
]

users = current_users(events)
print(users)

generate_report(users)