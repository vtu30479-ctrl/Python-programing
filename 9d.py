try:
    initial=float(input('enter the initial investment amt:'))
    final=float(input('enter teh final investment amt:'))
    roi=(final-initial)/initial*100
    print('Return on investment(ROI):{:.2f}'.format(roi))
except ValueError:
    print('Error:please enter a valid numeric value for investment amt')
except ZeroDivisionError:
    print('Error:initial investment amount cant be zero')
