from patients import *
from doctors import *
from etc import *
week= ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']

appointment = [
    {
        'Patient ID':'1',
        'Patient Name':'Arvind',
        'Patient Doctor Name':'Mohan',
        'Patient Department[Speciality]':'Cardiologist Doctor',
        'Patient Appointment Day':'Thur',
        'Patient Appointment Date':'10/1/2025',
        'Patient Arriving Time':'8:00 AM'
        


    } ,
    {
        'Patient ID':'2',
        'Patient Name':'Krishna',
        'Patient Doctor Name':'Ali',
        'Patient Department[Speciality]':'General Doctor',
        'Patient Appointment Day':'Tue',
        'Patient Appointment Date':'15/3/2025',
        'Patient Arriving Time': '11:00 AM'
    } 
    ]
# schedual = [
#       {
#             'Doctor Name'doc_name,
#             'Slot':0,
#       }
# ]

# def book_appoi():
def book_appoi(p_id,doc_name,p_name,p_appt_date,appt_spel,avail,p_time):
        appointment.append(
        {'1.Patient ID':p_id,
         '2.Patient Name: ':p_name,
         '2.Patient Doctor Name':doc_name,
         '5.Patient Department[Speciality]':appt_spel,
         '3.Patient Appointment Day':avail,
         '4.Patient Appointment Date':p_appt_date,
         '5.Patient appointment Timing':(p_time + ' AM')
        } 
        )
        print('')
        print('='*70)
        print(' *** New Appointment Booked Successfully!... *** '.center(50,'*'))
        print('='*70)
# call Booking Function:
#==========================
def call_book():
    app_p_id = input('Enter Patient Id: ').strip()
    for item in patient:
        if app_p_id == item['Patient ID']:
              p_name = item['Patient Name']
              app_p_id = item['Patient ID']
              print('='*70)
              print(f'You are Booking an Appointment for [{p_name}] Please Choose The Sepcialist Doctor and his Available Day from the List blow:')
              print('='*70)
              for n,doc in enumerate (doctors):
                    print('')
                    print(f'-Doctor:{n+1}')
                    print('-'*60)
                    for key , value in doc.items():
                        if  key != 'Doctor ID':
                                print(f'-{key}: {value}')
              print('='*70)
              appt_spel = int(input('Please Choose a Doctor [Choose #1 /#2 / #3]: ').strip())
              print('='*70)
              if appt_spel == 1:
                    doc_name = doctors[0]['Doctor Name']
                    spel = doctors[0]['Doctor Speciality']
                    print(f'You Have Choosed Dr.[{doctors[0]['Doctor Name']}] His is Available on {doctors[0]['Doctor Availablilty']}')
                    avail = input('Please Choose Suitable Day for your Appointment: ').title().strip()
                    p_appt_date = input('Please Enter Patient Appointment Date [day/Month/year]: ').strip()
                    appt_spel = doctors[0]['Doctor Speciality']
              elif appt_spel == 2:
                    doc_name = doctors[1]['Doctor Name']
                    spel = doctors[1]['Doctor Speciality']
                    print(f'You Have Choosed Dr.[{doctors[1]['Doctor Name']}] His is Available on: {doctors[1]['Doctor Availablilty']}')
                    avail = input('Please Choose Suitable Day for your Appointment: ').title().strip()
                    p_appt_date = input('Please Enter Patient Appointment Date [day/Month/year]: ').strip()
                    appt_spel=doctors[1]['Doctor Speciality']
              elif appt_spel == 3:
                    doc_name = doctors[2]['Doctor Name']
                    spel = doctors[2]['Doctor Speciality']
                    print(f'You Have Choosed Dr.[{doctors[2]['Doctor Name']}] His is Available on: {doctors[2]['Doctor Availablilty']}')
                    avail = input('Please Choose Suitable Day for your Appointment: ').title().strip()
                    p_appt_date = input('Please Enter Patient Appointment Date [day/Month/year]: ').strip()
                    appt_spel=doctors[2]['Doctor Speciality']
              p_time=input('Patient Arriving Time Please put timing in formate eg. [09:00] Please: ').strip().upper()
              book_appoi(app_p_id,doc_name,p_name,p_appt_date,appt_spel,avail,p_time)
              break
    else:
            print('='*60)
            print('''*** \nSorry! Patient is Not In Patient List.\nPlease Register New Patient.\nAnd Book Later!\n***''')
            print('='*60)


#Call Cancel function 
#==========================
def call_cancel():
    p_id = input('Enter Patient ID: ').strip()
    for pat in appointment:
            if pat['Patient ID'] == p_id:
                answer = input(f'Are you Sure You want to Cancel Appoint ment for [{pat['Patient Name']}] Y/N: ').strip().lower()
                if answer in ['y','yes']:
                        appointment.remove(pat)
                        print('='*90)
                        print(f'*** Appointment for the Patient for the Following patient Was Canceled Sucussfully! ***')
                        print('='*90)
                        for p , d in pat.items():
                            if p != 'Patient ID':
                                    print(f'-{p}: {d}')
                else:
                        cancel_message = f'Appointment Was Not Canceled for [{pat['Patient Name']}]'
                        print(decor(cancel_message))
                        break
            else:
             print('Sorry Cant Find Patient ID Very Patient ID Please!')

#call Schedual function:
#============================
def call_schedual():
      for index, appnt in enumerate (appointment):
                  print('')
                  print(f'{index+1}- Schedual for Dr.[{appnt['Patient Doctor Name']}]')
                  print('='*50)
                  for sec1 , sec2 in appnt.items():
                        if sec1 != 'Patient ID' and sec1 != 'Patient Name' :
                              print(f'{sec1}: {sec2}')
#call generate daily appointment list:
#=====================================
def generate_daily():
    for day in week:
                    print(f'\n-{day}day Appointments:')
                    print('=' * 60)
                    for book in show_book():
                        if book['Patient Appointment Day'] == day:
                                for k, v in book.items():
                                    if k != 'Patient ID':
                                            print(f'{k}: {v}')
                                print('-' * 60)
                                break
                    else:
                        print('Sorry! No Appointment For The Day')

#call all appointment function:
#==============================
def all_appt():
    for n, book in enumerate(show_book()):
        print('')
        print(f'Appointment{n+1}:')
        print('='*60)
        for k,v in book.items():
                if k != 'Patient ID' :
                    print(f'-{k}: {v}')
def show_book():
    return appointment
# def del_book():
      
