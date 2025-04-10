#Coursera_Dict_SG2

def list_full_names(employee_dictionary):
    full_names = []

    for last_name, first_names in employee_dictionary.items():
        #key,value = last_name, first_names
        for first_name in first_names:



            full_names.append(first_name+" "+last_name)

    return(full_names)

print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"],
                       "Devi": ["Ram", "Amaira"],
                       "Chen": ["Feng", "Li"]
                       }))