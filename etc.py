def decor1():
    print('*'*70)
    print(('*'*35).center(70,' '))
    print('  Welcome to Doctor Appointment App!  '.center(70,'*'))
    print(('*'*35).center(70,' '))
    print('*'*70)
def show_menu():
     print('''
    =======================================       
    || 1.Add Doctor                      ||
    || 2.Register a patient              ||
    || 3.Book an Appointment             ||
    || 4.Cancel an Appointment           ||
    || 5.View Doctor's Scheduale         ||
    || 6.View Patient History            ||
    || 7.Generate Daily Appointment List ||
    || 8.Check Doctor Availability       ||
    || 9.View All Appointment            ||
    || 10.More Options:[]                ||
    || 11.Exit                           ||
    =======================================
''')
def decor(n):
 return f'''
================================================
||  {n}             ||
================================================
 '''
def more_opt(more):
        print('''
    ===========================================
    || 12.Show All Hospital Deptment List:[] ||
    || 13.Show All doctors list              ||
    || 14.Show All Registerd Patients        ||
    || 15.Go Back                            ||   
    ===========================================
              ''')
        more = input('Please From the Options: ')
        return more

def exiting():
   print('*'*70)
   print('*'*70)
   print('  Exiting The Program Thank you come again please!  '.center(70,'*'))
   print('*'*70)
   print('*'*70)