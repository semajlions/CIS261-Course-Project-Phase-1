#James Carpenter
#CIS261 Course Project Phase 1

def gerEmpName():
    empName = input("Enter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter hours: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter hourly rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def prinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay):
    print(empName, f"{hours:, .2f}", f"{hourlyRate:, .2f}", f"{gPay:, .2f}", f"{taxRate:, .1%}", f"{incomeTax:, .2f}", f"{netPay:, .2f}" )
    
def PrinTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay):
    print(f"\nTotal number of employees: {totalemployees}" )
        print(f"Total hours: {totalHours}:, .2f" )
        print(f"Total gross pay: {totalGrossPay}:, .2f" )
        print(f" Total tax: {totalTax}:, .2f" )
        print(f" Total netpay: {totalNetPay}:, .2f" )
              
        
    
              
        

        

