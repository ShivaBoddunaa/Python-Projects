patient = [
    {
        'Patient ID':'1',
        'Patient Name':'Arvind',
        'Patient Age':32,
        'Patient Contact Number':123456789,
    },
    {
        'Patient ID':'2',
        'Patient Name':'Krishna',
        'Patient Age':32,
        'Patient Contact Number':987654321,
    },
    {
        'Patient ID':'3',
        'Patient Name':'SRK',
        'Patient Age':56,
        'Patient Contact Number':8952356,
        
    }
]
def add_patient(app_p_id,p_name,p_age,p_contact):
    patient.append(
    {'Paitent ID':app_p_id,
     'Patient Name':p_name,
     'Patient Age':p_age,
     'Patient Contact Number':p_contact
     }
    )
    print('='*70)
    print('  New Patient Added Successfully!...  '.center(50,'*'))
# Call Patient Functions:
#==========================
def call_patient():
    while True: #Patient ID
        p_id = input('Enter Patient ID: ')
        if p_id == '':
            print('Cant be empty!')
            continue
        elif not p_id.isdigit():
            print('Only Numbers Please!')
            continue
        else:
            break
    while True: # Patient Name...
        p_name = input('Enter Patient Name: ').title()
        if p_name == '':
            print('Cant be empty!')
            continue
        elif p_name.isdigit():
            print('Only Names Please!')
            continue
        else:
            break
    while True: # Patient Age...
            p_age = input('Enter Patient Age: ')
            if p_age == '':
                    print('Cant be empty!')
                    continue
            elif not p_age.isdigit():
                    print('Only Numbers Please!')
                    continue
            else:
                    break
    while True: # Patient Contact...
            p_contact = input('Enter Patient Contact Number: ')
            if p_contact == '':
                    print('Cant be empty!')
                    continue
            elif not p_contact.isdigit():
                    print('Only Numbers Please!')
                    continue
            else:
                    break
    add_patient(p_id,p_name,p_age,p_contact)
#Call Patient History Function:
#==============================
def history():
    get_patients = get_patient()
    for k1 ,pat in enumerate(get_patients):
            print('')
            print(f'-History for Patient {k1+1}')
            print('='*60)
            for key , value in pat.items():
                    print(f'-{key}: {value}')
#Show all patient:
#=================
def show_patients():
    for n,patien in enumerate(patient):
        print('\n')
        print(f'Patinet: {n+1}')
        print('='*50)
        for k,v in patien.items():
            print(f'- {k}: {v}')

def get_patient():
    return patient