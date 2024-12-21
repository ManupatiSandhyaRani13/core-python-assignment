def search_disease(patients,search):
    matching_patients = []
    for p in patients:
        if p["disease"].lower()==search.lower():
            matching_patients.append(p["name"])
    print(f"Patients with {search} : {matching_patients}")

patients=[]
while True:
    name=input("Enter the name of the patient( or type exit to stop) : ")
    if name.lower()=='exit':
        break
    age=int(input(f"Enter the age of {name} : "))
    disease=input(f"Enter the disease of {name} : ")
    patients.append({"name":name,"Age":age,"disease":disease})
print(f"Patients = {patients}")
search=input("Enter the disease you want to search : ")
search_disease(patients,search)