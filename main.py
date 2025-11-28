from doctors import *
import time
from patients import *
from appointments import *
from etc import *

# from etc import *
# from days import *

def main():
     while True:
          decor1()
          show_menu()
          choice = input('Please choose from the menu: ').strip()
          if choice == '':
                print('='*50)
                print(" can't leave it empty please choose again! ".center(50,'X'))
                continue
          elif choice == '1':
                  print('')
                  print('Adding New Doctor ...')
                  doct_message = 'Please Enter Doctors Details: '
                  print('='*50)
                  print(decor(doct_message))
                  call_doc()
                  time.sleep(2.5)
          elif choice == '2':
                print('')
                print('Registering New patient ...')
                print('='*50)
                patient_message ='Please Add Patient Details: '
                print(decor(patient_message))
                call_patient()
                time.sleep(2.5)
          elif choice == '3':
                book_message = 'Booking an Appointment ...'
                print(decor(book_message))
                call_book()
          elif choice == '4':
                choice_4 ='Canceling an Appointment ...'
                print(decor(choice_4))
                call_cancel()
          elif choice == '5':
                schedual_message ="Viewing Doctor's Scheduale ..."
                print(decor(schedual_message))
                call_schedual()
          elif choice == '6':
                history_message ='Viewing Patient History ...'
                print(decor(history_message))
                history()
                time.sleep(5)
          elif choice == '7':
                generate_message ='Generating Daily Appointment List ...'
                print(decor(generate_message))
                generate_daily()
                time.sleep(2.5)
          elif choice == '8':
                available_message ='Checking Doctor Availability ...'
                print(decor(available_message))
                Check_doc_avail()
                time.sleep(5)
                print('')
          elif choice == '9':
                all_appt_message ='Viewing All Appointment ...'
                print(decor(all_appt_message))
                all_appt()
                time.sleep(2.5)
                print('')
          elif choice == '10':
            print('Viewing More Options:[]\n','='*20)
            more = ''
            more = more_opt(more)
            if more == '12':
                  print('Show All Hospital Deptment List:[]\n','='*20)
                  show_dept()
                  print('')
            elif more == "13":
                 print('Showing All doctors list:\n','='*50)
                 all_doctors()
                 print('')
            elif more == '14':
                 print('Viewing All Registered Patient:[]..')
                 show_patients()
                 print('')
            elif more == '15':
                  continue
            else:
                 print('Invalid Choice Please Choose Again! ')
                 more_opt(more)
                 print('')
          elif choice == '11':
            exiting()
            print('')
            break
          else:
            print('Invalid Choice Please Choose Again! ')
            continue


if __name__ == '__main__':
    main()