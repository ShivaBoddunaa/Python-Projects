#list of doctors:
#================================
from patients import *
doctors = [
    {
        'Doctor ID':1,
        'Doctor Name':'Mohan',
        'Doctor Speciality':'Cardiologist Doctor',
        'Doctor Availablilty':['Thur','Fri','Sat'],
        # 'Appointments':['Thur']
    },
    {
        'Doctor ID':2,
        'Doctor Name':'Ali',
        'Doctor Speciality':'General Doctor',
        'Doctor Availablilty':['Tue','Wed','Thur'],
        # 'Appointments':['Tue']
    }
]
# adding new doctor function:
#================================
def add_doc(doc_id,doc_name,spel,avail):
    avail = avail.split(',')
    doctors.append(
    {'Doctor ID: ':doc_id,
     'Doctor Name: ':doc_name,
     'Doctor Speciality: ':spel,
     'Doctor Availablilty: ':avail,
    #  'Appointments':appointment
     }
    )
    print('='*70)
    print('  New Doctor Added Successfully!...  '.center(50,'*'))

#================================
def call_doc():
    while True:
        doc_id = input('Enter Doctor ID: ')
        if doc_id == '':
                print('Cant be empty!')
                continue
        elif not doc_id.isdigit():
                print('Only Numbers Please!')
                continue
        else:
                break
    while True:
        doc_name = input('Enter Doctor Name: ').title()
        if doc_name == '':
                print('Cant be empty!')
                continue
        elif doc_name.isdigit():
                print('Only Names Please!')
                continue
        else:
                break
    spel_list()
    spel = spel_choice()
    print(spel)
    avail_days()
    avail = input('Enter Doctor Availabilty: ').title().strip()
    add_doc(doc_id,doc_name,spel,avail)


#getting doctor informations:
#================================
def get_doc():
    return doctors

#getting doctor available days:
#================================
def avail_days():
    print('''Please Choose the Available Days for the Doctor [separate the Entery date by a (,)eg: sat,sun]:
          [1].Mon
          [2].Tue
          [3].Wed
          [4].Thur
          [5].Fri
          [6].Sat
          [7].Sun
               ''')

#showing doctors speciality list:
#================================
def spel_list():
    print('''Please Specify the Doctor Sepciality:
          [1].General Doctor
          [2].Child Doctor 
          [3].General Surgen
          [4].Cardiologist Doctor
          [5].ENT Doctor
          [6].Spine & Brain Doctor
          [7].Dermatologist Doctor
                  ''')

#doctor speciality functions:
#================================
def spel_choice():
    while True:
        spel = input('Enter Doctor Speciality: ').lower().strip()
        if spel == '':
            continue
        elif spel == '1'or spel in ['general doctor','general','doctor']:
            spel = 'General Doctor'
            return spel
        elif spel == '2'or spel in ['child doctor','child']:
            spel = 'Child Doctor'
            return spel
        elif spel == '3'or spel in ['general Surgen','surgen']:
             spel = 'General Surgen'
             return spel
        elif spel == '4'or spel in ['cardiologist doctor','heart', 'cardiologist']:
            spel = 'Cardiologist Doctor'
            return spel
        elif spel == '5'or spel in ['ent doctor','ent']:
            spel = 'ENT Doctor'
            return spel
        elif spel == '6'or spel in ['spine & brain doctor','spine doctor','brain Doctor','spine','brain']:
            spel = 'Spine & Brain Doctor'
            return spel
        elif spel == '7'or spel in ['dermatologist doctor','dermatologist','derma']:
            spel = 'Dermatologist Doctor'
            return spel
        else:
            print('Unknow Option please choose from the list again ')
            continue
def choosed():
    while True:
        spel_list()
        p_dep = spel_choice()
        print(f'You have Choosed [{p_dep}]')
        for doctor in doctors:
            if doctor['Doctor Speciality'] ==  p_dep:
                return p_dep
        else:
            print(f'''*** Sorry Curruntly there is no [{p_dep}] available please choose another doctor speciality! ***''')
            print('='*90)
            print(f'currnetly Available Doctors Are:')
            for doctor in doctors:
                print(f'-{doctor['Doctor Speciality']}: \n Available Days: \n -> {doctor['Doctor Availablilty']}')
            print('='*60)    
            continue
            
            # for k,v in doctor.items():
            #     if v == p_dep:
            #         print(v)
            #     else:
            #         print('Not found')
                # for key, value in doctor.items():
                #     print(f'{key}: {value}')
                    
                # elif  p_dep != doctor['Doctor Speciality'] :
                #     found = False
                #     message =  f'''*** Sorry Curruntly there is no [{p_dep}] available please choose another doctor speciality! *** \nCurrnetly Only: 
                #     \n-{doctor['Doctor Speciality']} is Available'''
                # return 
#appointment records:
#================================
appointment = []
def appo_add(appointment):
    if len(appointment)== 5: 
        return appointment
    while True:
        count = input('Enter Slot Number: ')
        if count == '':
            print('cant be empty!')
            continue
        elif not count.isdigit():
            print('only numbers please')
            continue
        else:
            if count not in appointment:
                appointment.append(count)
                return 'appointment schedual'
            elif count in appointment:
                print('Slot is already Taken Please choose another slot')
                continue
#================================
def spel_list():
    print('''Please Specify the Doctor Sepciality:
          [1].General Doctor
          [2].Child Doctor 
          [3].General Surgen
          [4].Cardiologist Doctor
          [5].ENT Doctor
          [6].Spine & Brain Doctor
          [7].Dermatologist Doctor
                  ''')
    
def check_availability():
   print('='*70)
   for doctor in doctors:
      print('='*70)
      for k,v in doctor.items():
         print(f'-{k}: {v}')

#call Check_avail functions:
#===========================
def Check_doc_avail():
    for n,doc in enumerate (doctors):
        print('')
        print(f'-Doctor:{n+1}')
        print('='*60)
        for key , value in doc.items():
                if  key != 'Doctor ID' and key != 'Appointments':
                    print(f'-{key}: {value}')

#show all doctors functions:
#===========================
def all_doctors():
   for n,doctor in enumerate(doctors):
      print('\n')
      print(f'Doctor: {n+1}')
      print('='*50)
      for k,v in doctor.items():
         print(f'- {k}: {v}')
#show all hospital dep:
#======================
def show_dept():
    for n,doctor in enumerate(doctors):
        print('\n')
        print(f'Deprtment: {n+1}')
        print('='*50)
        for k,v in doctor.items():
            if k == 'Doctor Speciality' or k == 'Doctor Name':
                print(f'- {k}: {v}')
#================================
# appointment = []
# def appo_add(appointment):
#     if len(appointment)== 5: 
#         return appointment
#     while True:
#         count = input('Enter Slot Number: ')
#         if count == '':
#             print('cant be empty!')
#             continue
#         elif not count.isdigit():
#             print('only numbers please')
#             continue
#         else:
#             if count not in appointment:
#                 appointment.append(count)
#                 return 'appointment schedual'
#             elif count in appointment:
#                 print('Slot is already Taken Please choose another slot')
#                 continue
# appo = appo_add(appointment)
# print(appo)